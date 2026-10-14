from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # approach1:recursion
        # in-order traversal, record the prev and compare with the curr node.val

        self.prev = None

        if not root:
            return True

        def inorder(node) -> bool:

            if not node:
                return True

            if not inorder(node.left):
                return False

            if self.prev != None and node.val <= self.prev.val:
                return False

            self.prev = node

            return inorder(node.right)
            
        return inorder(root)



        '''
        # approach2: iteration
        # in-order traversal, compare val with prev val
        prev = None

        stack = []
        curr = root

        while stack or curr:

            # go left to the leaf node
            while curr:
                stack.append(curr)
                curr = curr.left

            # pop the node, compare, go to right node
            curr = stack.pop()
            if prev != None and curr.val <= prev.val:
                return False
            
            prev = curr

            curr = curr.right # if no curr.right, stack will pop a node or stop while loop

            
        return True
        '''