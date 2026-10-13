# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        
        if not root or (not root.left and not root.right):
            return 0

        stack = [root]
        value = 0

        # pre-order traversal (mid left right), push right child first
        # the order of traversal does not matter, the point is to validate the left leaf
        while stack:

            node = stack.pop()

            # validate if node.left is a left leaf.
            if node.left and not node.left.left and not node.left.right:
                value += node.left.val

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return value
