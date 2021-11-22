import numpy as np
import numpy.random as rand

x_1 = np.arange(12, 43) # вектор с элементами от 12 до 42
x_2 = np.array([3 if i == 5 else 0 for i in range(12)]) # вектор, заполненный 0, кроме 5 элемента
x_3 = np.array([i for i in range(9)]).reshape(3, 3) # матрица 3 на 3, заполненная числами от 0 до 8
x_4 = np.array([ i for i in np.array([1,2,0,0,4,0]) if i > 0 ]) # все положительные элементы матрицы
# x_4 = np.array( [i for i in [1, 2, 0 , 0, 4, 0] if i > 0])
array_1 = np.arange(15).reshape(5, 3)
array_2 = np.arange(1, 12, 2).reshape(3, 2)
x_5 = np.dot(array_1, array_2) # перемножение матриц
x_6 = np.zeros((10,10))
x_6[1:-1,1:-1] = 1 # матрица, внутри заполненная 1, а снаружи 0
x_7 = sorted(np.random.randint(1, 9, 10)) # случайный отсортированный вектор
x_8 = np.arange(9).reshape(3,3) # for index, value in nd.ndenumerate(x_8)
#########################
#########################
