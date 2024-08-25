import json

def criar_Player(nome, hp, atk):
    ficha = {
        'nome':nome, 
        'hp': hp,
        'atk': atk
    }
    return ficha

def salvar(arquivo):
    with open('save.json', 'wt') as save:
        json.dump(arquivo, save)

def carregar():
    with open('save.json', 'rt') as save:
        return json.load(save)

