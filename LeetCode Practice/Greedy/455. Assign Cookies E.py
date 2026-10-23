class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:

        # approach: greedy
        # use max s[i] to fix the most greedy child

        s.sort(reverse=True)
        g.sort(reverse=True)

        count = 0
        i = 0
        j = 0

        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                count += 1
                i += 1
                j += 1

            else:
                j += 1

        return count

# O(n log n)
# O(1)