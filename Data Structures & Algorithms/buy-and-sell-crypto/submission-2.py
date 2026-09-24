class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            currPrice = 0
            if prices[l] < prices[r]:
                currPrice = prices[r] - prices[l]
                maxP = max(maxP, currPrice)
            else:
                l = r
            r += 1
        return maxP
            


