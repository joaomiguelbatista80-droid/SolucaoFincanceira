from fastapi import FastAPI

from .database import engine, Base
from .auth import router as auth_router


# Cria as tabelas do banco de dados
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Solução Financeira IA",
    description="Sistema de organização e educação financeira baseado em Inteligência Artificial.",
    version="0.1.0"
)


# Adiciona as rotas de autenticação
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Solução Financeira IA está funcionando!"
    }