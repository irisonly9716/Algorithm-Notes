from collections import Counter

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        
        # approach: just use TwoSum approach, we need 1 hashmap to record the frequency of results of num1 and num2 using double loops
        ans = 0
        res_counter = Counter()

        for num1 in nums1:
            for num2 in nums2:
                res_counter[num1 + num2] += 1

        for num3 in nums3:
            for num4 in nums4:
                # the number of results == -(num3 + num4) in the counter is the number of possible combinations those sum up to 0
                if res_counter[-(num3 + num4)] != 0: # this line can be deleted
                    ans += res_counter[-(num3 + num4)]

        return ans

# TC:O(n**2)
# SC:O(n**2)