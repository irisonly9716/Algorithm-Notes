from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # approach: greedy - sort the intervals by left end, make each interval closer

        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x:x[0])
        
        res = [intervals[0]]

        for start, end in intervals[1:]:

            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])

        return res

# TC:O(n log n) sorting by the left end
# SC:O(n) the sort key list and the result
