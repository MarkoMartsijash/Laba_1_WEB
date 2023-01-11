import numpy as np
import sys


def Neyro_Volodya():
    #Функція, що оприділяє ваги.
    def sigmoid(x, der=False):
        if der == True:
            return x * (1-x)
        return 1 / (1 + np.exp(-x))

    def YOU_DATA():
        your_data = np.array([0,0,0])
        your_data[0] = int(input("Вкажи (1 або 0): "))
        your_data[1] = int(input("Вкажи (1 або 0): "))
        your_data[2] = int(input("Вкажи (1 або 0): "))

        print("Гаразд, тепер я спробую зрозуміти, чи схоже це на правду...\n ")

        error = 0

        if your_data[0] == 0 or your_data[0] == 1:
            if your_data[1] == 0 or your_data[1] == 1:
                if your_data[2] == 0 or your_data[2] == 1:
                    print(your_data)
                    return your_data
                else:
                    error += 1
            else:
                error += 1
        else:
            error += 1

        if error > 0:
            print("Ми ще в школі такого не вчили.\n Вкажи 1 або 0.")

    def INPUT(DATA):
        new_x = DATA
        reply = ''

        l1_new = sigmoid(np.dot(new_x, syn0))
        if l1_new[0] < 0.6:
            l1_new[0] = 0
            reply = "ОБМАН"
        else:
            l1_new[0] = 1
            reply = "ПРАВДА"

        print("На основі цих даних:", new_x, "Я думаю, що це", reply, sep=" ", end="\n\n")

    #Вхідні дані
    a = np.array([[1,0,1], [1,0,1], [0,1,0], [0,1,0]])
    b = np.array([[0,1,0], [0,0,1], [1,0,0], [1,0,1], [1,1,0], [0,1,1]])
    c = np.array([[0,0,0], [1,1,0], [1,0,0], [1,1,1]])
    x = b

    #Вихідні дані
    a2 = np.array([[1,1,0,0]]).T
    b2 = np.array([[0,0,0,1,1,1]]).T
    c2 = np.array([[0,1,0,1]]).T
    y = b2

    #Випадкові числа стають більш конкретні
    np.random.seed(1)

    #Ініціалізація вагів випадковим чином з середнім 0
    syn0 = 2 * np.random.random((3, 1))-1

    l1 = []

    for inter in range(100000):
        l0 = x
        l1 = sigmoid(np.dot(l0, syn0))
        l1_error = y - l1
        l1_delta = l1_error * sigmoid(l1, True)
        syn0 += np.dot(l0.T, l1_delta)

    # print("Вихідні дані після тренування:")
    # print(l1)

    INPUT(YOU_DATA())

def Gypotez_Kolatz():
    print("Гіпотеза Колатца")

    n = int(input("Enter your number: "))
    res_arr = []

    while True:
        if type(n) != int:
            break
        if n <= 0:
            break

        res_arr.append(n)

        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int (n * 3 + 1)
        if n == 1:
            res_arr.append(n)
            break
        
    print(res_arr)

