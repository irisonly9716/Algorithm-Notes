class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        
        # approach: greedy 
        # each time we met a wiggle, we count 1
        # we update prediff only when we encounter a wiggle.
        n = len(nums)
        if n <= 1:
            return n

        count = 1
        prediff = 0
        currdiff = 0
        
        for i in range(n - 1):

            currdiff = nums[i + 1] - nums[i]

            # if find a wiggle ⭐<= and >= is important, because we need to skip the same number
            # we update prediff only when the pair of currdiff is a wiggle
            if (prediff <= 0 and currdiff > 0) or (prediff >= 0 and currdiff < 0):
                prediff = currdiff
                count += 1

        return count


# O(n)
# O(1)



