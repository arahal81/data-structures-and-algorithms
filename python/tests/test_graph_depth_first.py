from graph.graph import Graph


def test_df_graph_one():
    graph = Graph()
    node_a = graph.add_node("A")
    node_b = graph.add_node("B")
    node_c = graph.add_node("C")
    node_g = graph.add_node("G")
    node_d = graph.add_node("D")
    node_e = graph.add_node("E")
    node_h = graph.add_node("H")
    node_f = graph.add_node("F")
    graph.add_edge(node_a, node_b)
    graph.add_edge(node_a, node_d)
    graph.add_edge(node_b, node_c)
    graph.add_edge(node_c, node_g)
    graph.add_edge(node_b, node_d)
    graph.add_edge(node_d, node_e)
    graph.add_edge(node_d, node_h)
    graph.add_edge(node_d, node_f)
    graph.add_edge(node_f, node_h)
    breadth = graph.depth_first(node_a)
    actual = [vertex.value for vertex in breadth]
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert expected == actual


def test_df_graph_two():
    graph = Graph()
    node_a = graph.add_node("A")
    node_b = graph.add_node("B")
    node_c = graph.add_node("C")
    node_g = graph.add_node("G")
    node_d = graph.add_node("D")
    node_e = graph.add_node("E")
    node_h = graph.add_node("H")
    node_f = graph.add_node("F")
    graph.add_edge(node_a, node_b)
    graph.add_edge(node_a, node_d)
    graph.add_edge(node_b, node_c)
    graph.add_edge(node_c, node_g)
    graph.add_edge(node_b, node_d)
    graph.add_edge(node_d, node_e)
    graph.add_edge(node_d, node_f)
    graph.add_edge(node_d, node_h)
    graph.add_edge(node_f, node_h)
    breadth = graph.depth_first(node_a)
    actual = [vertex.value for vertex in breadth]
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'F', 'H']
    assert expected == actual


def test_df_empty_graph():

    graph = Graph()
    assert graph.depth_first() == []
