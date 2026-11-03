class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        # approach: monotonic stack
        # find the next greater element for elements. 
        # position in nums1, next greater in nums2
        # we need a dict to know the index of elements in nums1, referring to nums2

        m = len(nums1)
        res = [-1] * m

        index_dict = {num:index for index, num in enumerate(nums1)}
        stack = [] # num, DESC

        for index, num in enumerate(nums2):
            while stack and stack[-1] < num:
                curr_num = stack.pop() # the current num that should be record [next greater element].
                curr_index = index_dict[curr_num] # the index in res array(also the index in nums1)
                res[curr_index] = num # num is the next greater element in nums2

            # ⭐：check if num in index_dict, nums1 is the subset of nums2, elements in
            # nums2 may not in nums1
            if num in index_dict:
                stack.append(num)

        return res

# TC:O(m + n) m = len(nums1), n = len(nums2); every element is pushed and popped at most once
# SC:O(m) the dict and the stack, not counting the result
