# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:

        # approach1: monotonic stack
        # keep elements in stack descending
        # if the curr num is smaller than top element, link as top element's right child
        # if bigger, pop all elements smaller than curr, the last one is the curr.left


        stack = []

        for num in nums:

            node = TreeNode(num)
            last = None

            # keep the stack descending
            while stack and num > stack[-1].val:
                
                # record last node, it should be curr's left child
                last = stack.pop()

            if last:
                node.left = last

            if stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0] if stack else None

        # O(n)
        # O(n)
        


        
        '''
        # approach2:pre-order traversal, find the max num during recursion.

        index_dict = {num:index for index,num in enumerate(nums)}

        def build(left:int, right:int) -> TreeNode | None:

            if left > right:
                return None

            val = max(nums[left:right + 1])
            new = TreeNode(val)
            index = index_dict[val]

            new.left = build(left, index - 1)
            new.right = build(index + 1, right)

            return new


        return build(0, len(nums) - 1)

    # 平均情况：O(n log n)，类似快排的划分
    # 最坏情况：O(n²)，例如数组单调递增或递减时，每次只能剥掉一个元素
    # 空间：切片 nums[left:right+1] 每次都会复制出一个新列表，有额外开销；最坏递归深度为 O(n)
    '''