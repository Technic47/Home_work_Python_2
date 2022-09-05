# Реализуйте алгоритм перемешивания списка.

import random

number = int(input('Enter your number: '))
numbers = []

for i in range(number):
    num = random.randint(10, 99)
    numbers.append(num)
print(f"{numbers} - Original list")

random.shuffle(numbers)
print(f"{numbers} - Build in shaffle")

indexs = []
for i in range(len(numbers)):
    index = random.randint(0, number - 1)
    if index in indexs:
        while index in indexs:
            index = random.randint(0, number - 1)
    indexs.append(index)
    indexs[i] = numbers[indexs[i]]


print(f"{indexs} - Selfmade shaffle")
