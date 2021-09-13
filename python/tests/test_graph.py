from graph.graph import Graph

# Node can be successfully added to the graph


def test_node_to_graph():
    graph = Graph()
    assert graph.add_node("z").value == "z"
# An edge can be successfully added to the graph


def test_edge_to_graph():
    graph = Graph()
    node_1 = graph.add_node("z")
    node_2 = graph.add_node("a")
    assert graph.add_edge(node_2, node_1).vertex.value == "z"
# A collection of all nodes can be properly retrieved from the graph


def test_get_all_nodes():
    graph = Graph()
    _ = graph.add_node("z")
    _ = graph.add_node("a")
    get_nodes = graph.get_nodes()
    actual = [vertex.value for vertex in get_nodes]
    expected = ['z', 'a']
    assert actual == expected
# All appropriate neighbors can be retrieved from the graph


def test_get_neighbors():
    graph = Graph()
    node_z = graph.add_node("z")
    node_a = graph.add_node("a")
    node_y = graph.add_node("y")
    node_f = graph.add_node("f")
    graph.add_edge(node_a, node_z)
    graph.add_edge(node_a, node_f)
    graph.add_edge(node_a, node_y)
    get_neighbors = graph.get_neighbors(node_a)
    actual = [neighbor.vertex.value for neighbor in get_neighbors]
    expected = ['z', 'f', 'y']
    assert actual == expected
# Neighbors are returned with the weight between nodes included


def test_get_neighbors_with_weight():
    graph = Graph()
    node_z = graph.add_node("z")
    node_a = graph.add_node("a")
    node_y = graph.add_node("y")
    node_f = graph.add_node("f")
    graph.add_edge(node_a, node_z, 2)
    graph.add_edge(node_a, node_f, 5)
    graph.add_edge(node_a, node_y, 4)
    get_neighbors = graph.get_neighbors(node_a)
    actual = [node_a.value]
    for neighbor in get_neighbors:
        actual += [[neighbor.vertex.value, neighbor.weight]]
    expected = ['a', ['z', 2], ['f', 5], ['y', 4]]
    assert actual == expected
# The proper size is returned, representing the number of nodes in the graph


def test_get_graph_size():
    graph = Graph()
    _ = graph.add_node("z")
    _ = graph.add_node("a")
    _ = graph.add_node("y")
    _ = graph.add_node("f")
    assert graph.size() == 4
# A graph with only one node and edge can be properly returned


def test_get_graph_one_node_and_edge():
    graph = Graph()
    node_a = graph.add_node("a")
    graph.add_edge(node_a, node_a, 2)
    actual = [node_a.value]
    get_neighbors = graph.get_neighbors(node_a)
    for neighbor in get_neighbors:
        actual += [[neighbor.vertex.value, neighbor.weight]]
    expected = ['a', ['a', 2]]
    assert actual == expected
# An empty graph properly returns null


def test_empty_graph():
    graph = Graph()

    assert not graph.get_nodes()


# de

def test_get_graph_breadthFirst():
    graph = Graph()
    node_z = graph.add_node("z")
    node_a = graph.add_node("a")
    node_y = graph.add_node("y")
    node_f = graph.add_node("f")
    graph.add_edge(node_a, node_z, 2)
    graph.add_edge(node_z, node_f, 5)
    graph.add_edge(node_a, node_y, 4)
    breadth = graph.breadthFirst(node_a)
    actual = [vertex.value for vertex in breadth]
    expected = ['a', 'z', 'y', 'f']
    assert actual == expected


def test_get_breadthFirst_graph_one_vertex():
    graph = Graph()
    node_a = graph.add_node("a")

    breadth = graph.breadthFirst(node_a)
    actual = [vertex.value for vertex in breadth]
    expected = ['a']
    assert actual == expected


def test_get_breadthFirst_empty_graph():
    graph = Graph()
    breadth = graph.breadthFirst()
    actual = [vertex.value for vertex in breadth]
    expected = []
    assert actual == expected
