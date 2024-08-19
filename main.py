from time import sleep
from deposit import printy, roll
'''from deposit import printy'''

printy('Bem vindo aventureiro!')
sleep(1)
nome = str(input(printy('Qual sera seu nome nessa aventura? ', n = False))).strip().capitalize()
printy(f'bom {nome}, nesse RPG, as coisas são decididas pelos numeros aleatorios')
input(printy('então vamos decidir quais vão ser seus atributos?', n = False))

sleep(0.5)
n = roll(10)
sleep(1)

print(f'seu numero foi: {n}')
