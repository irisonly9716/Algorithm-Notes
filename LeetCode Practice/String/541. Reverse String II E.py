class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        # approach:two pointers. reverse the string by group.
        str_list = list(s)
        n = len(s)
        
        
        def reverse(left:int, right:int) -> None:

            while left < right:
                str_list[left], str_list[right] = str_list[right], str_list[left]
                left += 1
                right -= 1

        
        index = 0
        while index < n:
            # reverse first k chars for every 2k chars
            # min() is important in here, ensuring indexes will not exceed
            right = min(index + k - 1, n - 1)
            reverse(index, right)
            index += 2 * k 

        return ''.join(str_list)

# TC:O(n)
# SC:O(n)


# return "".join(s[i:i+k][::-1] + s[i+k:i+2*k] for i in range(0, len(s), 2*k))