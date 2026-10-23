class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # approach: greedy
        # each day we can only buy OR sell stocks
        # we can only hold 1 stock at the same time
        # only collect profit (positive diff between adjecent prices)

        profit = 0

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit += diff

        return profit
            