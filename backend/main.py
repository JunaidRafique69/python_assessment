import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.post("/task/")
async def create_task():
    task_id = random.randint(1000, 9999)
    print(f"Task created with ID: {task_id}")  
    return {"task_id": task_id}
