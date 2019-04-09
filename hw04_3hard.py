print('{:*^30s}'.format('Задание-1:'))
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
          
# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

[print(line) for line in list(map(list, zip(*matrix)))]

print('{:*^30s}'.format('Задание-2:'))
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

import re

number1 = (re.findall(r'\d', number))

sum0 = k = 0
for i in range(len(number1)-4):
    sum = int(number1[i]) * int(number1[i + 1]) * int(number1[i + 2]) * int(number1[i + 3]) * int(number1[i + 4])
    if sum >= sum0:
        sum0 = sum
        k = i
    else:
        pass
print('наибольшее произведение пяти последовательных цифр = ', sum0, '\nиндекс смещения первого числа последовательных 5-ти цифр =', k)

print('{:*^30s}'.format('Задание-3:'))
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

import random
matrix = []
#Рандомим 8мь ферзей:
for i in range(8):
    lst_i = [random.randint(1,8) for _ in range(2)]
    matrix.append(lst_i)
for line in matrix:
    print('ферзь:', line)
# Выполняем поворот (транспонирование) матрицы
matrix = list(map(list, zip(*matrix)))
#Функция вычисления произведения всех X(0) or Y(1)
def multiplic(a):
    mult = 1
    for x in matrix[a]:
        mult *= x
    return mult
#ферзи не бьют друг друга только в двух случаях,
#при которых соблюдается лишь одно условие - все Y и X координаты должны быть разные.
#т.е можно вычислить произведение всех X, Y координат и сравнить с 8!
#8! = 40320
if multiplic(0) == multiplic(1) == 40320:
    print('NO - не бьют')
else:
    print('YES - под ударом')