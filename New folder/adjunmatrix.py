def create_(edge_list):
    node_set=set()
    for edge in edge_list:
        node_set.add(edge[0])
        node_set.add(edge[1])
    nv=len(node_set)
    adj=[[0]*nv for i in range(nv)]
    for row in adj_mat:
        print(row)
    for edge in edge_list:
        s=ord(edge[0])-97
        d=ord(edge[1])-97
        adj_mat[s][d]=edge[2]
        adj_mat[d][s]=edge[2]
    print("")
    for row