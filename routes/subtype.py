from fastapi import APIRouter
from models.subtype import Subtype
from config.db import conn 
from schemas.card import serializeDict, serializeList
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

subtype = APIRouter()


@subtype.get('/subtype')
async def find_all_subtypes():
    return serializeList(conn.local.subtype.find())


@subtype.get('/subtype/{id}')
async def find_subtype_by_id(id: str):
    return serializeDict(conn.local.subtype.find_one({'_id': ObjectId(id)}))


@subtype.post('/subtype')
async def create_subtype(subtype: Subtype):
    conn.local.subtype.insert_one(dict(subtype))
    return serializeList(conn.local.subtype.find())


@subtype.delete('/subtype/{id}')
async def delete_subtype(id: str):
    return serializeDict(conn.local.subtype.find_one_and_delete({'_id': ObjectId(id)}))


@subtype.put('/subtype/{id}')
async def update_subtype(id: str, subtype: Subtype):
    conn.local.subtype.find_one_and_update({'_id': ObjectId(id)}, {
        '$set': dict(subtype)
    })
    return serializeDict(conn.local.subtype.find_one({'_id': ObjectId(id)}))
