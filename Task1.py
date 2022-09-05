# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

number = input('Enter your number: ')
count = 0

for i in range(len(number)):
    if number[i].isdigit():
        count += int(number[i])

print(count)