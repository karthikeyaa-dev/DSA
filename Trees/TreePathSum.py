class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    if not root:
        return False

    # If it's a leaf node
    if not root.left and not root.right:
        return root.val == targetSum

    # Recurse left and right
    remaining = targetSum - root.val
    return hasPathSum(root.left, remaining) or hasPathSum(root.right, remaining)