def DEYKSTRA():
    class Graph(object):
        def __init__(self, nodes, init_graph):
            self.nodes = nodes
            self.graph = self.construct_graph(nodes, init_graph)
            
        def construct_graph(self, nodes, init_graph):
            
            graph = {}
            for node in nodes:
                graph[node] = {}
            
            graph.update(init_graph)
            
            for node, edges in graph.items():
                for adjacent_node, value in edges.items():
                    if graph[adjacent_node].get(node, False) == False:
                        graph[adjacent_node][node] = value
                        
            return graph
        
        def get_nodes(self):
            
            return self.nodes
        
        def get_outgoing_edges(self, node):
            
            connections = []
            for out_node in self.nodes:
                if self.graph[node].get(out_node, False) != False:
                    connections.append(out_node)
            return connections
        
        def value(self, node1, node2):
            
            return self.graph[node1][node2]
    def dijkstra_algorithm(graph, start_node):
        unvisited_nodes = list(graph.get_nodes())
    
        shortest_path = {}
    
        previous_nodes = {}
    
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[start_node] = 0
        
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes: 
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
                    
            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node
    
            unvisited_nodes.remove(current_min_node)
        
        return previous_nodes, shortest_path
    def print_result(previous_nodes, shortest_path, start_node, target_node):
        path = []
        node = target_node
        
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]
    
    
        path.append(start_node)
        
        print("Найкращий маршрут з вагою: {}.".format(shortest_path[target_node]))
        print(" -> ".join(reversed(path)))
    nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
    
    init_graph = {}
    for node in nodes:
        init_graph[node] = {}
        
    init_graph["Reykjavik"]["Oslo"] = 5
    init_graph["Reykjavik"]["London"] = 4
    init_graph["Oslo"]["Berlin"] = 1
    init_graph["Oslo"]["Moscow"] = 3
    init_graph["Moscow"]["Belgrade"] = 5
    init_graph["Moscow"]["Athens"] = 4
    init_graph["Athens"]["Belgrade"] = 1
    init_graph["Rome"]["Berlin"] = 2
    init_graph["Rome"]["Athens"] = 2
    graph = Graph(nodes, init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Reykjavik")
    print_result(previous_nodes, shortest_path, start_node="Reykjavik", target_node="Belgrade")

def MAIN():
    restart = 1

    while restart == 1:
        print()
        print()
        print()
        restart = int(input("1 - Запустити\n2 - Вийти\n: "))
        if restart == 1 or restart == 2:
            if restart == 2:
                break
        else:
            print("Невідома команда")
            break
        print()
        print()
        print()
        print("Привіт. Я Володя ;)\nЯ вмію деякі речі, хочеш щось покажу?")
        print()
        print("Оберіть можливість:")
        print("1 - Володя застосує нейронну мережу, і перевірить чи ваша числова послідовність відповідає правді.")
        print("2 - Володя перевірить, чи справедлива гіпотеза Колатца для вашого числа.")
        print("3 - Володя спробує знайти найкоротший шлях між вершинами графа (алгоритм Дейкстри).")
        print("4 - Інформація про програму.")
        print("5 - Вийти з програми.")
        

        inter_btn = int(input("Що показати: "))

        if inter_btn == 1 or inter_btn == 2 or inter_btn == 3 or inter_btn == 4 or inter_btn == 5:
            if inter_btn == 1:
                Neyro_Volodya()
            elif inter_btn == 2:
                Gypotez_Kolatz()
            elif inter_btn == 3:
                DEYKSTRA()
            elif inter_btn == 4:
                print()
                print()
                print()
                print("Режим '1' - відповідає за запуск нейронної мережі.")
                print("          Користувач задає послідовність з 0 чи 1 (наразі послідовність лише в три числа).")
                print("          Далі Володя оцінюючи її, вирішує чи вона істинна чи оманлива.")
                print("          Діло в тому, що Володю навчили відносити послідовність з більшою кількістю одиниць до ПРАВДИ,")
                print("          а з більшою кількістю нулів до ОБМАНУ. На даному етапі можливості Володі примітивні,")
                print("          але якщо, під час навчання, йому показати послідовності чисел, скажімо з параметрами")
                print("          автомобілів, а замість слів 'ПРАВДА' і 'ОБМАН' марки чи моделі реальних авто,")
                print("          трішки удосконалити код і провести навчання. Володя зможе розпізнавати різні автомобілі.")
                print("          P.S. Але Володя лише в 1-му класі) Тому і так не погано ;) ")
                print()
                print()
                print()
                print("Режим '2' - гіпотеза Колатца.")
                print("          Ця гіпотеза говорить - починаючи, з будь-якої цифри і в подальшому видозмінюючи його")
                print("          за допомогою формул (n*3+1 - для непарних чисел і n/2 - для парних) створюється послідовність чисел")
                print("          і ця послідовність сходиться до циклу [4,2,1]. Візьмімо наприклад число 3:")
                print("          воно не парне, тому використовуємо першу формулу, отримуємо 10, воно парне, використовуючи вже")
                print("          другу формулу, отримуємо 5, далі 16, 8, 4, 2, 1. Ось, ми прийшли до циклу в 4,2,1")
                print("          одиниця не парна, тому з неї отримуємо 4, а з 4-рки знову 2, потім знову один і так  далі.")
                print("          Довести цю гіпотезу неможливо, так як цифр безкінечно, проте Володя зможе перевірити")
                print("          деякі числа за вашим бажаням, щоб ви переконалися, що гіпотеза справедлива хоча б для них.")
                print()
                print()
                print()
                print("Режим '3' - алгоритм Дейкстри.")
                print("          Алгоритм Дейкстри - це популярний алгоритм пошуку, який використовується для визначення")
                print("          найкоротшого шляху між двома вузлами у графі. У вихідному сценарії граф представляв")
                print("          Нідерланди, вузли графа представляли різні голландські міста, а ребра представляли дороги")
                print("          між містами. Алгоритм Дейкстри можна використовувати для вирішення будь-якого завдання,")
                print("          яке може бути представлене у вигляді графа . Пропозиції друзів у соціальних мережах, ")
                print("          маршрутизація пакетів через Інтернет або пошук шляхів через лабіринт — це можна зробити")
                print("          алгоритмом Дейкстри. Володя вміє шукати шлях лише строго заданого графа.")
                print("          Тому вам він, нажаль, не допоможе :(")
                print()
                print()
                print()
            elif inter_btn == 5:
                break
        else:
            print("Невідома команда")
            break
        
MAIN()