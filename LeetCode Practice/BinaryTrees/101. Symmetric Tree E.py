# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        
        # pre-order traversal and see if every pair of right&left is the same

        # an empty tree is symmetric
        if not root:
            return True

        def preorder(left, right) -> bool:

            if not left and not right:
                return True

            if not left or not right:
                return False
            
            if left.val != right.val:
                return False

            if preorder(left.left, right.right) and preorder(left.right, right.left):
                return True

            return False


        return preorder(root.left, root.right)

# TC:O(n) every pair of nodes is compared once
# SC:O(h) h is the height of the tree (the recursion stack), O(n) when the tree is skewed
