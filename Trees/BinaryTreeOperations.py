from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Insert into Binary Tree (Level Order)
def insert(root, val):
    if not root:
        return TreeNode(val)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if not node.left:
            node.left = TreeNode(val)
            return root
        else:
            queue.append(node.left)
        if not node.right:
            node.right = TreeNode(val)
            return root
        else:
            queue.append(node.right)

# Inorder Traversal (Left → Root → Right)
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# Preorder Traversal (Root → Left → Right)
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

# Postorder Traversal (Left → Right → Root)
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# Level Order Traversal (BFS)
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Example Usage
if __name__ == "__main__":
    root = TreeNode(1)
    insert(root, 2)
    insert(root, 3)
    insert(root, 4)
    insert(root, 5)

    print("Inorder Traversal:", inorder(root))
    print("Preorder Traversal:", preorder(root))
    print("Postorder Traversal:", postorder(root))
    print("Level Order Traversal:", level_order(root))
