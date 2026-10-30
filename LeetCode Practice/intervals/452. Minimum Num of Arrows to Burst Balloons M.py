from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # approach:greedy+sort intervals
        # greedy: when the next interval's start is bigger than "last_end", we add an arrow

        points.sort(key=lambda x:x[1])
        last_end = points[0][1]
        arrow = 1 # we must have 1 arrow

        for start, end in points[1:]:

            if start > last_end:
                arrow += 1
                last_end = end

        return arrow

# TC:O(n log n) sorting by the end
# SC:O(n) sort() with a key function builds a temporary list of keys, the rest is O(1)
