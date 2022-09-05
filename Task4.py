# Задайте список из N элементов, заполненных числами
# из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем
# через пробел позициях.

number = int(input('Enter your number: '))
numbers = []
count = -number

for i in range(number*2):
    count += 1
    numbers.append(count)

print(numbers)
pos = input('Enter positions via space: ').split(' ')
numpos = 0
mult = 1
for i in range(len(pos)):
    numpos = int(pos[i])
    mult *= numbers[numpos]

print(mult)