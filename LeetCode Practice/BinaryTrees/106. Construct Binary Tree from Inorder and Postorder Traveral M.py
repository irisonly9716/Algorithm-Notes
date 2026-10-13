from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:


        in_dict = {val:index for index, val in enumerate(inorder)}
        self.post_index = len(postorder) - 1

        # the parameters will be the current left/right bound of need-to-build array
        def build(left, right) -> Optional[TreeNode]:

            if left > right:
                return None

            val = postorder[self.post_index]
            self.post_index -= 1

            new = TreeNode(val)
            curr_index = in_dict[val]

            # ⭐postorder! we need to build right side first
            new.right = build(curr_index + 1, right)
            new.left = build(left, curr_index - 1)

            return new

        return build(0, len(postorder) - 1)
            