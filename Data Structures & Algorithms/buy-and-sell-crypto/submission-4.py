class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            currP = 0
            if prices[l] >= prices[r]:
                l = r
            else:
                currP = prices[r] - prices[l]
            maxP = max(maxP, currP)
            r += 1
        return maxP

            


