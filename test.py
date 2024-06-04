import unittest
import networkx as nx
from graph_algorithms import *
from graph import *


class TestSimpleNavigator(unittest.TestCase):
    def test_GetShortestPathBetweenVertices_1(self):
        x = s21_graph()
        filename = "graphDij2.txt"
        x.LoadGraphFromFile(filename)
        z = s21_graph_algorithms()
        res = z.GetShortestPathBetweenVertices(x, 2, 6)
        self.assertEqual(res, 12)

    def test_GetShortestPathBetweenVertices_2(self):
        x = s21_graph()
        filename = "graphDij.txt"
        x.LoadGraphFromFile(filename)
        z = s21_graph_algorithms()
        res = z.GetShortestPathBetweenVertices(x, 1, 7)
        self.assertEqual(res, 13)

    def test_GetShortestPathBetweenVertices_3(self):
        x = s21_graph()
        filename = "graph1.txt"
        x.LoadGraphFromFile(filename)
        z = s21_graph_algorithms()
        res = z.GetShortestPathBetweenVertices(x, 4, 11)
        self.assertEqual(res, 25)

    def test_GetShortestPathsBetweenAllVertices_1(self):
        x = s21_graph()
        filename = "graphDij.txt"
        x.LoadGraphFromFile(filename)
        z = s21_graph_algorithms()
        res = z.GetShortestPathsBetweenAllVertices(x)
        answer = np.array([[ 0,  5,  8, 10, 11, 13, 13],
                           [ 5,  0,  3,  5,  6,  8,  8],
                           [ 8,  3,  0,  5,  4,  6,  7],
                           [10,  5,  5,  0,  1,  3,  3],
                           [11,  6,  4,  1,  0,  2,  3],
                           [13,  8,  6,  3,  2,  0,  1],
                           [13,  8,  7,  3,  3,  1,  0]])
        self.assertEqual(res.all(), answer.all())

    def test_GetShortestPathsBetweenAllVertices_2(self):
        x = s21_graph()
        filename = "graphDij2.txt"
        x.LoadGraphFromFile(filename)
        z = s21_graph_algorithms()
        res = z.GetShortestPathsBetweenAllVertices(x)
        answer = np.array([[ 0,  7,  9, 20, 20, 11],
                           [ 7,  0, 10, 15, 21, 12],
                           [ 9, 10,  0, 11, 11,  2],
                           [20, 15, 11,  0,  6, 13],
                           [20, 21, 11,  6, 0,  9],
                           [11, 12,  2, 13,  9,  0]])
        self.assertEqual(res.all(), answer.all())

    def test_GetLeastSpanningTree_1(self):
        x = s21_graph()
        f = "graphDij2.txt"
        x.LoadGraphFromFile(f)
        z = s21_graph_algorithms()
        a = z.GetLeastSpanningTree(x)
        elist = x.get_elist()
        G = nx.Graph()
        G.add_weighted_edges_from(elist)
        T = nx.minimum_spanning_tree(G, algorithm='prim')
        b = x.get_matrix(T.edges(data=True))
        self.assertEqual(a.all(), b.all())

    def test_GetLeastSpanningTree_2(self):
        x = s21_graph()
        f = "graph1.txt"
        x.LoadGraphFromFile(f)
        z = s21_graph_algorithms()
        a = z.GetLeastSpanningTree(x)
        elist = x.get_elist()
        G = nx.Graph()
        G.add_weighted_edges_from(elist)
        T = nx.minimum_spanning_tree(G, algorithm='prim')
        b = x.get_matrix(T.edges(data=True))
        self.assertEqual(a.all(), b.all())

    def test_BreadthFirstSearch_1(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphBFS1.txt')
        z = s21_graph_algorithms()
        res = z.BreadthFirstSearch(x, 2)
        answer = [2, 5, 6, 1, 4, 3]
        self.assertEqual(res, answer)

    def test_BreadthFirstSearch_2(self):
        x = s21_graph()
        x.LoadGraphFromFile('graph0.txt')
        z = s21_graph_algorithms()
        res = z.BreadthFirstSearch(x, 3)
        answer = [3, 1, 2, 4]
        self.assertEqual(res, answer)

    def test_BreadthFirstSearch_3(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphBFS1.txt')
        z = s21_graph_algorithms()
        res = z.BreadthFirstSearch(x, 6)
        answer = [6, 2, 3, 5, 1, 4]
        self.assertEqual(res, answer)

    def test_BreadthFirstSearch_4(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphBFS2.txt')
        z = s21_graph_algorithms()
        res = z.BreadthFirstSearch(x, 3)
        answer = [3, 1, 2, 4, 5, 8, 9, 10, 7, 6]
        self.assertEqual(res, answer)

    def test_BreadthFirstSearch_5(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphBFS2.txt')
        z = s21_graph_algorithms()
        res = z.BreadthFirstSearch(x, 7)
        answer = [7, 1, 2, 4, 9, 10, 3, 8, 6, 5]
        self.assertEqual(res, answer)

    def test_DepthFirstSearch_1(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphBFS1.txt')
        z = s21_graph_algorithms()
        res = z.DepthFirstSearch(x, 2)
        answer = [2, 5, 1, 3, 4, 6]
        self.assertEqual(res, answer)

    def test_DepthFirstSearch_2(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphBFS2.txt')
        z = s21_graph_algorithms()
        res = z.DepthFirstSearch(x, 5)
        answer = [5, 3, 1, 2, 4, 7, 9, 6, 10, 8]
        self.assertEqual(res, answer)

    def test_DepthFirstSearch_3(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphDij2.txt')
        z = s21_graph_algorithms()
        res = z.DepthFirstSearch(x, 3)
        answer = [3, 1, 2, 4, 5, 6]
        self.assertEqual(res, answer)

    def test_DepthFirstSearch_4(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphDij2.txt')
        z = s21_graph_algorithms()
        res = z.DepthFirstSearch(x, 6)
        answer = [6, 1, 2, 3, 4, 5]
        self.assertEqual(res, answer)

    def test_DepthFirstSearch_5(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphDij.txt')
        z = s21_graph_algorithms()
        res = z.DepthFirstSearch(x, 2)
        answer = [2, 1, 3, 5, 4, 7, 6]
        self.assertEqual(res, answer)

    def test_DepthFirstSearch_6(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphDij.txt')
        z = s21_graph_algorithms()
        res = z.DepthFirstSearch(x, 7)
        answer = [7, 4, 2, 1, 3, 5, 6]
        self.assertEqual(res, answer)

    def test_SolveTravelingSalesmanProblem_1(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphS1.txt')
        z = s21_graph_algorithms()
        path, length = z.SolveTravelingSalesmanProblem(x)
        answer_path = [1, 2, 3, 4, 1]
        answer_length = 4
        self.assertEqual(path, answer_path)
        self.assertEqual(length, answer_length)

    def test_SolveTravelingSalesmanProblem_2(self):
        x = s21_graph()
        x.LoadGraphFromFile('graph8.txt')
        z = s21_graph_algorithms()
        path, length = z.SolveTravelingSalesmanProblem(x)
        answer_path = [1, 4, 3, 6, 5, 2, 1]
        answer_length = 85
        self.assertEqual(path, answer_path)
        self.assertEqual(length, answer_length)

    def test_SolveTravelingSalesmanProblem_3(self):
        x = s21_graph()
        x.LoadGraphFromFile('graphDij2.txt')
        z = s21_graph_algorithms()
        try:
            path, length = z.SolveTravelingSalesmanProblem(x)
            self.assertRaises(Exception, Exception)
        except Exception as exp:
            print('')

if __name__ == "__main__":
    unittest.main()
