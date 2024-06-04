import numpy as np

class s21_graph():

    def __init__(self):
        self.__size = 0
        self.__matrix = np.array(0)

    def get_graph_matrix(self):
        return self.__matrix

    def get_graph_size(self):
        return self.__size

    def get_elist(self):
        return [(i, j, self.__matrix[i][j]) for i in range(self.__size) for j in range(self.__size)]

    def get_matrix(self, elist):
        m = np.zeros((self.__size, self.__size), dtype=int)
        for i, j, w in elist:
            m[i][j] = m[j][i] = w['weight']
        return m

    def LoadGraphFromFile(self, filename: str):
        try:
            with open(filename, "r") as f:
                self.__matrix = np.loadtxt(filename, skiprows=1, dtype=int)
                self.__size = len(self.__matrix)

        except Exception as exp:
            print(exp)

    def ExportGraphToDot(self, filename: str):
        try:
            exept_list = []
            with open(filename, "w") as f:
                f.write("graph graphname {")
                f.write("\n")
                for i in range(self.__size):
                    for j in range(self.__size):
                        if self.__matrix[i][j] > 0 and (i, j) not in exept_list:
                            exept_list.append((j, i))
                            f.write("\t")
                            f.write(str(i + 1))
                            f.write(" -- ")
                            f.write(str(j + 1))
                            f.write(";")
                            f.write("\n")
                f.write("}")
        except Exception as exp:
            print(exp)



if __name__ == "__main__":
    x = s21_graph()
    filename = "graphDij.txt"
    x.LoadGraphFromFile(filename)
    x.ExportGraphToDot("test_dot.dot")
    print(x.get_graph_matrix())