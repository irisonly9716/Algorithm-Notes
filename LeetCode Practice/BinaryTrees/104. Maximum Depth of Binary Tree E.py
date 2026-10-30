# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        
        # post-order traversal
        if not root:
            return 0

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)

# TC:O(n)
# SC:O(h) h is the height of the tree (the recursion stack), O(n) when the tree is skewed
