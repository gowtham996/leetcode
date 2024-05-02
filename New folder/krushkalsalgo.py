class disjointset:
    def __init__(self, vertices):
        self.parent = list(range(len(vertices)))  # Initialize with indices instead of vertex labels

    def find_root(self, v):
        index = v
        if v == self.parent[index]:
            return v
        else:
            self.parent[index] = self.find_root(self.parent[index])
            return self.parent[index]

    def union(self, v1, v2):
        p1 = self.find_root(v1)
        p2 = self.find_root(v2)
        self.parent[p1] = p2

def distance(e):
    return e[2]

def kruskals(graph):
    obj = disjointset(graph['vertices'])
    edgelist = graph['edges']
    edgelist.sort(key=distance)
    mst = []

    for edge in edgelist:
        u, v, w = edge
        u_index = graph['vertices'].index(u)
        v_index = graph['vertices'].index(v)
        if obj.find_root(u_index) != obj.find_root(v_index):
            obj.union(u_index, v_index)
            mst.append(edge)

    return mst

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E'],
    'edges': [('A', 'B', 3), ('B', 'D', 2), ('D', 'E', 7), ('E', 'C', 1), ('C', 'D', 5), ('A', 'C', 4)]
}

mst = kruskals(graph)
print("Edges in MST:", mst)
