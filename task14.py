#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('введите число n больше 1: '))

def degree (n):
    if n<2:
        n = int(input('введите число n больше 1: '))
        degree (n)
    else:
        for i in range(1, n+1):
            if 2**i <= n:
                print (2**i)

degree(n)
