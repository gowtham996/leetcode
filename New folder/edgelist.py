# # # tot=0
# # # edge_list=[('a','b',2),('b','d',4),('d','e',5),('c','e',1),('c','d',6),('a','c',3)]
# # # for i in edge_list:
# # #     tot+=i[2]
# # # print(tot)
# # # adlist=set()
# # # for i in edge_list:
# # #     adlist.add(i[0])
# # #     adlist.add(i[1])
# # # no=len(adlist)
# # # print(no)
# # # #empty adjacency list
# # # addlist={v:[] for v in adlist}
# # # print(addlist)
# # # for edge in adlist:
# # #     addlist[edge[0]].append(addlist[1])
# # # print(addlist)

# # # tot = 0
# # # edge_list = [('a', 'b', 2), ('b', 'd', 4), ('d', 'e', 5), ('c', 'e', 1), ('c', 'd', 6), ('a', 'c', 3)]


# # # for i in edge_list:
# # #     tot += i[2]
# # # print("Total weight of all edges:", tot)

# # # adlist = set()
# # # for i in edge_list:
# # #     adlist.add(i[0])
# # #     adlist.add(i[1])
# # # no = len(adlist)
# # # print("Number of vertices:", no)

# # # adjacency_list = {v: [] for v in adlist}
# # # print("Empty adjacency list:", adjacency_list)

# # # # Populate the adjacency list
# # # for edge in edge_list:
# # #     adjacency_list[edge_list].append(edge[1])  # Assuming the graph is undirected
# # # print("Populated adjacency list:", adjacency_list)


# # tot = 0
# # edge_list = [('a', 'b', 2), ('b', 'd', 4), ('d', 'e', 5), ('c', 'e', 1), ('c', 'd', 6), ('a', 'c', 3)]

# # for i in edge_list:
# #     tot += i[2]

# # print("Total weight of all edges:", tot)

# # adlist = set()
# # for i in edge_list:
# #     adlist.add(i[0])
# #     adlist.add(i[1])
# # no = len(adlist)
# # print("Number of vertices:", no)

# # adjacency_list = {v: [] for v in adlist}
# # print("Empty adjacency list:", adjacency_list)


# # for edge in edge_list:
# #     adjacency_list[edge[0]].append((edge[1]))  
# #     adjacency_list[edge[1]].append((edge[0]))  
# # print("Populated adjacency list:", adjacency_list)


# tot = 0
# edge_list = [('a', 'b', 2), ('b', 'd', 4), ('d', 'e', 5), ('c', 'e', 1), ('c', 'd', 6), ('a', 'c', 3)]

# for i in edge_list:
#     tot += i[2]
# print("Total weight of all edges:", tot)


# adj = set()
# for i in edge_list:
#     adj.add(i[0])
#     adj.add(i[1])
# print("Set of nodes:", adj)

# adjacency_set = {v: set() for v in adj}
# print("Empty adjacency set:", adjacency_set)

# for start, end, _ in edge_list:
#     adjacency_set[start].add(end)
#     adjacency_set[end].add(start)

# print("Populated adjacency set:", adjacency_set)
# #


import heapq

def prims(graph):
    adjlist = {v: [] for v in graph['vertices']}
    
    for edge in graph['edges']:
        adjlist[edge[0]].append((edge[1], edge[2]))  # (destination, weight)
        adjlist[edge[1]].append((edge[0], edge[2]))  # (source, weight)
    
    start = 'A'
    visited = set()
    visited.add(start)
    heap = [(weight, start, destination) for destination, weight in adjlist[start]]
    heapq.heapify(heap)
    mintree = []
    
    while heap:
        weight, source, destination = heapq.heappop(heap)
        if destination not in visited:
            visited.add(destination)
            mintree.append((weight, source, destination))
            for j, w in adjlist[destination]:
                if j not in visited:
                    heapq.heappush(heap, (w, destination, j))
    
    return mintree

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E'],
    'edges': [('A', 'B', 2), ('B', 'D', 4), ('D', 'E', 5), ('C', 'E', 1), ('C', 'D', 6),('A','C',3)]
}
print("original:",prims(graph))


