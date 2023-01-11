num1 = int(input("Введіть число: "))


num1b = bin(num1)
num1b = str(num1b)
num1b = list(num1b)

count = 0


for i in round(len(num1b)):
    if num1b[i] == 1:
        count += 1

print("Кількість одиниць в вашому двійковому числі дорівнює:",  count)