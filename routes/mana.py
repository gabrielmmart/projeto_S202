from fastapi import APIRouter
from models.mana import Mana
from config.db import conn 
from schemas.card import serializeDict, serializeList
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

mana = APIRouter()

@mana.get('/mana')
async def find_all_manas():
    return serializeList(conn.local.mana.find())

@mana.post('/mana')
async def create_mana(mana: Mana):
    conn.local.mana.insert_one(dict(mana))
    return serializeList(conn.local.mana.find())

@mana.delete('/mana/{id}')
async def delete_mana(id,mana: Mana):
    return serializeDict(conn.local.mana.find_one_and_delete({"_id":ObjectId(id)}))


@mana.put('/mana/{id}')
async def update_mana(id,mana: Mana):
    conn.local.mana.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(mana)
    })
    return serializeDict(conn.local.mana.find_one({"_id":ObjectId(id)}))