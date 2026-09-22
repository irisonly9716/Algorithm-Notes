class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        # approach:use a set to store all appearing num in nums1. check if elements in nums2 are in the set.

        num_set = set(nums1)

        ans = set()
        for num in nums2:
            if num in num_set:
                ans.add(num)

        return list(ans)

# TC:O(n+m)
# SC:O(n) n is the length of nums1