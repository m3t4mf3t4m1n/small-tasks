''' 
Задача:
написать функцию, которая принимает число и возвращает 1 если хотя бы одна перестановка цифр этого числа (в т.ч. оригинал)
является простым числом, иначе 0.
'''

from itertools import permutations

def primeCheck(num):
    l = list(permutations((map(int, str(num))))) #получаем список со всеми возможными перестановками

    for i in l: #проверяем каждую перестановку на простое число, если хоть одно простое - выводим 1

        number_frm_tupple = int(''.join(map(str, i))) #конвертим тапл в число
        d = 2

        while number_frm_tupple % d != 0: 
            d += 1
        if d == number_frm_tupple:
            return print(1)
    return print(0)

primeCheck(68)