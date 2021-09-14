from collections import deque


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """
        Adds a vertex to the graph

        arguments
        vertex: Vertex
        """
        vertex = Vertex(value)

        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Adds an edge to our graph

        """
        if start_vertex not in self._adjacency_list:
            raise ValueError('Start vertex not exist in the graph')
        if end_vertex not in self._adjacency_list:
            raise ValueError('End Vertex not exist in the graph')

        self._adjacency_list[start_vertex].append(Edge(end_vertex, weight))
        return self._adjacency_list[start_vertex][0]

    def get_nodes(self):
        """
            Arguments: none
            Returns all of the nodes in the graph as a collection (set, list, or similar)
        """
        if len(self._adjacency_list) == 0:
            return None
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
            Arguments: node
            Returns a collection of edges connected to the given node
            Include the weight of the connection in the returned collection
        """
        return self._adjacency_list.get(vertex, [])

    def size(self):
        """
            Arguments: none
            Returns the total number of nodes in the graph
        """
        return len(self._adjacency_list)

    def breadthFirst(self, vertex=None, action=lambda x: print(x)):
        """
        Performs a level order traversal of the graph and calls action at each node
        """
        if not vertex:
            return[]
        breadth = Queue()
        visited = set()
        nodes = []
        breadth.enqueue(vertex)
        visited.add(vertex)
        while len(breadth):
            front = breadth.dequeue()
            nodes.append(front)
            neighbors = self.get_neighbors(front)

            for edge in neighbors:
                n_v = edge.vertex
                if n_v in visited:
                    continue
                else:
                    visited.add(n_v)
                    breadth.enqueue(n_v)
        return nodes

    def depth_first(self, vertex=None):
        if not vertex:
            return[]
        visited = set()
        nodes = []

        def rec_fun(node):
            neighbors = self.get_neighbors(node)

            for neighbor in neighbors:
                n_v = neighbor.vertex
                if n_v in visited:
                    continue
                else:
                    nodes.append(n_v)
                    visited.add(n_v)
                    rec_fun(n_v)

        nodes.append(vertex)
        rec_fun(vertex)
        return nodes


if __name__ == "__main__":
    # graph = Graph()
    # node_z = graph.add_node("z")
    # node_a = graph.add_node("a")
    # node_y = graph.add_node("y")
    # node_f = graph.add_node("f")
    # graph.add_edge(node_a, node_z)
    # graph.add_edge(node_z, node_f)
    # graph.add_edge(node_f, node_y)
    # print(graph.breadthFirst(node_a))
    # print(graph.depth_first(node_a))
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
    print(actual)
