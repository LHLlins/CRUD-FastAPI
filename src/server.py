from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_medicoes 


app = FastAPI()


origins = ["http://localhost:8080"]

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(rotas_medicoes.router)

