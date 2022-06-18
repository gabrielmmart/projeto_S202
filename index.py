from fastapi import FastAPI
from routes.card import card 
app = FastAPI()
app.include_router(card)
