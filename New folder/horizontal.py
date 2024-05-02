# class TreeNode:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None

# def horizontal_traversal(root):
#     if not root:
#         return []

#     result = []
#     queue = [(root, 0)]  # Store the node and its horizontal distance from the root

#     while queue:
#         node, hd = queue.pop(0)
#         if hd == len(result):
#             result.append([node.val])
#         else:
#             result[hd].append(node.val)

#         if node.left:
#             queue.append((node.left, hd + 1))
#         if node.right:
#             queue.append((node.right, hd + 1))

#     return result

# # Example usage:
# # Create a tree
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

# # Perform horizontal traversal
# print(horizontal_traversal(root))
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.hd = 0

def vertical_map(root):
    vertical_map = {}
    queue = [(root, 0)]
    while queue:
        node, hd = queue.pop(0)
        if hd not in vertical_map:
            vertical_map[hd] = []
        vertical_map[hd].append(node.data)
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    print("\nVertical Order Traversal:")
    for hd in sorted(vertical_map):
        print(vertical_map[hd], end=" ")

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

vertical_map(root)
