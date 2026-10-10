# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        
        # we can't just use min(left + 1, right + 1) because it will give us a definite 0
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0:
            return right + 1

        if right == 0:
            return left + 1

        return min(left + 1, right + 1)
