from pydantic import BaseModel

class Mana(BaseModel):
    tipo: str
    cor: str
    imgURL: str
