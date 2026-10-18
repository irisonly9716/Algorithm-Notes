# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        # approach: pre-order traversal without a path.
        # is any sum(root to leaf) == target?

        if not root:
            return False

        def dfs(node, curr_sum) -> bool:

            # if node is a leaf and curr_sum == targetSum, return True
            if not node.left and not node.right and curr_sum == targetSum:
                return True
     
            left = node.left and dfs(node.left, curr_sum + node.left.val)

            right = node.right and dfs(node.right, curr_sum + node.right.val)

            # ⭐should add bool() otherwise when it's false it will only return null
            return bool(right or left)


        return dfs(root, root.val)
