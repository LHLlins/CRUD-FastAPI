from sqlalchemy import Column, Integer, String, Boolean, Float
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy_utc import UtcDateTime

class MedicoesModels(Base):
    __tablename__ = 'medicoesdados2'
    
    # id=Column(Integer, primary_key=True)
    gateway_id=Column(String, primary_key=True)
    gateway_name=Column(String)
    number_of_registered_sensors=Column(Integer)
    valid_configurations=Column(Boolean)
    percentual_valid_configurations_perc=Column(Float)
    expected_measurements=Column(Float)
    signal_mean_value=Column(Float)
    signal_status=Column(String)
    signal_issue=Column(Float)
    elapsed_time_since_last_measurement = Column(UtcDateTime)
    measurement_status=Column(String)
    one_hour_groups=Column(Integer)