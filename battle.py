from random import randint 
from os import system
from time import sleep

Player = {'nome':input('digite seu nome: '), 'atk': 2, 'hp': 20}
Monstro = [
    {'nome':"Slime", 'atk': 1, 'hp': 10},
    {'nome':"Goblin", 'atk': 2, 'hp': 20},
    {'nome':"Orc", 'atk': 5, 'hp': 35},
    {'nome':"Troll", 'atk': 8, 'hp': 65},
    {'nome':"Dragão", 'atk': 15, 'hp': 100}
    ]

for c in range(0, 5):

    print(f"Você econtrou um {Monstro[c]['nome']}")
    while True:
        
        print(f"{Monstro[c]['nome']} = {Monstro[c]['hp']} hp")
        print(f"{Player['nome']} = {Player['hp']} hp")
        sleep(1)
        acao = input('''Oque você vai fazer:
[0] - Atacar
'''
        )
        system('cls')
        if acao == '0':
            print(f"você deu {Player['atk']} de dano")
            sleep(1)
            Monstro[c]['hp'] -= Player['atk']
            print(f"você recebeu {Monstro[c]['atk']} de dano")
            sleep(1)
            Player['hp'] -= Monstro[c]['atk']
            
        if Monstro[c]['hp'] <= 0:
            print(f"parabens {Player['nome']} você upou de nivel!")
            sleep(1)
            Player['hp'] += 10
            Player['atk'] += 2
            if Monstro[c]['nome'] == 'Goblin':

                Player['hp'] += 10
                Player['atk'] += 3
                
            if Monstro[c]['nome'] == 'Orc':

                Player['hp'] += 20
                Player['atk'] += 5
                
            if Monstro[c]['nome'] == 'Troll':
                print(f"{Player['nome']}!")
                sleep(2)
                print(f"Com a morte do troll, você achou uma espada flamejante!")
                Player['hp'] += 40
                Player['atk'] += 15
            break
        if Player['hp'] <= 0:
            if Monstro[c]['nome'] == 'Orc':
                print(f"Seu hp chegou em {Player['hp']} porem...")
                sleep(1)
                print('...')
                sleep(1)
                print('...')
                sleep(1)
                print('Sua alma não aceita a morte, então com um suspiro da vida, você recebe hp')
                Player['hp'] += 50
                
            else:
                print(f"seu hp chegou em {Player['hp']}")
                sleep(1)
                print("Game over")
                break
        
    if Player['hp'] <= 0:

        break
if Monstro[4]['hp'] <= 0:
    print(f"Parabens {Player['nome']} você ganhou o jogo!!!")
    