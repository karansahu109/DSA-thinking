class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r]- prices[l])
            else:
                l = r
            r += 1
        return maxP

        # profit = 0
        # minAtI = []
        # minPrice = prices[0] 

        # for i in range(len(prices)):
        #     minPrice = min(prices[i],minPrice)
        #     profit = max(profit, prices[i] - minPrice)
        # return profit

        