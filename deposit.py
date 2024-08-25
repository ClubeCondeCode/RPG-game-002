



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
    from random import randint

    n = randint(1, number)
    return n





