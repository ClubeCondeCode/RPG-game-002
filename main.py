from time import sleep
from deposit import printy, roll
from player import criar_Player, salvar, carregar

try:
    player = carregar()
    printy(f"bem vindo {player['nome']}")

except FileNotFoundError:
    printy('Bem vindo aventureiro!')
    #sleep(1)
    nome = str(input(printy('Qual sera seu nome nessa aventura? ', n = False))).strip().capitalize()
    printy(f'bom {nome}, nesse RPG, as coisas são decididas pelos numeros aleatorios')
    #sleep(1)
    input(printy('então vamos decidir quais vão ser seus atributos?', n = False))

    player = criar_Player(nome, roll(20), roll(5))
    del nome

    printy(f'bom... {player['nome']} seus stributos ficaram assim: {player}')
    #sleep(1)
    girar = input(printy(f'você deseja salvar e continuar ou girar novamente?[S para salvar|R para girar novamente] ', n = False))[0].strip().upper()
    if girar == 'S':
        salvar(player)
    if girar == 'R':
        while True:
            nome = input(printy('qual sera seu nome?: ', n = False)).strip().capitalize()
            player = criar_Player(nome, roll(20), roll(5))
            printy(f'seus stributos: {player}')
            if input(printy('[S/R]: ', n = False)).upper().strip() == 'S':
                salvar(player)
                break

#abandon


