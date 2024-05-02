class Node:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None

def rightview(root, level, maxroot):
    if root == None:
        return 
    if level > maxroot[0]:
        print(root.data)
        maxroot[0] = level
    rightview(root.rc, level + 1, maxroot)
    rightview(root.lc, level + 1, maxroot)

def rightview1(root):
    maxroot = [0]
    rightview(root, 1, maxroot)
    
root = Node(1)
root.lc = Node(2)
root.rc = Node(3)
root.lc.lc = Node(4)
root.lc.rc = Node(5)
root.rc.lc = Node(6)
root.rc.rc = Node(7)
root.rc.lc.rc = Node(8)
 
rightview(root)
# class Node:
#     # A constructor to create a new Binary tree Node
#     def __init__(self, item):
#         self.data = item
#         self.left = None
#         self.right = None
 
# # Recursive function to print right view of Binary Tree
# # used max_level as reference list ..only max_level[0]
# # is helpful to us
 
 
# def rightViewUtil(root, level, max_level):
 
#     # Base Case
#     if root is None:
#         return
 
#     # If this is the last node of its level
#     if (max_level[0] < level):
#         print(root.data),
#         max_level[0] = level
 
#     # Recur for right subtree first, then left subtree
#     rightViewUtil(root.right, level+1, max_level)
#     rightViewUtil(root.left, level+1, max_level)
 
 
# def rightView(root):
#     max_level = [0]
#     rightViewUtil(root, 1, max_level)
 
 
# Driver program to test above function
