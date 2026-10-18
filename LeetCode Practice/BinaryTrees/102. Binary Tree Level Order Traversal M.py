from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        # approach: queue - FIFO; pop from left and add their children to queue
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            
            # we need to know the length of the queue 'cause nodes will be continuely added to the queue
            layer = []

            for _ in range(len(queue)):

                node = queue.popleft()
                layer.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(layer)

        return res

# o(n)
# O(n)