from src.infra.sqlalchemy.repositorios.medicoesdados import RepositorioMedicoes
from src.infra.sqlalchemy.config.database import criar_db, get_db
from fastapi import APIRouter, status, Depends, HTTPException 
from src.schema.schemas import MedicoesSchemas
from sqlalchemy.orm import Session
from typing import List


criar_db()

router = APIRouter()


@router.post('/criar', status_code = status.HTTP_201_CREATED)
async def criar_coleta(medicoesdados: MedicoesSchemas, db: Session = Depends(get_db)):
    coleta_criada = RepositorioMedicoes(db).criar(medicoesdados)
    return coleta_criada

@router.get('/listar',status_code = status.HTTP_200_OK, response_model = List[MedicoesSchemas])
async def listar_coletas(db: Session = Depends(get_db)):
    coletas_criadas = RepositorioMedicoes(db).listar()
    return coletas_criadas


@router.get('/mostrar/{gateway_id}')
async def exibir_produtos(gateway_id:str, db:Session = Depends(get_db)):
    gateway_localizado = RepositorioMedicoes(db).obter(gateway_id)
      
    if not gateway_localizado:
        raise HTTPException(status_code=404, detail = f'Não existe {gateway_id}')
    return gateway_localizado


@router.put('/editar/{gateway_id}', response_model = MedicoesSchemas)
async def editar_produtos(gateway_id:str, medicoesdados: MedicoesSchemas, db: Session = Depends(get_db)):
    coleta_editada = RepositorioMedicoes(db).editar(gateway_id, medicoesdados)
    return coleta_editada

@router.delete('/remover/{gateway_id}', response_model = MedicoesSchemas)
async def remover(gateway_id:str, db: Session = Depends(get_db)):
    coleta_removida = RepositorioMedicoes(db).remover(gateway_id)
    return coleta_removida

