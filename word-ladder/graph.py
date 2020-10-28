from typing import List


class Graph:

    def __init__(self):
        self.vertices = {}
        self.edges = []

    def new_vertex(self, value):
        """Creates a new vertex and inserts it into the graph

        Parameters:
        value(Any): the value of the vertex to insert

        Returns:
        vertex(Node): the created node or None
        """
        if value not in self.get_vertices():
            vertex = Node(value)
            self.vertices[value] = vertex
            return vertex
        else:
            return None

    def insert_node(self, node):
        """Inserts an existing node object into the graph

        Parameters:
        node(Node): The node to insert into the graph

        Returns:
        (int): the count of nodes inserted (0 or 1)
        """
        if node.value not in self.get_vertices():
            self.vertices[node.value] = node
            return 1
        else:
            return 0

    def new_edge(self, start, end, weight=None):
        """Inserts the edge defined by start and end node values into the graph

        Parameters:
        start(Any): the value of the start node in the edge
        end(Any):   the value of the end node in the edge
        weight(int): Optionally the weight of the edge

        Returns:
        edge(Edge): the newly created edge
        """
        edge = Edge(start, end, weight)
        edge_list = self.get_edges()
        if edge.ends not in edge_list:
            self.edges.append(edge)
            return edge
        else:
            return None

    def get_vertices(self) -> List:
        """Returns the list of vertex values in the graph

        Returns:
        (List): List of vertex values in the graph
        """
        return list(self.vertices.keys())

    def get_edges(self) -> List:
        """Returns the list of Edges in the graph

        Returns:
        (List): a list of ends (Set) in the graph
        """
        return [x.ends for x in self.edges]

    def get_vertex(self, value):
        """Returns the node object identified by 'value'

        Parameters:
        value(Any): the value of the node to locate.

        Returns:
        (Node): the node whose value is 'value'
        """
        if value in self.vertices.keys():
            return self.vertices[value]
        else:
            return None

    def get_adj_matrix(self) -> List:
        """Produces the adjacency matrix for the graph

        Returns:
        matrix(List): A list of int lists containing 0s where the is no
            adjacency and 1s on coordinates where there IS adjacency of nodes.
        """
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
        """Produces the adjacency list for the graph

        Returns:
        adj_list(List): A list of dicts keyed on each node value and
            referencing a list of adjacent node values.
        """
        adj_list = {}
        for vtx in self.get_vertices():
            adj_list[vtx] = []
            for edge in self.edges:
                if vtx in edge.ends:
                    value = edge.ends - {vtx}
                    adj_list[vtx].append(value)
        return adj_list

    def trace_back(self, value) -> List:
        """ Traces backward through the graph starting from the designated node
            value and following parentNode links.

        Parameters:
        value (Any): the value of a start node in the graph

        Returns:
        path (List): an ordered list of values reversed (value at end)

        """
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
        """Updates the node with a parent node reference

        Parameters:
        parentNode(Node): The node to designate as the parent
        """
        self.parent = parentNode


class Edge:

    def __init__(self, start, end, weight=None):
        self.start = start
        self.end = end
        self.weight = weight
        self.ends = {start, end}
