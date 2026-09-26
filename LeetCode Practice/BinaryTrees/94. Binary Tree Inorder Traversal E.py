# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        
        # approach1: recursion, operating the current node in the middle
        # inorder: left, node, right
        res = []

        def inorder(node:TreeNode | None) -> None:

            if not node:
                return

            inorder(node.left)

            res.append(node.val)

            inorder(node.right)

        inorder(root)

        return res 


'''
        # approach2:iteration with stack
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:     

        if not root:
            return []   

        stack = []
        res = []
        node = root

        while stack or node:

            # append node from middle to the very left
            while node:
                stack.append(node)
                node = node.left

            # pop from the very left and add it to the results
            node = stack.pop()
            res.append(node.val)

            # turn to the right in the end
            node = node.right

        return res

# TC:O(n)
# SC:O(n) no risk of stack overflow due to the recursion.          
'''

