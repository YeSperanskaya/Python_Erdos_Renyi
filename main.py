"""
С использованием библиотеки NetworkX требуется написать скрипт для генерации графа в модели Эрдёша-Реньи
с заданными характеристиками. Преподавателем будут даны значения количества вершин и вероятность появления
случайного ребра. Требуется вычислить в программе среднюю степень вершины и сравнить её со значением средней
степени вершины, полученной по формуле из материала лекций.
"""
#7 баз данных за семь денеь, докуменьтация

import networkx as nx #импорт бибиолиотеки networkx

# функция, которая рассчитывает среднюю степень вершины
def ren_graph(n, p): # создание функции
    G = nx.erdos_renyi_graph(n, p)
    a = 0
    for n in G.nodes():
        a = a + G.degree(n)
    return (float(a) / len(G.nodes())) # функция возвращает результат расчета средней степени вершины по заданным данным

def generate_graph(n, p):
    G = nx.erdos_renyi_graph(n,p)
    print("Граф выглядит следующим образом: ")
    for n in G.nodes():
        print(G.degree(n), end="")
    print()


# подаются индивидуальные данные
n = 11
p = 0.35
print(f"Индивидуальные данные {n}, {p}:")
res_python = ren_graph(n,p) #рассчитывает среднюю степень вершины по индивидуальному заданию
print(res_python) # печать результата рассчета средней степени вершины
generate_graph(n,p)

# средняя степень вершины по формуле
calc_avr = (n-1)*p

# разница значений
res = calc_avr - res_python
print("Средняя степень вершины фактическая: ", round(res_python, 4))
print("Средняя степень вершины по формуле: ", round(calc_avr, 4))
print("Полученная разница значений: ", round(abs(res), 4))


