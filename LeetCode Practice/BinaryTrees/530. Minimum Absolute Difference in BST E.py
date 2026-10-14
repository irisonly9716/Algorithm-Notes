from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        # approach:iteration using a stack

        stack = []
        curr = root

        min_abs = float('inf')
        prev = None

        while stack or curr:

            # push all the way down through the left path
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()
            if prev != None and (node.val - prev.val) < min_abs: # prev is smaller
                min_abs = (node.val - prev.val)
            prev = node

            curr = node.right

        return min_abs

            
