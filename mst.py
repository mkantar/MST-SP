# CENG 412 HW04 Spring 2018
# Author: Muharrem Kantar
# Date: 5/16/2018
# Implementing Dijkstra's Algorithm For Shortest Path

import sys


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

    def shortest_path(self):
        dst = {}
        lst = {}
        source = self.vertices[0].name
        dst[source] = 0
        for vertex in self.vertices:
            if vertex.name != source:
                dst[vertex.name] = sys.maxsize
            lst[vertex.name] = vertex

        while lst:
            m = sys.maxsize
            min_vertex = 'a'
            for key, value in lst.items():
                if dst[key] < m:
                    m = dst[key]
                    min_vertex = key

            vertex = lst[min_vertex]
            lst.pop(min_vertex)

            for adjacent in vertex.adjacents:
                alt = dst[min_vertex] + adjacent["weight"]
                if alt < dst[adjacent["node"].name]:
                    dst[adjacent["node"].name] = alt
        dst.pop(source)
        return dst


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


def print_mst(T):
    total_weight = 0
    for edge in T:
        total_weight = total_weight + edge.weight

    print(total_weight)

    for edge in T:
        print(edge.n1.name + " " + edge.n2.name)


def print_shortest_path(P):
    for key, value in P.items():
        print(key, value)


def main():
    val = input()
    nodes = []
    vertices = {}
    while len(val) != 0:
        val = val.split(' ')
        nodes.append(val)
        val = input()

    for node in nodes:
        vertices[node[0]] = Node(node[0])

    for node in nodes:
        d = {}
        for i in range(1, len(node)):
            if i % 2 == 0:
                d["weight"] = int(node[i])
                vertices[node[0]].push(d)
                d = {}
            else:
                d["node"] = vertices[node[i]]

    g = Graph(list(vertices.values()))

    # T = g.mst()
    #
    # print_mst(T)

    P = g.shortest_path()

    print_shortest_path(P)


main()
