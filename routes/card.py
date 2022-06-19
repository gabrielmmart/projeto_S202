from fastapi import APIRouter
from models.card import Card 
from models.card import Mana
from config.db import conn 
from schemas.card import serializeDict, serializeList
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
card = APIRouter() 
mana = APIRouter()

@card.get('/card')
async def find_all_cards():
    return serializeList(conn.local.card.find())

@card.get('/card/nome')
async def buscar_por_nome(nome):
    return serializeList(conn.local.card.find({"nome":nome}))

@card.get('/card/cor')
async def buscar_por_cor(cor):
    return serializeList(conn.local.card.find({"cor":cor}))

@card.get('/card/raridade')
async def buscar_por_raridade(raridade):
    return serializeList(conn.local.card.find({"raridade":raridade}))

@card.post('/card')
async def create_card(card: Card):
    conn.local.card.insert_one(dict(card))
    return serializeList(conn.local.card.find())

# @mana.post('/criar mana')
# async def create_card(mana: Mana):
#     conn.local.card.insert_one(dict(mana))
#     return serializeList(conn.local.card.find())

@card.put('/card/{id}')
async def update_card(id,card: Card):
    conn.local.card.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(card)
    })
    return serializeDict(conn.local.card.find_one({"_id":ObjectId(id)}))

# @card.patch('/update cor/{id}')
# async def update_cor(id,card: Card):
#     id = card.id
    

@card.delete('/card/{id}')
async def delete_card(id,card: Card):
    return serializeDict(conn.local.card.find_one_and_delete({"_id":ObjectId(id)}))