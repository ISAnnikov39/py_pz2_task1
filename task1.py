# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input( 'введите количество монеток '))

import random
list_num = [random.randint(0,1) for i in range(n)] # рандомно распределил монетки, лежащие стороной вверх решкой и гербом

tails = 0
emblems = 0

for i in range(n):
    if list_num[i] == 0:
        tails += 1
    else: 
        emblems += 1

print (f'решкой вверх: {tails} , гербом вверх {emblems}')
if tails > emblems:
    print (f'количество лежащих монет гербом вверх, которые необходимо перевернуть: {emblems} ')
elif tails < emblems:
    print (f'оличество лежащих монет решкой вверх, которые необходимо перевернуть: {tails} ')
else:
    print ('количество монет лежащих гербом и решкой вверх одинакого')