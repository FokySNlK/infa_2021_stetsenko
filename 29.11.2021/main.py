import random
import math

import numpy
import numpy as np
import matplotlib.pyplot as plt

def four_histograms():
    N = [100, 1000, 10000, 100000]
    mu, sigma = 0, 1
    #subplot 1

    sp = plt.subplot(221)
    x = mu + sigma * np.random.randn(N[0])
    n, bins, patches = plt.hist(x, facecolor='g')
    plt.grid(True)

    # subplot 2
    sp = plt.subplot(222)
    x = mu + sigma * np.random.randn(N[1])
    n, bins, patches = plt.hist(x, facecolor='r')
    plt.grid(True)

    # subplot 3
    sp = plt.subplot(223)
    x = mu + sigma * np.random.randn(N[2])
    n, bins, patches = plt.hist(x, facecolor='b')
    plt.grid(True)

    # subplot 4
    sp = plt.subplot(224)
    x = mu + sigma * np.random.randn(N[3])
    n, bins, patches = plt.hist(x)
    plt.grid(True)
    plt.show()

def solve_ex_2():
    x = np.arange(-10, 20, 0.01)
    plt.plot(x, x*x - x - 6)
    plt.grid(True, linewidth = 1)
    plt.minorticks_on()
    plt.grid(which='minor',
            color='k',
            linestyle=':')
    plt.show()
def solve_ex_3():
    x = np.arange(-10, 20, 0.01)
    y = []
    for i in x:
        z = np.log((i**2 + 1)*math.exp(-abs(i)/10))/np.log(1 + math.tan(1/(1 + (math.sin(i))**2)))
        y.append(z)
    plt.plot(x, y)
    plt.grid(True, linewidth=1)
    plt.minorticks_on()
    plt.grid(which='minor',
             color='k',
             linestyle=':')
    plt.show()

def solve_ex_4_alternative():
    x = list(map(int, input().split()))
    plt.figure(num = 1, figsize=(6, 6))
    plt.title('Plot 3', size=14)
    plt.pie(x)
    z = list(map(str, input().split()))
    with plt.xkcd(length=100, randomness=30):
        plt.pie(x, labels=(z))
        plt.title('Не знаю что, не знаю где!')
    plt.show()
def solve_ex_4():
    eq = input()
    x = np.arange(-20, 20, 0.01)
    plt.plot(x, eval(eq))
    plt.grid(True, linewidth = 1)
    plt.minorticks_on()
    plt.grid(which='minor',color='k',linestyle=':')
    plt.show()
def solve_ex_5():
    polynom = list(map(int, input().split()))
    n = len(polynom)
    polynom = np.poly1d(polynom)
    x = np.arange(-100, 100, 0.01)
    y = np.array([polynom(i) for i in x])
    x_x, y_y = np.polyfit(x, y, deg = n - 1, cov=True)
    plt.plot(x_x, y_y)
    plt.show()
solve_ex_5()