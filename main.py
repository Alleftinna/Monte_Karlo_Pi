import time
import random


def calculate_Pi():
    number_point = int(input('Введите количество точек: '))
    squre_side = int(input('Введите сторону квадрата: '))
    start = time.time()
    i = 0
    x_coordinate = 0
    y_coordinate = 0
    n_within = 0
    for i in range( number_point):
        x_coordinate = random.randint(0, squre_side)  # Рандомный Х с 3 знаками после запятой
        y_coordinate = random.randint(0, squre_side)  # Рандомный Y с 3 знаками после запятой
        if pow(x_coordinate, 2) + pow(y_coordinate, 2) <= squre_side ** 2:  # Условие принадлежности точки к кругу
            n_within += 1
        i += 1

    Pi = n_within / number_point * 4
    print('Число Пи: ',Pi)
    end = time.time() - start
    print("Время работы: ", end)
    input("123")
if __name__ == "__main__":
    calculate_Pi()