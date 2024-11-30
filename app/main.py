from fastapi import FastAPI
from app.routers import insurance, tariffs
from app.database import engine, Base

app = FastAPI()

# Создание таблиц в БД
Base.metadata.create_all(bind=engine)

# Подключение роутеров
app.include_router(insurance.router)
app.include_router(tariffs.router)
