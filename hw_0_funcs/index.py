#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pow
from time import time

#  --- ЗАДАНИЕ 1 ---


def show_spent_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        finish = time() - start
        print('Finished in: %.6f ms' % finish)
        return res
    return wrapper


# возвращает список переданных чисел в квадрате
# либо в стпени, переданной в именованном аттрибуте pwr
@show_spent_time
def pow_list(*args, pwr=2):
    return [int(pow(i, pwr)) for i in args]


# возвращает простое целое число если
# вспомогательная функция для фильтрации
def getPrime(num):
    deviders = [2, 3]
    is_complex = True

    if num > 1 and not num in deviders:
        is_complex = [i for i in deviders if num % i == 0]
        return num if not is_complex else None
    elif num in deviders:
        return num


# возвращает список чисел, отфильтрованных согласно заданию
@show_spent_time
def even_odd_prime(*args, **kwargs):
    switch = {
        'even': list(filter(lambda x: not x % 2, args)),
        'odd': list(filter(lambda x: x % 2, args)),
        'prime': list(filter(getPrime, args))
    }
    return switch[kwargs['num_type']]


if __name__ == '__main__':
    print(even_odd_prime(*[i for i in range(102)], num_type='prime'))
