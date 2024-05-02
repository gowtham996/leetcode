class Node:
    def __init__(self, d):
        self.lc = None
        self.rc = None
        self.d = d
        self.hd = 0
    
    
    def construct_tree(nodelist):
        root = Node(nodelist[1])
        root.lc = Node(nodelist[2])
        root.rc = Node(nodelist[3])
        root.lc.lc = Node(nodelist[4])
        root.lc.rc = Node(nodelist[5])
        root.rc.lc = Node(nodelist[6])
        root.rc.rc = Node(nodelist[7])
        return root
    
    
    def top_view(root):
        if root is None:
            return
        m = {}
        q = [(root, 0)]
        while q:
            curr_node, hd = q.pop(0)
            if hd not in m:
                m[hd] = curr_node.d
            if curr_node.lc:
                q.append((curr_node.lc, hd - 1))
            if curr_node.rc:
                q.append((curr_node.rc, hd + 1))
        
        for key in sorted(m.keys()):
            print(m[key], end=' ')
    
    
    def bottom_view(root):
        if root is None:
            return
        m = {}
        q = [(root, 0)]
        while q:
            curr_node, hd = q.pop(0)
            m[hd] = curr_node.d
            if curr_node.lc:
                q.append((curr_node.lc, hd - 1))
            if curr_node.rc:
                q.append((curr_node.rc, hd + 1))
        
        for key in sorted(m.keys()):
            print(m[key], end=' ')

# Define node values as a list
nodelist =[None, 1, 2, 3, 4, 5, 6, 7]  # Adding None as index 0 for convenience

# Construct the tree
root = Node.construct_tree(nodelist)

# Print the top view of the tree
print("Top view of the tree:")
Node.top_view(root)

# Print the bottom view of the tree
print("\nBottom view of the tree:")
Node.bottom_view(root)



#BOTTOM VIEW OF TREE
# class Node:
#     def __init__(self, d):
#         self.lc = None
#         self.rc = None
#         self.d = d
#         self.hd = 0

#     @staticmethod
#     def constructtree(nodelist):
#         root = Node(nodelist[0])
#         root.lc = Node(nodelist[1])
#         root.rc = Node(nodelist[2])
#         root.lc.lc = Node(nodelist[3])
#         root.lc.rc = Node(nodelist[4])
#         root.rc.lc = Node(nodelist[5])
#         root.rc.rc = Node(nodelist[6])
#         return root

#     @staticmethod
#     def bottomview(root):
#         if not root:
#             return
        
#         m = {}
#         q = []
#         q.append(root)

#         while len(q) > 0:
#             currnode = q.pop(0)
#             # Always update the dictionary value for the horizontal distance
#             m[currnode.hd] = currnode.d
#             if currnode.lc:
#                 currnode.lc.hd = currnode.hd - 1
#                 q.append(currnode.lc)
#             if currnode.rc:
#                 currnode.rc.hd = currnode.hd + 1
#                 q.append(currnode.rc)
        
#         # Since we want the bottom view, we will print the values in sorted order of horizontal distance
#         # This way, the nodes with the same horizontal distance will be printed in the order from left to right
#         for key in sorted(m.keys()):
#             print(m[key], end=' ')

# # Example usage:
# nodelist = [1, 2, 3, 4, 5, 6, 7]
# root = Node.constructtree(nodelist)
# Node.bottomview(root)
