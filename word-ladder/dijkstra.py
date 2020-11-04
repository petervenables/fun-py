# from graph import Graph
# from word_list import dictionary as word_list
# from word_func import hamming_distance


class DijkstraSPFSolver:

    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.checked = []
        self.todo = []

    def solve(self):
        for vertex in self.graph.vertices.values():
            key = vertex.value
            if key == self.start:
                vertex.distance = 0
                vertex.parent = None
            for adj in self.graph.get_adj_nodes(key):
                edge = self.graph.get_edge(key, adj.value)
                tdist = edge.weight + vertex.distance
                if adj.distance > tdist:
                    adj.distance = tdist
                    adj.parent = vertex
            self.checked.append(key)

    def show_solution(self):
        path = []
        vertex = self.graph.vertices[self.end]
        while vertex.parent is not None:
            if vertex.value not in path:
                path.append(vertex.value)
            vertex = vertex.parent
        path.append(vertex.value)
        return path[::-1]
