class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        l, r = 0, 1
        n = len(prices)
        while l < n:
            while r < n:
                profit = prices[r] - prices[l]
                maxprofit = max(profit, maxprofit)
                r += 1
            l += 1
            r = l
        return maxprofit
        