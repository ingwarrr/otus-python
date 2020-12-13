#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pow
import time

#  --- ЗАДАНИЕ 1 ---

def showSpendedTime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time() - start
        print('Finished in: %.6f ms' % finish)
        return res
    return wrapper

# возвращает список переданных чиел в квадрат
@showSpendedTime
def powList(*args, pwr = 2):
    return [int(pow(i, pwr)) for i in args]

# возвращает простое целое число если
# вспомогательная функция для фильтрации
def getPrime(num):
    deviders = [2,3]
    isComplex = True

    if num > 1 and not num in deviders:        
        isComplex = [i for i in deviders if num % i == 0]        
        return num if not isComplex else None
    elif num in deviders:
        return num

# возвращает список отфильтрованных чисел
@showSpendedTime
def evenOddPrime(*args, **kwargs):
    switch = {
        'even': list(filter(lambda x: not x%2, args)),
        'odd': list(filter(lambda x: x%2, args)),
        'prime': list(filter(getPrime, args))
    }
    return switch[kwargs['numType']]
    
print(evenOddPrime(*[i for i in range(102)], numType = 'prime'))
