# from collections import defaultdict, deque

# class TreeNode:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None

# def vertical_order_traversal(root):
#     if not root:
#         return []

#     column_table = defaultdict(list)
#     queue = deque([(root, 0)])

#     while queue:
#         node, column = queue.popleft()

#         if node:
#             column_table[column].append(node.val)
#             queue.append((node.left, column - 1))
#             queue.append((node.right, column + 1))

#     sorted_columns = sorted(column_table.keys())
#     result = [column_table[column] for column in sorted_columns]
#     return result

# # Create a balanced binary tree with 15 nodes
# root = TreeNode('A')
# root.left = TreeNode('B')
# root.right = TreeNode('C')
# root.left.left = TreeNode('D')
# root.left.right = TreeNode('E')
# root.right.left = TreeNode('F')
# root.right.right = TreeNode('G')
# root.left.left.left = TreeNode('H')
# root.left.left.right = TreeNode('I')
# root.left.right.left = TreeNode('J')
# root.left.right.right = TreeNode('K')
# root.right.left.left = TreeNode('L')
# root.right.left.right = TreeNode('M')
# root.right.right.left = TreeNode('N')
# root.right.right.right = TreeNode('O')

# # Perform vertical order traversal
# print(vertical_order_traversal(root))
class Node:
    def __init__(self,data):
        self.lc=None
        self.rc=None
        self.data=data
        self.hd=0





root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')
root.left.left.left = Node('H')
root.left.left.right = Node('I')
root.left.right.left = Node('J')
root.left.right.right = Node('K')
root.right.left.left = Node('L')
root.right.left.right = Node('M')
root.right.right.left = Node('N')
root.right.right.right = Node('O')
    