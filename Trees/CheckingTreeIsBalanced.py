class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_height(node):
            if not node:
                return 0  # height of empty tree is 0

            left = check_height(node.left)
            if left == -1:
                return -1  # left subtree is not balanced

            right = check_height(node.right)
            if right == -1:
                return -1  # right subtree is not balanced

            if abs(left - right) > 1:
                return -1  # current node not balanced

            return max(left, right) + 1  # return height

        return check_height(root) != -1
