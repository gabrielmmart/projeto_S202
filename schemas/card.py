# Normal way
def cardEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "cor":item["cor"],
        "dano":item["dano"],
        "habilidades":item["habilidades"],
        "imgURL":item["imgURL"],
        "manas":item["manas"],
        "nome":item["nome"],
        "raridade":item["raridade"],
        "resistencia":item["resistencia"],
        "subtipos":item["subtipos"],
        "texto_ilustrativo":item["texto_ilustrativo"]
    }

def cardsEntity(entity) -> list:
    return [cardEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]