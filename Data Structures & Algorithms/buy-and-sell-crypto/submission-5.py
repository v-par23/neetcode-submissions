class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                price = prices[r] - prices[l]
                maxPrice = max(maxPrice, price)
                
            else:
                l = r
            r += 1

        return maxPrice

            


