from fastapi import FastAPI
from .config import create_tables
from .routers import router


create_tables()
app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message":"Welcome to Agrim"}
