from fastapi import FastAPI
from routes.card import card 
from routes.mana import mana
from routes.skill import skill
from routes.type import typeCard
from routes.subtype import subtype
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE"],
    allow_headers=["*"],
)


app.include_router(card) # Mount a router on the ap
app.include_router(mana)
app.include_router(skill)
app.include_router(typeCard)
app.include_router(subtype)
