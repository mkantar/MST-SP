class Node:
    count = 0

    def __init__(self, name):
        self.__name = name
        self.__adjacents = []
        self.__index = Node.count
        Node.count = Node.count + 1

    @property
    def name(self):
        return self.__name

    @property
    def adjacents(self):
        return self.__adjacents

    @property
    def index(self):
        return self.__index

    @name.setter
    def name(self, val):
        self.__name = val

    def push(self, n):
        self.adjacents.append(n)


class Edge:
    def __init__(self, n1, n2, weight):
        self.__n1 = n1
        self.__n2 = n2
        self.__weight = weight

    def __repr__(self):
        return '{}: {} - {}, w: {}'.format(self.__class__.__name__, self.n1.name, self.n2.name, self.weight)

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    @property
    def n1(self):
        return self.__n1

    @property
    def n2(self):
        return self.__n2

    @property
    def weight(self):
        return self.__weight


class Graph:
    def __init__(self, vertices):
        self.__vertices = vertices
        self.__weights = []
        self.__edges = []

        for vertex in vertices:
            arr = [0] * len(vertices)
            for adjacent in vertex.adjacents:
                arr[adjacent["node"].index] = adjacent["weight"]
            self.__weights.append(arr)

        for i in range(len(vertices) - 1):
            arr = self.__weights[i]
            for j in range(i+1, len(arr)):
                if arr[j] != 0:
                    self.__edges.append(Edge(vertices[i], vertices[j], arr[j]))

    @property
    def vertices(self):
        return self.__vertices

    @property
    def weights(self):
        return self.__weights

    @property
    def edges(self):
        return self.__edges

    def mst(self):
        sorted_edges = sorted(self.edges)

        T = []

        for edge in sorted_edges:
            if self.is_different(T, edge):
                T.append(edge)

        return T

    def is_different(self, T, candidate):
        is_found_n1 = False
        if len(T) == 0:
            return True
        for edge in T:
            if candidate.n1.name == edge.n1.name:
                is_found_n1 = True

        for edge in T:
            if candidate.n2.name == edge.n1.name and is_found_n1:
                return False

        for edge in T:
            if candidate.n1.name == edge.n2.name:
                is_found_n1 = True

        for edge in T:
            if candidate.n2.name == edge.n2.name and is_found_n1:
                return False

        return True


def main():
    n1 = Node('a')
    n2 = Node('b')
    n3 = Node('c')
    n4 = Node('d')

    n1.push({"node": n2, "weight": 5})
    n1.push({"node": n4, "weight": 1})

    n2.push({"node": n1, "weight": 5})
    n2.push({"node": n4, "weight": 8})

    n3.push({"node": n4, "weight": 15})

    n4.push({"node": n1, "weight": 1})
    n4.push({"node": n2, "weight": 8})
    n4.push({"node": n3, "weight": 15})

    vertices = [n1, n2, n3, n4]

    g = Graph(vertices)

    print(g.weights)

    edges = g.edges

    print(sorted(edges))

    for edge in edges:
        print("edge: " + edge.n1.name + " - " + edge.n2.name + ", w: " + str(edge.weight))

    T = g.mst()

    print(T)


main()
