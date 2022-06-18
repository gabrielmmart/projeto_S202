from pydantic import BaseModel

class Card(BaseModel):
    id: str
    cor: str
    dano: str
    habilidades: object
    imgURL: str
    manas: object
    nome: str
    raridade: str
    resistencia: str
    subtipos: object
    texto_ilustrativo: str

class Mana(BaseModel):
    tipo: str