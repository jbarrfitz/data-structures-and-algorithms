class Graph:
    """
    A class representing a graph data structure.

    Attributes:
        neighbors (dict): A dictionary mapping vertices to their respective neighbors.

    Methods:
        add_node(value): Adds a new vertex with the given value to the graph.
        add_edge(vertex1, vertex2, weight=None): Adds an edge between vertex1 and vertex2 with an optional weight.
        get_vertices(): Returns a list of all vertices in the graph.
        get_neighbors(vertex): Returns a list of neighbors of the specified vertex.
        size(): Returns the number of vertices in the graph.
        get_nodes(): Returns a list of all vertices in the graph (same as get_vertices()).
    """

    def __init__(self):
        """Initialize an empty graph."""
        self.neighbors = {}

    def add_node(self, value):
        """
        Add a new vertex with the given value to the graph.

        Args:
            value: The value of the new vertex.

        Returns:
            The newly created vertex.
        """
        vertex = Vertex(value)
        if vertex not in self.neighbors:
            self.neighbors[vertex] = []
        return vertex

    def add_edge(self, vertex1, vertex2, weight=None):
        """
        Add an edge between vertex1 and vertex2 with an optional weight.

        Args:
            vertex1: The first vertex of the edge.
            vertex2: The second vertex of the edge.
            weight (optional): The weight of the edge (default is None).

        Raises:
            KeyError: If either vertex1 or vertex2 is not in the graph.
        """
        if vertex1 in self.neighbors and vertex2 in self.neighbors:
            self.neighbors[vertex1].append(Edge(vertex2, weight))
            if vertex1 != vertex2:
                self.neighbors[vertex2].append(Edge(vertex1, weight))
        else:
            raise KeyError("Both vertices must be in the graph")

    def get_vertices(self):
        """
        Get a list of all vertices in the graph.

        Returns:
            A list of all vertices in the graph.
        """
        return list(self.neighbors.keys())

    def get_neighbors(self, vertex):
        """
        Get a list of neighbors of the specified vertex.

        Args:
            vertex: The vertex to retrieve the neighbors for.

        Returns:
            A list of neighbors of the specified vertex.
        """
        if vertex in self.neighbors:
            return self.neighbors[vertex]
        return []

    def size(self):
        """
        Get the number of vertices in the graph.

        Returns:
            The number of vertices in the graph.
        """
        return len(self.neighbors)

    def get_nodes(self):
        """
        Get a list of all vertices in the graph.

        Returns:
            A list of all vertices in the graph.
        """
        return list(self.neighbors.keys())


class Vertex:
    """
    A class representing a vertex in a graph.

    Attributes:
        value: The value associated with the vertex.

    Methods:
        __repr__(): Returns a string representation of the vertex.
    """

    def __init__(self, value):
        """Initialize a vertex with the given value."""
        self.value = value

    def __repr__(self):
        """Return a string representation of the vertex."""
        return str(self.value)


class Edge:
    """
    A class representing an edge in a graph.

    Attributes:
        vertex: The vertex that the edge connects to.
        weight: The weight of the edge.

    Methods:
        None
    """

    def __init__(self, vertex, weight):
        """Initialize an edge with the given vertex and weight."""
        self.vertex = vertex
        self.weight = weight
