from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schema import schemas
from sqlalchemy import select, delete, update


class RepositorioMedicoes():

    def __init__(self, db: Session):
        self.db = db 
    

    # Criar as medições
    def criar(self, medicoesdados: schemas.MedicoesSchemas): 
        db_medicoesdados = models.MedicoesModels(
                            # id=medicoesdados.id,
                            gateway_id=medicoesdados.gateway_id,
                            gateway_name=medicoesdados.gateway_name,
                            number_of_registered_sensors=medicoesdados.number_of_registered_sensors,
                            valid_configurations=medicoesdados.valid_configurations,
                            percentual_valid_configurations_perc=medicoesdados.percentual_valid_configurations_perc,
                            expected_measurements=medicoesdados.expected_measurements,
                            signal_mean_value=medicoesdados.signal_mean_value,
                            signal_status=medicoesdados.signal_status,
                            signal_issue=medicoesdados.signal_issue,
                            elapsed_time_since_last_measurement=medicoesdados.elapsed_time_since_last_measurement,
                            measurement_status=medicoesdados.measurement_status,
                            one_hour_groups=medicoesdados.one_hour_groups
                            )
        self.db.add(db_medicoesdados) 
        self.db.commit() 
        self.db.refresh(db_medicoesdados) 
        return db_medicoesdados

    #Remover as medições a partir do gateway especificado    
    def remover(self, gateway_id: str):
        stmt = delete(models.MedicoesModels).where(models.MedicoesModels.gateway_id == gateway_id)

        self.db.execute(stmt)
        self.db.commit()

    # Exibir as todas as medições
    def listar(self): 
        medicoesdados = self.db.query(models.MedicoesModels).all() 

        return medicoesdados
    
    def editar(self, gateway_id: str, medicoesdados: schemas.MedicoesSchemas): 
        stmt = (update(models.MedicoesModels).
                where(models.MedicoesModels.gateway_id == gateway_id).
                values(gateway_id=medicoesdados.gateway_id,
                        gateway_name=medicoesdados.gateway_name,
                        number_of_registered_sensors=medicoesdados.number_of_registered_sensors,
                        valid_configurations=medicoesdados.valid_configurations,
                        percentual_valid_configurations_perc=medicoesdados.percentual_valid_configurations_perc,
                        expected_measurements=medicoesdados.expected_measurements,
                        signal_mean_value=medicoesdados.signal_mean_value,
                        signal_status=medicoesdados.signal_status,
                        signal_issue=medicoesdados.signal_issue,
                        elapsed_time_since_last_measurement=medicoesdados.elapsed_time_since_last_measurement, 
                        measurement_status=medicoesdados.measurement_status,
                        one_hour_groups=medicoesdados.one_hour_groups
                       )
                )
        self.db.execute(stmt)
        self.db.commit()
   
    # Obter as medições do gateway específico
    def obter(self, gateway_id: str):
        stmt = select(models.MedicoesModels).filter_by(gateway_id=gateway_id)
        medicoesdados = self.db.execute(stmt).one()

        return medicoesdados
    
    
