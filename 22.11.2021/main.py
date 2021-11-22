import math
import numpy as np
import numpy.random as rand
def x_1(): # вектор с элементами от 12 до 42
    return np.arange(12, 43)
def x_2(): # вектор, заполненный 0, кроме 5 элемента
    return np.array([3 if i == 5 else 0 for i in range(12)])
def x_3(): # матрица 3 на 3, заполненная числами от 0 до 8
    return np.array([i for i in range(9)]).reshape(3, 3)
def x_4(): # все положительные элементы матрицы
    return np.array([ i for i in np.array([1,2,0,0,4,0]) if i > 0 ]) # все положительные элементы матрицы
    # x_4 = np.array( [i for i in [1, 2, 0 , 0, 4, 0] if i > 0])
def x_5(): # перемножение матриц
    array_1 = np.arange(15).reshape(5, 3)
    array_2 = np.arange(1, 12, 2).reshape(3, 2)
    return np.dot(array_1, array_2)
def x_6():  # матрица, внутри заполненная 1, а снаружи 0
    x_6 = np.zeros((10,10))
    x_6[1:-1,1:-1] = 1
    return  x_6
def x_7():# случайный отсортированный вектор
    return sorted(np.random.randint(1, 9, 10))# случайный отсортированный вектор
def x_8(): # просто ответ на вопрос
    x_8 = np.arange(9).reshape(3, 3)
    for index, value in np.ndenumerate(x_8):
        print(index, value)
    for index in np.ndindex(x_8.shape):
        print(index, x_8[index])
    return 0
def x_9(): # нормализация вектора
    x_9 = np.random.randint(1, 9, 10) # случайный вектор(лучше с начала создать случайный массив)
    suma = math.sqrt(sum(i**2 for i in x_9))
    x_9 = np.array([i/suma for i in x_9]) # нормализация
    return x_9
def x_10():
    x = float(input())
    x_10 = np.random.randint(-10, 9, 10)
    z = min([abs(i - x) for i in x_10]) # 32  (8, 56)  24 -> 8
    print(x_10)
    if z + x in x_10: # [8, 56] x = 32 -> выводит 56
        return z + x
    else:
        return x - z
