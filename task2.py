#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. 
#Для проверки своего кода используйте модуль fractions.

import fractions

a = str(input('Введите дробь N1 : '))
b = str(input('Введите дробь N2 : '))
first = a.split('/')
second = b.split('/')
sum = str(int(first[0]) * int(second[1]) + int(first[1]) * int(second[0])) + '/' + str(int(second[1]) * int(first[1]))
mult = str( int(first[0]) * int( second[0])) + '/' + str ( int(first[1]) * int(second[1]))
print(f'сумма {sum}, произведение {mult}')
f1 = fractions.Fraction(int(first[0]), int(first[1]))
f2 = fractions.Fraction(int(second[0]), int(second[1]))
print(f'сумма дробей {f1+f2}, произведение дробей {f1*f2}')

# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def integer_to_hex(num: int, base=16):
    hex_chars = '0123456789abcdef'
    result_str = ''
    while num > 0:
        result_str = hex_chars[num % base] + result_str
        num //= base
    return result_str


num = 111
print(integer_to_hex(num))
print(hex(num))