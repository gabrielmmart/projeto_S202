from fastapi import APIRouter
from models.type import Type
from config.db import conn 
from schemas.card import serializeDict, serializeList
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

typeCard = APIRouter()


@typeCard.get('/type')
async def find_all_types():
    return serializeList(conn.local.type.find())


@typeCard.post('/type')
async def create_type(typeCard: Type):
    conn.local.type.insert_one(dict(typeCard))
    return serializeList(conn.local.type.find())


@typeCard.delete('/type/{id}')
async def delete_type(id):
    return serializeDict(conn.local.type.find_one_and_delete({'_id': ObjectId(id)}))


@typeCard.put('/type/{id}')
async def update_type(id: str, typeCard: Type):
    conn.local.type.find_one_and_update({'_id': ObjectId(id)}, {
        '$set': dict(typeCard)
    })
    return serializeDict(conn.local.type.find_one({'_id': ObjectId(id)}))
