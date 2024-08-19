



def printy(text, speed = 0.01, n = True):
    from time import sleep
    from sys import stdout

    for txt in text:
        stdout.write(txt)
        stdout.flush()
        sleep(speed)
    if n == True:
        print()
    else:
        return ''

def roll(number):
    from time import sleep
    from random import randint
    import os

    n = randint(0, number)
    time = 0.1
    for c in range(20):
        sleep(time)
        os.system('cls')
        if c == 10:
            time = 0.3
        if c == 15:
            time = 0.5
        print(randint(0, number))
        
        
    n = f'\033[0;32;40m{n}\033[m'
    os.system('cls')
    return n





