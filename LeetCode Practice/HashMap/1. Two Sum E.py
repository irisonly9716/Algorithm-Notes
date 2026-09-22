from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # the best approach: hashmap = {[num:index], [...]}. we encounter a element, we check if diff = target-element is in the hashmap, if so, return[current index, hashmap[diff]]
        # other approaches: 1. double loop.O(n**2) 2. sort + two pointers O(n log n + n)

        index_dict = {}

        for index, num in enumerate(nums):

            diff = target - num
            if diff in index_dict:
                return [index, index_dict[diff]]

            else:
                index_dict[num] = index


        
# TC:O(n)
# SC:O(n)

