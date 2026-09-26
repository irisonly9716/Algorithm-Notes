from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # approach: monotonic queue
        # keep the queue a valid window for k size and descending so that we can find
        # the largest num in the head of the queue. -> O(n) 

        queue = deque() # stores indexes, use indexes to find the num
        res = []

        for index, num in enumerate(nums):

            while queue and num > nums[queue[-1]]:
                queue.pop()

            queue.append(index)

            # check if the head of queue is stale: index - k is already out of the window
            while queue and queue[0] <= index - k:
                queue.popleft()

            # the first full window ends at index k - 1, before that there is no valid window.
            if index >= k - 1:
                res.append(nums[queue[0]]) # the head of the queue is the index of the max num

        return res
