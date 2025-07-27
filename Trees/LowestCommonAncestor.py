# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Base case: if root is None or root is p or q
    if root is None or root == p or root == q:
        return root
    
    # Search in left subtree
    left = lowestCommonAncestor(root.left, p, q)
    # Search in right subtree
    right = lowestCommonAncestor(root.right, p, q)
    
    # If p and q found in left and right subtree of current node,
    # then current node is their LCA
    if left and right:
        return root
    
    # Otherwise, return the non-null child (either left or right)
    return left if left else right
