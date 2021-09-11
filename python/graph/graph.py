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

    def _breadthFirst(self, vertex, action=lambda x: print(x)):
        """
        Performs a level order traversal of the graph and calls action at each node
        """
        breadth = Queue()
        visited = set()
        nodes = []
        breadth.enqueue(vertex)
        visited.add(vertex)
        while len(breadth):
            front = breadth.dequeue()
            nodes.append(front.value)
            neighbors = self.get_neighbors(front.value)

            for edge in neighbors:
                n_v = edge.vertex
                if n_v in visited:
                    continue
                else:
                    visited.add(n_v)
                    breadth.enqueue(n_v)
        return nodes
