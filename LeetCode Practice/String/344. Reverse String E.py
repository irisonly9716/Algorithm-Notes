class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # approach: two pointers
        n = len(s)
        if n <= 1:
            return

        left = 0
        right = n - 1

        # when left == right in the middle, we don't need to switch the single letter
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        
# TC:O(n)
# SC:O(1)