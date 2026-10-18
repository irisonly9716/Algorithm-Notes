from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # approach: iterate from bigger values to smaller values
        # order: right - mid - left

        if not root:
            return None

        stack = []
        curr_sum = 0
        curr = root

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.right

            # deal with the curr node
            node = stack.pop()
            val = node.val # ⭐ be aware of math
            node.val += curr_sum
            curr_sum += val

            curr = node.left

        return root

