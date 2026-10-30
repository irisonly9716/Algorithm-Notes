from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # approach:greedy - we need to remove intervals as big as we can

        # 尽量留下范围小的intervals 所以按照end排序 这样在越后面的越可能是范围更大的interval
        # 因为end排序的话 越是后面的end越大，start的范围也会更大 更可能是小的start+大的end的组合

        intervals.sort(key=lambda x:x[1])

        last_end = intervals[0][1] # 维护一个last end 如果有合理的就更新 没有last_end是错误的 
        count = 0

        for start, end in intervals[1:]:

            if start < last_end:

                count += 1

            else:
                last_end = end # 被删掉的不能更新last_end


        return count

    # 为什么不可以不记录lastend而去直接和上一个区间比较？
    # 关键在于：被删掉的区间已经不存在了，不能再拿它的 end 去和后面的区间比较。
    # last_end 记录的是最后一个保留下来的区间的 end，而不是"上一个区间"的 end。

# TC:O(n log n) sorting by the end
# SC:O(n) sort() with a key function builds a temporary list of keys, the rest is O(1)
