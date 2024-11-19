from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import crud
from datetime import datetime

app = FastAPI()

# Pydantic models for validation
class actorinfo(BaseModel):
    actor_id: int
    first_name: str
    last_name: str
    last_update: datetime

class FieldCreate(actorinfo):
    pass

class FieldResponse(actorinfo):
    actor_id: int

@app.post("/actors/", response_model=FieldResponse)
def create_field(actor: FieldCreate):
    return crud.create_field(actor)

@app.get("/actor/{actor_id}", response_model=FieldResponse)
def read_field(actor_id: int):
    actor = crud.get_field(actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@app.get("/actors/", response_model=list[FieldResponse])
def read_actors(skip: int = 0, limit: int = 10):
    return crud.get_field(skip, limit)

@app.put("/actors/{actor_id}", response_model=FieldResponse)
def update_actor(actor_id: int, updates: dict):
    actor = crud.update_field(actor_id, updates)
    if not actor:
        raise HTTPException(status_code=404, detail="actor not found")
    return actor

@app.delete("/actors/{actor_id}", response_model=dict)
def delete_field(actor_id: int):
    return crud.delete_field(actor_id)
