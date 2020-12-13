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
    if num > 1 and not num in deviders:
        isPrime = True
        for i in deviders:
            if num % i == 0:
                isPrime = False
                break
        if isPrime:
            return num
    elif num in deviders:
        return num

# возвращает список отфильтрованных чисел
@showSpendedTime
def evenOddPrime(*args, **kwargs):
    result = []
    if kwargs['numType'] == 'even':
        result = list(filter(lambda x: not x%2, args))        
    elif kwargs['numType'] == 'odd':
        result = list(filter(lambda x: x%2, args))
    elif kwargs['numType'] == 'prime':
        result = list(filter(getPrime, args))
    return result
