# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
#  между ними в 2D пространстве. 
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/

# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099

from math import sqrt
Ax = int(input('Введите координату Х точки А : '))
Ay = int(input('Введите координату Y точки A : '))
Bx = int(input('Введите координату Х точки B : '))
By = int(input('Введите координату Y точки B : '))
distance = sqrt(((Ax-Bx)**2)+((Ay-By)**2))
print(round(distance, 3))
