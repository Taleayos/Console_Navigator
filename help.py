import random
import numpy as np

from graph import *

def check_valid_matrix(matrix: np.matrix):
    return len([num for row in matrix for num in row if num == 0]) == len(matrix)

class Ant:

    def __init__(self, start_position, alfa, betta):
        self.start_position = start_position
        self.path = []
        self.path_length = 0
        self.ALFA = alfa
        self.BETTA = betta

    def make_step(self, weight_graph: np.matrix, ferromon_graph: np.matrix, position: int):
        s = len(weight_graph)
        variants = [i for i in range(s) if weight_graph[position][i] > 0 and i not in self.path]
        if len(variants) == 0:
            variants = [self.start_position]
        wish_sum = sum([(ferromon_graph[position][i] ** self.ALFA) * (weight_graph[position][i] ** self.BETTA) for i in variants])
        wish_list = [((ferromon_graph[position][i] ** self.ALFA) * (weight_graph[position][i] ** self.BETTA)) / wish_sum for i in variants]
        rand_num = round(random.random(), 2)
        chose = -1
        interval = 0
        for i in range(len(wish_list) - 1):
            if interval <= rand_num < interval + wish_list[i + 1]:
                chose = variants[i]
                break
            interval += wish_list[i]
        else:
            chose = variants[len(wish_list) - 1]
        self.path.append(chose)
        self.path_length += weight_graph[position][chose]
        return chose

    def make_path(self, weight_graph: np.matrix, ferromon_graph: np.matrix):
        position = self.start_position
        self.path.append(position)
        pos = -1
        while self.start_position != pos:
            position = self.make_step(weight_graph, ferromon_graph, position)
            pos = position

        return self.path_length



if __name__ == "__main__":
    a1 = Ant(0,1, 1)
    x = s21_graph()
    filename = "graph0.txt"
    x.LoadGraphFromFile(filename)
    f_matrix = np.array([[0.1 for _ in range(x.get_graph_size())]
                         for _ in range(x.get_graph_size())])

    a1.make_path(x.get_graph_matrix(), f_matrix)
    for i in a1.path:
        print(i + 1, end=' ')
    print(a1.path_length)





