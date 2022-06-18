from pydantic import BaseModel

class Skill(BaseModel):
    nome: str
    efeito: str
    descricao: str
    