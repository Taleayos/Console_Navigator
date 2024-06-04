from graph import *
import math
from help import *
from stack import *

class s21_graph_algorithms():
    def GetShortestPathBetweenVertices(self, new_graph: s21_graph, vertex1: int, vertex2: int):
        try:
            visited_vertex = [False] * new_graph.get_graph_size()
            inf = math.inf
            weight = [inf] * new_graph.get_graph_size() # так как вес достижения конечной вершины неизвестен, считаем что он бесконечен
            weight[vertex1 -1] = 0

            def go_vertex(): # проверяет какие вершины еще не посещены с наименьшим весом
                vertex = 0
                weight_min = inf
                for i in range(new_graph.get_graph_size()):
                    if weight[i] < weight_min and visited_vertex[i] == False:
                        weight_min = weight[i]
                        vertex = i

                return vertex

            while False in visited_vertex:
                i = go_vertex()
                for j in range(new_graph.get_graph_size()):
                    if new_graph.get_graph_matrix()[i][j] != 0 and (not visited_vertex[j]):
                        weight[j] = min(weight[j], weight[i] + new_graph.get_graph_matrix()[i][j]) #проверяем что меньше, то что там лежит или то как мы туда пришли
                visited_vertex[i] = True

            return weight[vertex2-1]

        except Exception as exp:
            print(exp)

    def GetShortestPathsBetweenAllVertices(self, new_graph: s21_graph):
        try:
            res_matrix = new_graph.get_graph_matrix().copy()
            for i in range(new_graph.get_graph_size()):
                for j in range(new_graph.get_graph_size()):
                    res_matrix[i][j] = self.GetShortestPathBetweenVertices(new_graph, j + 1, i + 1)
            return res_matrix
        except Exception as exp:
            print(exp)


    def BreadthFirstSearch(self, graph: s21_graph, start_vertex: int):
        res = s21_stack()
        res.append(start_vertex)
        tmp_matrix = graph.get_graph_matrix().copy()
        vertexes_stack = s21_stack()
        vertexes_stack.append(start_vertex - 1)
        tmp_stack = s21_stack()
        while np.unique(tmp_matrix).size > 1:
            for i in vertexes_stack.get_list():
                for j in range(graph.get_graph_size()):
                    if tmp_matrix[i][j] > 0 and j + 1 not in res.get_list():
                        res.append(j + 1)
                        tmp_stack.append(j)
                        tmp_matrix[i][j] = 0
                    else:
                        tmp_matrix[i][j] = 0
            vertexes_stack.copy(tmp_stack.get_list())
            tmp_stack.clear()

        return res.get_list()

    def DepthFirstSearch(self, graph: s21_graph, start_vertex: int):
        tmp_matrix = graph.get_graph_matrix().copy()
        res = s21_stack()
        res.append(start_vertex)
        tmp_stack = s21_stack()
        while np.unique(tmp_matrix).size > 1:
            for j in range(graph.get_graph_size() -1, -1, -1):
                if tmp_matrix[start_vertex - 1][j] > 0:
                    tmp_stack.append(j)
                    tmp_matrix[start_vertex - 1][j] = 0
            start_vertex = tmp_stack.pop() + 1
            if start_vertex not in res.get_list():
                res.append(start_vertex)

        return res.get_list()

    def GetLeastSpanningTree(self, graph: s21_graph):
        arr = np.zeros((graph.get_graph_size(), graph.get_graph_size()), dtype=int)
        start = 0
        v = {start}
        u = set([i for i in range(graph.get_graph_size()) if i != start])
        while u:
            a = {(i, j, graph.get_graph_matrix()[i][j]) for i in u for j in v}
            if a == {}:
                arr = None
                break
            (i, j, w) = min(a, key=lambda t: t[2])
            arr[i][j] = arr[j][i] = w
            v.add(i)
            u.remove(i)

        return arr

    def SolveTravelingSalesmanProblem(self, graph: s21_graph, count: int=16000):
        if check_valid_matrix(graph.get_graph_matrix()):
            alfa = 1
            betta = 4
            evaporation = 0.6
            q = 40
            # count = 16000  # amount of starts
            ferromon_matrix = np.array([[0.1 for _ in range(graph.get_graph_size())]
                                        for _ in range(graph.get_graph_size())])
            min_path_length = float('inf')
            min_path = []
            for _ in range(count):
                ferromon_matrix *= evaporation
                for _ in range(len(ferromon_matrix)):  # amount of ants
                    start_position = random.randint(0, graph.get_graph_size() - 1)
                    ant = Ant(start_position, alfa, betta)
                    tmp_length = ant.make_path(graph.get_graph_matrix(), ferromon_matrix)
                    if min_path_length > tmp_length:
                        min_path_length = tmp_length
                        min_path = ant.path
                    for i in range(len(ant.path) - 1):
                        ferromon_matrix[ant.path[i]][ant.path[i + 1]] += q / ant.path_length
            min_path = [i + 1 for i in min_path]
            return self.make_answer(min_path), min_path_length
        else:
            raise Exception('Invalid graph!')

    def make_answer(self, path: list):
        pos = path.index(1)
        return path[pos:-1] + path[:pos] + [1]

    def Nearest_neighbor_method(self, new_graph: s21_graph):
        try:
            visited_vertex = [False] * new_graph.get_graph_size()
            inf = math.inf
            weight = [inf] * new_graph.get_graph_size()
            weight[0] = 0
            new_list_vert = []
            result = 0
            def go_vertex():
                vertex = 0
                weight_min = inf
                for i in range(new_graph.get_graph_size()):
                    if weight[i] < weight_min and visited_vertex[i] == False:
                        weight_min = weight[i]
                        vertex = i
                return vertex

            while False in visited_vertex:
                i = go_vertex()
                new_list_vert.append(i)
                for j in range(new_graph.get_graph_size()):
                    if new_graph.get_graph_matrix()[i][j] != 0 and (not visited_vertex[j]):
                        weight[j] = new_graph.get_graph_matrix()[i][j]
                visited_vertex[i] = True

            new_list_vert.append(0)

            for ind, k in enumerate(new_list_vert):
                result += new_graph.get_graph_matrix()[k][new_list_vert[ind+1 if (ind+1) < len(new_list_vert) else 0]]
            reslist = [i + 1 for i in new_list_vert]

            return reslist, result

        except Exception as exp:
            print(exp)

    def STSP_one_step_algo(self, graph: s21_graph, count: int = 1000):
        l = graph.get_graph_size()
        min_path = []
        min_length = float('inf')
        for _ in range(count):
            path = []
            while len(path) < l:
                number = random.randint(0, l - 1)
                if number not in path:
                    path.append(number)

            length = 0
            for idx, i in enumerate(path):
                stop = path[len(path) - 1]
                length += graph.get_graph_matrix()[i][path[idx + 1] if i != stop else path[0]]
            path.append(path[0])
            if min_length > length:
                min_length = length
                min_path = path
        return [i + 1 for i in min_path], min_length

if __name__ == "__main__":
    x = s21_graph()
    # filename = "graph0.txt"
    filename = "graph1.txt"
    x.LoadGraphFromFile(filename)
    z = s21_graph_algorithms()
    res = z.GetShortestPathBetweenVertices(x, 4, 11)
    print(res)
    # res2 = z.GetShortestPathsBetweenAllVertices(x)






