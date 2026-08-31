class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minAtI = []
        minPrice = prices[0] 

        for i in range(len(prices)):
            minPrice = min(prices[i],minPrice)
            profit = max(profit, prices[i] - minPrice)
        return profit

        