# 5'. Реализуйте алгоритм перемешивания списка.

from random import shuffle
from random import randint

mass = list(map(int, input('Введите спсиок цифр: ').split()))
print(f'Введён список: {mass}')
print(f'Смешанный список: {shuffle(mass)}')
for i in range(len(mass)-1):
    n = randint(0,len(mass)-1)
    mass[i], mass[n] = mass[n], mass[i]
print(mass)
