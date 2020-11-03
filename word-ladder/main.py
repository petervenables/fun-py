from graph import Graph
from dijkstra import DijkstraSPFSolver
from word_func import hamming_distance
from word_list import dictionary as word_list
import sys


def extend_graph(graph, start):
    """extends the graph around the given node value

    Parameters:
    start(str): a node value to extend the graph around
    dist(int): a distance from graph start value to use as weight

    Returns:
    graph(Graph): the updated graph with +1 adjacent nodes
        to the given node
    """
    if start not in graph.get_vertices():
        graph.new_vertex(start)

    for word in word_list:
        if hamming_distance(start, word) == 1:
            graph.new_vertex(word)
            graph.new_edge(start, word, 1)
    return graph


def converge_edges(graph):
    header = graph.get_vertices()
    for start in header:
        for end in header:
            if hamming_distance(start, end) == 1:
                graph.new_edge(start, end, 1)
    return graph


def show_matrix(graph):
    header = graph.get_vertices()
    matrix = graph.get_adj_matrix()
    header.insert(0, " - ")
    matrix.insert(0, header)
    for label in header:
        if label != " - ":
            matrix[header.index(label)].insert(0, label)
    for idx, row in enumerate(matrix):
        if idx == 0:
            print(" ".join(str(x) for x in row))
        else:
            print("   ".join(str(x) for x in row))


def show_adj_list(graph):
    adj_list = graph.get_adj_list()
    for key in adj_list.keys():
        print(f"{key}: {adj_list[key]}")


def main():
    mygraph = Graph()
    mygraph.new_vertex("dog")
    mygraph = extend_graph(mygraph, "dog")

    curr = mygraph.get_adj_node_values("dog")
    next = set()
    limit = 5
    count = 2
    while "cat" not in mygraph.get_vertices() and count < limit:
        for value in curr:
            mygraph = extend_graph(mygraph, value)
            if value not in next:
                next.add(value)
        for each in next:
            if each in curr:
                curr.remove(each)
            curr = curr.union(mygraph.get_adj_node_values(each))
        count += 1

    if "bat" not in mygraph.get_vertices():
        print("FAILED!")
        sys.exit(1)

    spfsolver = DijkstraSPFSolver(mygraph, "dog", "cat")
    spfsolver.solve()
    print(spfsolver.show_solution())


if __name__ == "__main__":
    main()
