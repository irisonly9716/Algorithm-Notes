from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # approach: greedy
        # we need to know the last appear of each letter
        # each time we update the "end" index, if the end == index, we reached a border.

        last = {}
        for index, char in enumerate(s):
            last[char] = index

        res = []
        start = 0
        end = 0

        for index, char in enumerate(s):

            end = max(end, last[char])
            if end == index:
                res.append(end - start + 1)
                start = index + 1

        return res

# TC:O(n)
# SC:O(1) the dict holds at most 26 lowercase letters, not counting the output
