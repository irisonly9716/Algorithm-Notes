from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # post-order traversal, we need to know whether child trees are valid
        # balanced binary tree is height-balanced, the difference of height should only be 0~1.


        # if the diff > 1: return -1
        def height(node) -> int:

            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            if left == -1 or right == -1:
                return -1

            if abs(right - left) > 1:
                return -1

            return 1 + max(right, left)

        diff = height(root)

        return False if diff == -1 else True


