import random

symbol = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '!', '?', ' ']


text = list(input("Enter text (only english): "))

print(len(symbol)) #31

for i in range(len(text)):
    for j in range(len(symbol)):
        if text[i] == symbol[j]:
            text[i] = symbol[j]
                    

print(text)
