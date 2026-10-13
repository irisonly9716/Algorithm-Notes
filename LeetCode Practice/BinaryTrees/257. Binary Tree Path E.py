from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
   
        # dfs find all paths from root to leaf
        if not root:
            return []

        res = []
        path = [str(root.val)] # add root first

        def findpath(node) -> None:

            # if this node is a leaf node: record
            if not node.left and not node.right:
                res.append("->".join(path)) # must have str in the path
                return

            if node.left:
                path.append(str(node.left.val))
                findpath(node.left)
                path.pop()

            if node.right:
                path.append(str(node.right.val))
                findpath(node.right)
                path.pop()

        findpath(root)

        return res