#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pow
from datetime import datetime


#  --- ЗАДАНИЕ 1 ---

def time(func):
    def wrapper(*args, **kwargs):
        start = datetime.timestamp(datetime.now())
        res = func(*args, **kwargs)
        finish = datetime.timestamp(datetime.now()) - start
        print(finish)
        return res
    return wrapper

# возвращает список переданных чиел в квадрат
@time
def powList(*args, pwr = 2):
    poweredList = [] 
    for i in args:
        poweredList.append(pow(i,pwr))
    return poweredList

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
@time
def evenOddPrime(*args, **kwargs):
    result = []
    if kwargs['numType'] == 'even':
        result = list(filter(lambda x: not x%2, args))        
    elif kwargs['numType'] == 'odd':
        result = list(filter(lambda x: x%2, args))
    elif kwargs['numType'] == 'prime':
        result = list(filter(getPrime, args))
    return result
