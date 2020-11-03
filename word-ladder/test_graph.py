import pytest
from graph import Graph, Edge, Node


class TestNode:
    def test_node_value(self):
        node1 = Node("one")
        assert "one" == node1.value

    def test_node_compare(self):
        node1 = Node("one")
        node2 = Node("two")
        assert node1 != node2
        assert node1 == node1

    def test_node_set_parent(self):
        node1 = Node("one")
        node2 = Node("two")
        node2.set_parent(node1)
        assert node2.parent.value == "one"

    def test_node_init_parent(self):
        node1 = Node("one")
        node2 = Node("two", node1)
        assert node2.parent.value == "one"


class TestEdge:
    def test_edge_nodes(self):
        edge1 = Edge("one", "two")
        assert edge1.start == "one" and edge1.end == "two"
        assert edge1.weight is None

    def test_edge_ends(self):
        edge1 = Edge("one", "two", 5)
        assert {"one", "two"} == edge1.ends
        assert edge1.weight == 5

    def test_edge_compare(self):
        edge1 = Edge("one", "two")
        edge2 = Edge("two", "one")
        assert edge1 != edge2
        assert edge1 == edge1


class TestGraph:
    def test_graph_new(self):
        graph1 = Graph()
        graph2 = Graph()
        vertex = graph1.new_vertex("one")
        assert isinstance(vertex, Node)
        assert len(graph1.get_vertices()) == 1
        assert len(graph2.get_vertices()) == 0

    def test_graph_new_vertex(self):
        graph1 = Graph()
        graph1.new_vertex("one")
        graph1.new_vertex("two")
        assert len(graph1.get_vertices()) == 2

    def test_graph_duplicate_new_vertex(self):
        graph1 = Graph()
        vertex1 = graph1.new_vertex("one")
        assert isinstance(vertex1, Node)
        assert len(graph1.get_vertices()) == 1
        vertex2 = graph1.new_vertex("one")
        assert vertex2 is None
        assert len(graph1.get_vertices()) == 1

    def test_graph_insert_node(self):
        graph1 = Graph()
        node1 = Node("one")
        graph1.insert_node(node1)
        assert len(graph1.get_vertices()) == 1

    def test_graph_insert_duplicate_node(self):
        graph1 = Graph()
        node1 = Node("one")
        node2 = Node("one")
        ins1 = graph1.insert_node(node1)
        assert len(graph1.get_vertices()) == 1
        assert ins1 == 1
        ins2 = graph1.insert_node(node2)
        assert len(graph1.get_vertices()) == 1
        assert ins2 == 0

    def test_graph_get_vertex(self):
        graph1 = Graph()
        graph1.new_vertex("one")
        vertex = graph1.get_vertex("one")
        assert isinstance(vertex, Node)
        assert vertex.value == "one"

    def test_graph_get_vertices(self):
        graph1 = Graph()
        graph1.new_vertex("one")
        vertices = graph1.get_vertices()
        assert len(vertices) == 1
        assert vertices[0] == "one"

    def test_graph_new_edge(self):
        graph1 = Graph()
        graph1.new_edge("one", "two")
        assert len(graph1.get_edges()) == 1

    def test_graph_find_edge(self):
        graph1 = Graph()
        graph1.new_edge("one", "two")
        edge1 = graph1.get_edge("one", "two")
        assert edge1.start == "one"
        assert edge1.end == "two"
        edge2 = graph1.get_edge("two", "one")
        assert edge2.start == "one"
        assert edge2.end == "two"
        edge3 = graph1.get_edge("three", "four")
        assert edge3 is None

    def test_graph_adj_matrix(self):
        graph1 = Graph()
        graph1.new_vertex("one")
        graph1.new_vertex("two")
        graph1.new_edge("one", "two")
        matrix = graph1.get_adj_matrix()
        assert len(matrix) == 2
        assert len(matrix[0]) == 2
        assert matrix[0][1] == 1
        assert matrix[0][0] == 0

    def test_graph_adj_node_values(self):
        graph1 = Graph()
        graph1.new_vertex("one")
        graph1.new_vertex("two")
        graph1.new_vertex("three")
        graph1.new_edge("one", "two")
        nodes = graph1.get_adj_node_values("one")
        assert len(nodes) == 1
        assert "one" not in nodes
        assert "two" in nodes
        graph1.new_edge("one", "three")
        nodes = graph1.get_adj_node_values("one")
        assert len(nodes) == 2
        assert "three" in nodes

    def test_graph_adj_nodes(self):
        graph1 = Graph()
        graph1.new_vertex("one")
        graph1.new_vertex("two")
        graph1.new_vertex("three")
        graph1.new_edge("one", "two")
        nodes = graph1.get_adj_nodes("one")
        assert len(nodes) == 1
        assert "two" == nodes[0].value
        graph1.new_edge("one", "three")
        nodes = graph1.get_adj_nodes("one")
        assert len(nodes) == 2
        assert "three" == nodes[1].value

    def test_graph_adj_list(self):
        graph1 = Graph()
        graph1.new_vertex("one")
        graph1.new_vertex("two")
        graph1.new_vertex("three")
        graph1.new_edge("one", "two")
        adj_list = graph1.get_adj_list()
        assert len(adj_list["one"]) == 1
        assert len(adj_list["three"]) == 0

    def test_graph_trace_path(self):
        graph1 = Graph()
        node1 = Node("one")
        node2 = Node("two", node1)
        graph1.insert_node(node1)
        graph1.insert_node(node2)
        route = graph1.trace_back("two")
        assert route == ["one", "two"]


pytest.main()