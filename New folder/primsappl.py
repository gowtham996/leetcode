import heapq

def prims(graph, source, destination):
    visited = set()
    mincost = 0
    minheap = [(0, source)]
    
    while minheap:
        cost, current_vertex = heapq.heappop(minheap)
        
        if current_vertex not in visited:
            visited.add(current_vertex)
            if current_vertex == destination:
                return mincost
            for src, dest, edgecost in graph['edges']:
                if current_vertex == src and dest not in visited:
                    mincost += edgecost  # Update mincost with the edgecost
                    heapq.heappush(minheap, (edgecost, dest))
    return float('inf')

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E'],
    'edges': [('A', 'B', 2), ('B', 'D', 4), ('D', 'E', 5), ('C', 'E', 1), ('C', 'D', 6), ('A', 'C', 3)]
}
print("corrected:", prims(graph, 'A', 'B'))
