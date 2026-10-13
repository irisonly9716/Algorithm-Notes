from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        

        # approach:post-order traversal
        # we need to know the depth of each node
        # record the answer each time we firstly reach the deepest depth

        self.max_depth = 0
        self.leftmost = root.val # root.val is the default

        def preorder(node, depth) -> None:

            if not node:
                return

            if depth > self.max_depth:
                self.max_depth = depth
                self.leftmost = node.val

            preorder(node.left, depth + 1)
            preorder(node.right, depth + 1)

        preorder(root, 0)

        return self.leftmost
