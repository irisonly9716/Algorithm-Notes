# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        
        # approach: one-way traversal in a BST, when we find the node, we should link its 
        # existing subtrees to the its parent node. Need to consider all 3 situations.

        if not root:
            return None

        # ⭐link the modified subtrees and return the node
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        # we found the node, link its subtrees and return or return the existing subtree
        # 3 situations
        else: 
        
            left = root.left
            right = root.right

            # 1. no subtrees, just return None
            if not left and not right:
                return None

            # 2. go to the left leaf of root.right and link root.left to the leaf.left
            if left and right:
                
                curr = right
                while curr.left:
                    curr = curr.left
                curr.left = left

                return right

            # 3. one subtree, just skip the current node and return the one.
            return left if left else right

# TC:O(h) h is the height of the tree: one path down to the key, and one more down the left side of its right subtree
# SC:O(h) the recursion stack
