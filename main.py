import math
from multiprocessing import Pool
from matplotlib import pyplot as plt
from random import uniform
width = 10000
heigth = width
radio = width

npuntos = 0
ndentro = 0
radio2 = radio*radio
replicas = 60
promediopi = []
change_prom = []


def calc_pi(i):
    global npuntos 
    global ndentro

    for i in range(1000000):
        x = uniform(0, width)
        y = uniform(0, width)
        npuntos += 1
        if x*x + y*y <= radio2:
            ndentro += 1
    pi = ndentro * 4 / npuntos
    return pi


if __name__ == '__main__':

    with Pool(4) as p:
        results = p.map(calc_pi, [i for i in range(replicas)])
        print(results)
    # Calculo de promedio acumulativo
    avg = [results[0]]
    for i in range(1,len(results)):
        avg.append((avg[-1]*len(avg)+results[i])/(len(avg)+1))

    # Grafica
    
    plt.plot([i for i in range(len(avg))],avg)
    plt.plot([i for i in range(len(avg))],[math.pi for i in range(len(avg))])
    plt.title("Valor de pi por Método de Montecarlo")
    plt.xlabel("Iteraciones")
    plt.ylabel("Pi")
    plt.show()
