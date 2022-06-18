from fastapi import APIRouter
from models.skill import Skill
from config.db import conn 
from schemas.card import serializeDict, serializeList
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

skill = APIRouter()

@skill.get('/skill')
async def find_all_skills():
    return serializeList(conn.local.skill.find())


@skill.get('/skill/{id}')
async def find_skill_by_id(id: str):
    return serializeDict(conn.local.skill.find_one({'_id': ObjectId(id)}))


@skill.post('/skill')
async def create_skill(skill: Skill):
    conn.local.skill.insert_one(dict(skill))
    return serializeList(conn.local.skill.find())


@skill.delete('/skill/{id}')
async def delete_skill(id: str, skill: Skill):
    return serializeDict(conn.local.skill.find_one_and_delete({'_id': ObjectId(id)}))


@skill.put('/skill/{id}')
async def update_skill(id: str, skill: Skill):
    conn.local.skill.find_one_and_update({'_id': ObjectId(id)}, {
        '$set': dict(skill)
    })
    return serializeDict(conn.local.skill.find_one({'_id': ObjectId(id)}))

