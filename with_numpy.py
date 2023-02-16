import time
import random
import numpy as np

def calculate_Pi():
    np.random.seed(0)
    number_point = int(input('Введите количество точек: '))
    squre_side = int(input('Введите сторону квадрата: '))
    start = time.time()
    i = 0
    x_coordinate = 0
    y_coordinate = 0
    n_within = 0
    x_coordinates = np.random.randint(0, squre_side, size=number_point)  # Рандомный Х с 3 знаками после запятой
    y_coordinates = np.random.randint(0, squre_side, size=number_point)  # Рандомный Y с 3 знаками после запятой
    x_coordinates = np.square(x_coordinates)
    y_coordinates = np.square(y_coordinates)
    squre_side_sq = np.square(squre_side)
    result = np.add(x_coordinates, y_coordinates)
    print(len(result))
    for i in result:
        if i<squre_side_sq:  # Условие принадлежности точки к кругу
            n_within += 1
        i += 1

    Pi = n_within / number_point * 4
    print('Число Пи: ',Pi)
    end = time.time() - start
    print("Время работы: ", end)
    input("123")

if __name__ == "__main__":
    calculate_Pi()