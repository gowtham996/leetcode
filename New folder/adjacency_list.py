# # class Graph:
# #     def __init__(self):
# #         self.adjacency_list = {}

# #     def add_edge(self, vertex1, vertex2, weight):
# #         if vertex1 not in self.adjacency_list:
# #             self.adjacency_list[vertex1] = []
# #         if vertex2 not in self.adjacency_list:
# #             self.adjacency_list[vertex2] = []

# #         self.adjacency_list[vertex1].append((vertex2, weight))
# #         self.adjacency_list[vertex2].append((vertex1, weight))

# #     def format_adjacent_vertex(self, adjacent_vertex):
# #         vertex, weight = adjacent_vertex
# #         return f"({vertex}, {weight})"

# #     def display(self):
# #         for vertex in self.adjacency_list:
# #             adjacent_vertices = self.adjacency_list[vertex]
# #             formatted_adjacent_vertices = map(self.format_adjacent_vertex, adjacent_vertices)
# #             adjacent_vertices_str = ' -> '.join(formatted_adjacent_vertices)
# #             print(vertex, '->', adjacent_vertices_str)

# # if __name__ == "__main__":
# #     graph = Graph()
# #     graph.add_edge(0, 1, 10)
# #     graph.add_edge(0, 2, 100)
# #     graph.add_edge(1, 2, 200)
# #     graph.add_edge(1, 3, 20)
# #     graph.add_edge(2, 4, 2000)
# #     graph.display()


# # # class Graph:
# # #     def __init__(self):
# # #         self.list1={}
# # #     def addedge(self,ver1,ver2):
# # #         if ver1 not in self.list1:
# # #             self.list1[ver1]=[]
# # #         if ver2 not in self.list1:
# # #             self.list1[ver2]=[]
# # #         self.list1[ver1].append(ver2)
# # #         self.list1[ver2].append(ver1)
# # #     def display(self):
# # #         for i in self.list1:
# # #             print(i,'->','->'.join(map(str,self.list1[i])))
# # # ll=Graph()

# # # ll.addedge(0, 1)
# # # ll.addedge(0, 2)
# # # ll.addedge(1, 2)
# # # ll.addedge(1, 3)
# # # ll.addedge(2, 4)
# # # ll.display()


# class Graph:
#     def __init__(self, V):
#         self.V = V
#         self.adj_list={i : [] for i in range(V)}
#     def add_nodes(self, u, v, w):
#         self.adj_list[u].append((v,w))
#         self.adj_list[v].append((u,w))
#     def print_list(self):
#         for i in self.adj_list:
#            print(i,'->',' -> '.join(map(str,self.adj_list[i])))

# V = 5
# g = Graph(V)
# g.add_nodes(0, 1, 3)
# g.add_nodes(1, 2, 5)
# g.add_nodes(3, 4, 6)
# g.add_nodes(0, 4, 7)
# g.add_nodes(4, 1, 11)
# g.add_nodes(1, 3, 2)
# g.add_nodes(2, 3, 10)

# g.print_list()

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # Undirected graph

    @classmethod
    def from_edge_list(cls, edge_list, num_vertices):
        graph = cls(num_vertices)
        for edge in edge_list:
            u, v, weight = edge
            graph.add_edge(u, v, weight)
        return graph

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        parent = [-1] * self.V
        key = [float('inf')] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    parent[v] = u
                    key[v] = self.graph[u][v]

        return parent

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")

# Example usage:
edge_list = [
    (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11),
    (2, 3, 7), (2, 5, 4), (2, 8, 2), (3, 4, 9),
    (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1),
    (6, 8, 6), (7, 8, 7)
]
num_vertices = 9

g = Graph.from_edge_list(edge_list, num_vertices)
parent = g.prim_mst()
g.print_mst(parent)
