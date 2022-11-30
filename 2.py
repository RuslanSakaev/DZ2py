# 2'. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math

def mult(n: int) -> str:
    str_mult = '1'
    for i in range(2, n+1):
        if i == n:
            str_mult += f'*{i}'
        else:
            str_mult += f'*{i}'

    return str_mult

n = int(input("Введите число: "))
multiplicatins = [math.factorial(i) for i in range(1, n+1)]
multiplicatins_string = [mult(i) for i in range(1, n+1)]
print(f"Произведения чисел от 1 до {multiplicatins}")
print(f"Произведения чисел от 1 до {multiplicatins_string}")