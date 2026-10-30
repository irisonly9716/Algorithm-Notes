# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        
        # approach1: recursion but easier based on the nature of a BST

        if not root:
            return None

        if root.val == val:
            return root 

        return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)
        # TC:O(h) h is the height of the tree, we only go down one path
        # SC:O(h) the recursion stack, O(1) if written iteratively



        '''
        # approach2:recursion in-order traversal always applies to a BST.
        if not root:
            return None

        left = self.searchBST(root.left, val)
        if left:
            return left
            

        if root.val == val:
            return root

        right = self.searchBST(root.right, val)
        if right:
            return right


        return None
        '''

        