import random

def PASSGENERATOR():

    num = 1

    while num != 0:
        symbol = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '(', ')']

        password = ""

        num = int(input("\n\nКількість символів в паролі: "))


        for i in range(num):
            rand_num = random.randint(0, len(symbol))     #рандомні числа
            password += symbol[rand_num]
        print("\n\n", password, sep="", end="\n\n")
        password = ""


PASSGENERATOR()

