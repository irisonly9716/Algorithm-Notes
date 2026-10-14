# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        
        # approach:iteration
        # dynamically record the mode (value and frequence) in in-order traversal

        if not root:
            return []

        res = []
        stack = []
        curr = root
        curr_streak = 0
        max_streak = 0
        prev = None

        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()

            # ⭐deal with curr_streak at first
            if prev == None or (prev != None and node.val == prev.val):
                curr_streak += 1
            elif (prev != None and node.val != prev.val):
                curr_streak = 1

            if curr_streak > max_streak:
                max_streak = curr_streak
                res = [node.val] # discard all previous records
            elif curr_streak == max_streak:
                res.append(node.val)

            prev = node
            curr = node.right

        return res

