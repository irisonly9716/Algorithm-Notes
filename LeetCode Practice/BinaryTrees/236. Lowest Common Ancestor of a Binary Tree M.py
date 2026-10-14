# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # approach:post-order traversal, backtracking-likely
        # we can only use this approach when p and q are 100% in the tree
        
        if not root:
            return None

        # if root is q or q, just return root, because the other one is root's child
        if root.val == q.val or root.val == p.val:
            return root

        # we need to know the children first
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # ⭐if we have both left and right, the root is the LCA
        if left and right:
            return root

        if left:
            return left
        
        if right:
            return right

        if not left and not right:
            return None



# 为什么左右都非空时 root 就是 LCA?
# root 是公共祖先：p 和 q 是树中两个不同的节点，各自只出现一次。左边至少有一个，右边至少有一个，那只能是一个在左、一个在右。root 同时是左右子树所有节点的祖先，所以它是 p 和 q 的公共祖先。
# root 是最低的：比 root 更低的任何节点，要么整个在左子树里，要么整个在右子树里，不可能同时包含左边的那个和右边的那个。所以没有比 root 更低的公共祖先。

