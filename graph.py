class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        #stores adjacency list for each node
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join(["{}: {}".format(n, neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__reper__()