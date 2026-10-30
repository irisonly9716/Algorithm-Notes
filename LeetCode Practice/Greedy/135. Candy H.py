from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:

        # approach: greedy
        # iterate 2 times. front to end and end to front 
        # first iteration: each child has 1 candy at least, if the next one is greater, ⭐candy[i-1] + 1
        # second iteration: if the previous one is greater, check if the previous candy is bigger, if not, candy[j+1] +1

        n = len(ratings)
        candy = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i-1] + 1

        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j + 1] and candy[j] <= candy[j + 1]:
                candy[j] = candy[j+1] + 1 # ⭐ must greater than candy[j+1], not just +1


        return sum(candy)



# TC:O(n)
# SC:O(n) the candy list
