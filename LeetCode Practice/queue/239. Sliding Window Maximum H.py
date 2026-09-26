from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # approach: monotonic queue
        # keep the queue a valid window for k size and desending so that we can find
        # the largest num in the head of the queue. -> O(n) 

        queue = [] # stors indexes, use indexes to find the num
        res = []

        for index, num in enumerate(nums):

            while queue and num > nums[queue[-1]]:
                queue.pop()

            queue.append(index)

            # check if the head of queue is stale
            while queue[0] >= index - k:
                queue.popleft()

            # check if index >= k otherwise no valid window:
            if index >= k:
                res.append(queue[0])

        return res
