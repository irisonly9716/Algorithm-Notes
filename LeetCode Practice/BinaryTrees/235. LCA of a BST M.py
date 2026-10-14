# Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # approach: one-way traversal
        # ⭐this is a BST, when we first encounter a node between p and q, the node is the LCA

        if not root:
            return None

        node = root

        while node:
            if q.val < node.val and p.val < node.val:
                node = node.left
            elif q.val > node.val and p.val > node.val:
                node = node.right

            else:
                return node


        return None

# O(h), O(1)