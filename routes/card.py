from fastapi import APIRouter
from models.card import Card 
from models.card import Mana
from config.db import conn 
from schemas.card import serializeDict, serializeList
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
card = APIRouter() 
mana = APIRouter()

@card.get('/buscar todas as cartas')
async def find_all_cards():
    return serializeList(conn.local.card.find())

@card.get('/buscar carta por nome')
async def buscar_por_nome(nome):
    return serializeDict(conn.local.card.find_one({"nome":nome}))

@card.get('/buscar carta por cor')
async def buscar_por_cor(cor):
    return serializeDict(conn.local.card.find_one({"cor":cor}))

@card.get('/buscar carta por raridade')
async def buscar_por_cor(raridade):
    return serializeDict(conn.local.card.find_one({"raridade":raridade}))

@card.post('/criar carta')
async def create_card(card: Card):
    conn.local.card.insert_one(dict(card))
    return serializeList(conn.local.card.find())

@mana.post('/criar mana')
async def create_card(mana: Mana):
    conn.local.card.insert_one(dict(mana))
    return serializeList(conn.local.card.find())

@card.put('/update carta/{id}')
async def update_card(id,card: Card):
    conn.local.card.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(card)
    })
    return serializeDict(conn.local.card.find_one({"_id":ObjectId(id)}))

@card.patch('/update cor/{id}')
async def update_cor(id,card: Card):
    id = card.id
    

@card.delete('/deletar carta/{id}')
async def delete_card(id,card: Card):
    return serializeDict(conn.local.card.find_one_and_delete({"_id":ObjectId(id)}))