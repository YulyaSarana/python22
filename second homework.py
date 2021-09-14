# second homework
# 1.
animal = 'cat'
index = '1'
# 2. Создать 4 переменных типа Integer с разными значениями
x1 = 3
x2 = 15000
x3 = 50
x4 = 789
# 3. Создать 3 переменных типа Float с разными значениями
y1 = 3.1415926535
y2 = 1.5
y3 = 255.5
# 4. Реализовать 15 варианта сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
b_t = True
b_f = False
print(x1 >= x2)
print(x1 <= x2)
print(x1 != x2)
print(x2 >= x4)
print(x4 >= x3)
print(x2 != x4)
print(x4 >= x4)
print(x2 > x1)
print(x1 >= x3)
print(x3 < x4)
print(x3 != x4)
print(x3 >= x2)
print(x1 < x4)
print(x4 < x2)
print(x1 >= x4)
# 5. Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
print(y1 >= y2)
print(y1 <= y2)
print(y1 != y3)
print(y2 >= y1)
print(y3 >= y3)
print(y2 != y3)
print(y2 >= y1)
print(y3 > y2)
print(y1 >= y3)
# 6. Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not). Pезультаты весвести в консоль.
height = 38
length = 23
width = 28
result_1 = height == 38 and length == 23
print(result_1)
result_2 = not height < 39
print(result_2)
result_3 = height < 50 or width == 28
print(result_3)
result_4 = height < 50 and width > 28
print(result_4)
result_5 = height == 38 or width < 28
print(result_5)
result_6 = length == 38 or height <= 28
print(result_6)
result_7 = width >= 1 or height <= 10
print(result_7)
result_8 = not length < 40
print(result_8)
result_9 = not width >= 28
print(result_9)
result_10 = height == 38 and width == 27
print(result_10)
# 7. Сделать скрипт используя функцию input()
rooms = int(input('Вы ввели число = '))
if rooms == 30:
    print('которое равно 30')
elif rooms < 30:
    print('которое меньше 30')
elif rooms > 30:
    print('которое больше 30')
else:
    print('вы ввели не число')
# 8. Сделать скрипт используя функцию input()
import random
X = random.randint(0, 100)
volume = int(input('Вы ввели число = '))
if volume == X:
    print('которое равно сгенерированному числу')
elif volume > X:
    print('которое больше сгенерированного числа')
elif volume < X:
    print('которое меньше сгенерированного числа')
else:
    print('вы ввели не число')
# 9. Сделать скрипт используя функцию input()
import random
xx = random.randint(0, 100)
yy = random.randint(0, 100)
xy = int(input('Вы ввели число = '))
if xx == xy == yy:
    print('которое равно и равно сгенерированному числу')
elif xx == xy > yy:
    print('которое равно и больше сгенерированного числа')
elif xx == xy < yy:
    print('которое равно и меньше сгенерированного числа')
elif xx > xy == yy:
    print('которое меньше и равно сгенерированного числа')
elif xx > xy > yy:
    print('которое меньше и больше сгенерированного числа')
elif xx > xy < yy:
    print('которое меньше и меньше сгенерированного числа')
elif xx < xy == yy:
    print('которое больше и равно сгенерированному числу')
elif xx < xy > yy:
    print('которое больше и больше сгенерированного числа')
elif xx < xy < yy:
    print('которое больше и меньше сгенерированного числа')
else:
    print('Вы ввели не число')



