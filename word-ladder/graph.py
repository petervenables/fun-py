from typing import List


class Graph:

    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, value):
        self.vertices[value] = Node(value)

    def add_node(self, node):
        self.vertices[node.value] = node

    def add_edge(self, start, end, weight=None):
        edge = Edge(start, end, weight)
        edge_list = self.get_edges()
        if edge.ends not in edge_list:
            self.edges.append(edge)

    def get_vertices(self) -> List:
        return list(self.vertices.keys())

    def get_edges(self) -> List:
        return [x.ends for x in self.edges]

    def get_vertex(self, value):
        if value in self.vertices.keys():
            return self.vertices[value]
        else:
            return None

    def get_adj_matrix(self) -> List:
        matrix = []
        header = []
        for head in self.get_vertices():
            header.append(head)
        for _ in self.vertices:
            line = [0] * len(self.vertices)
            matrix.append(line)
        for edge in self.edges:
            col = header.index(edge.start)
            row = header.index(edge.end)
            matrix[col][row] = 1
            matrix[row][col] = 1
        return matrix

    def get_adj_list(self) -> List:
        adj_list = {}
        for vtx in self.get_vertices():
            adj_list[vtx] = []
            for edge in self.edges:
                if vtx in edge.ends:
                    value = edge.ends - {vtx}
                    adj_list[vtx].append(value)
        return adj_list

    def trace_path(self, value) -> List:
        path = []
        node = self.get_vertex(value)
        if node is not None:
            path.append(node.value)
            while node.parent is not None:
                node = node.parent
                path.append(node.value)
        return path[::-1]


class Node:

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

    def set_parent(self, parentNode):
        self.parent = parentNode


class Edge:

    def __init__(self, start, end, weight=None):
        self.start = start
        self.end = end
        self.weight = weight
        self.ends = {start, end}
