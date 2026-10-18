# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        
        # approach: build the tree from top to bottom. ⭐mid =  left + (right-left) // 2

        def build(left:int, right:int) -> TreeNode | None:

            if left > right:
                return None

            mid = left + (right - left) // 2
            val = nums[mid]
            new = TreeNode(val)

            new.left = build(left, mid - 1)
            new.right = build(mid + 1, right)

            return new

        return build(0, len(nums) - 1)

        