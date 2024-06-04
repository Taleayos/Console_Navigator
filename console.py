from graph_algorithms import *
from graph import *
import datetime

def check_graph():
    if x.get_graph_size() == 0:
        print("Oops! No graph! First load the graph from file ...")
        return False
    else:
        return True

def show_console():
    print("\n")
    print("*************************************  SimpleNavigator  *************************************")
    print("---------------------------------------------------------------------------------------------")
    print("            PRESS 1 - Load the original graph from a file  ")
    print("---------------------------------------------------------------------------------------------")
    print("            PRESS 2 - Traverse the graph in breadth ")
    print("---------------------------------------------------------------------------------------------")
    print("            PRESS 3 - Traverse the graph in depth  ")
    print("---------------------------------------------------------------------------------------------")
    print("            PRESS 4 - Find the shortest path between any two vertices  ")
    print("---------------------------------------------------------------------------------------------")
    print("            PRESS 5 - Find the shortest paths between all pairs of vertices in the graph  ")
    print("---------------------------------------------------------------------------------------------")
    print("            PRESS 6 - Search for the minimum spanning tree in the graph   ")
    print("---------------------------------------------------------------------------------------------")
    print("            PRESS 7 - Solve the Salesman problem  ")
    print("---------------------------------------------------------------------------------------------")
    print("            PRESS 8 - Comparison of methods for solving the traveling salesman problem  ")
    print("---------------------------------------------------------------------------------------------")
    print("            PRESS 9 - EXIT  ")
    print("---------------------------------------------------------------------------------------------")
def switch(press: int):
    if press == 1:
        filename = input("Enter file name: ")
        try:
            x.LoadGraphFromFile(filename)
        except Exception as exp:
            print(exp)

    elif press == 2:
        if check_graph():
            start_ver = int(input("Enter start vertex: "))
            if 1 <= start_ver <= x.get_graph_size():
                res2 = z.BreadthFirstSearch(x, start_ver)
                print(res2)
            else:
                print("Oops!  That was no valid vertex.  Try again...")

    elif press == 3:
        # print(x.get_graph_size())
        if check_graph():
            start_ver = int(input("Enter start vertex: "))
            if 1 <= start_ver <= x.get_graph_size():
                res3 = z.DepthFirstSearch(x, start_ver)
                print(res3)
            else:
                print("Oops!  That was no valid vertex.  Try again...")
    elif press == 4:
        if check_graph():
            vertex1 = int(input("Enter start vertex: "))
            vertex2 = int(input("Enter finish vertex: "))
            if 1 <= vertex1 <= x.get_graph_size() and 1 <= vertex2 <= x.get_graph_size():
                res4 = z.GetShortestPathBetweenVertices(x, vertex1, vertex2)
                print(res4)
            else:
                print("Oops!  That was no valid vertex.  Try again...")

    elif press == 5:
        if check_graph():
            res5 = z.GetShortestPathsBetweenAllVertices(x)
            print(res5)
    elif press == 6:
        if check_graph():
            res6 = z.GetLeastSpanningTree(x)
            print(res6)
    elif press == 7:
        if check_graph():
            try:
                res7, res7_1 = z.SolveTravelingSalesmanProblem(x)
                print(res7)
                print(res7_1)
            except Exception as exp:
                print(exp)

    elif press == 8:
        if check_graph():
            try:
                count = int(input("Enter N times: "))
                if 16000 >= count > 0:
                    start = datetime.datetime.now()
                    res7, res7_1 = z.SolveTravelingSalesmanProblem(x, count)
                    finish = datetime.datetime.now()
                    print("Running time for an ant colony algorithm: " + str(finish - start))

                    w = 0
                    start1 = datetime.datetime.now()
                    while w < count:
                        res8, res8_1 = z.Nearest_neighbor_method(x)
                        w += 1
                    finish1 = datetime.datetime.now()
                    print("Running time for the nearest neighbor algorithm: " + str(finish1 - start1))

                    start2 = datetime.datetime.now()
                    res7, res7_1 = z.STSP_one_step_algo(x, count)
                    finish2 = datetime.datetime.now()
                    print("Running time for an one step algorithm: " + str(finish2 - start2))

                else:
                    print("Oooops! Invalid number ...")
            except Exception as exp:
                print(exp)

    elif press == 9:
        exit()

if __name__ == "__main__":
    x = s21_graph()
    z = s21_graph_algorithms()
    while True:
        show_console()
        try:
            press = int(input())
            switch(press)
        except Exception as exp:
            print(exp)

