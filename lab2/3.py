from math import sqrt
a = float(input('1 число = '))
b = float(input('2 число = '))
c = float(input('3 число = '))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + sqrt(d))/2
    x2 = (-b - sqrt(d))/2
    print ('x1 = ', x1 ,'x2 = ', x2)
elif d == 0:
    x = -b / (2 * a)
    print ('x = ', x)
else:
    print ('корней нет')
