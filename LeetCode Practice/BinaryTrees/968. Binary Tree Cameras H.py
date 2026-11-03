from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        # approach:greedy, only when parents and children are not camera, we set a camera
        # 0 = not monitored 1 = camera 2 = monitored

        self.camera = 0

        def dfs(node) -> int:

            # if not node, we see it as monitored (because no camera needed)
            if not node:
                return 2

            # post-order iteration
            left = dfs(node.left)
            right = dfs(node.right)

            # if children are all monitored, curr node is not
            if left == 2 and right == 2:
                return 0

            # if left/right is not monitored, curr node should be a camera
            if left == 0 or right == 0:
                self.camera += 1
                return 1

            # if one of children is camera, curr node is monitored
            if left == 1 or right == 1:
                return 2
            
        # ⭐edge case: when we have at least one node and no camera, this root should be camera
        if root and dfs(root) == 0:
            self.camera += 1
        return self.camera

# TC:O(n) every node is visited once
# SC:O(h) the recursion stack, O(n) when the tree is skewed
