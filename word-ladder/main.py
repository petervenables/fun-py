from graph import Graph
import word_func
# import word_list as WL


def main():
    mygraph = Graph()

    set1 = ["dog", "dag", "cat", "cot", "kit", "cog", "cop"]

    for word in set1:
        mygraph.new_vertex(word)

    for start in mygraph.vertices:
        for end in mygraph.vertices:
            if start == end:
                next
            else:
                if word_func.hamming_distance(start, end) == 1:
                    mygraph.new_edge(start, end, 1)

    path = ["cat", "cot", "cog", "dog"]
    for idx, step in enumerate(path):
        if idx >= len(path)-1:
            next
        else:
            vertex = mygraph.get_vertex(step)
            if vertex is not None:
                parent = mygraph.get_vertex(path[idx+1])
                if parent is not None:
                    vertex.parent = parent

    route = mygraph.trace_back("cat")
    print(route)

    print(mygraph.get_edges())

    header = mygraph.get_vertices()
    header.insert(0, "-")
    adj_matrix = mygraph.get_adj_matrix()
    adj_matrix.insert(0, header)
    for label in header:
        if label != "-":
            adj_matrix[header.index(label)].insert(0, label)
    for row in adj_matrix:
        print("\t".join(str(x) for x in row))

    adj_list = mygraph.get_adj_list()
    for key in adj_list.keys():
        print(f"{key}: {adj_list[key]}")


if __name__ == "__main__":
    main()
