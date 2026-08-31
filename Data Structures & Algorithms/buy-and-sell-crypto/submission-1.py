class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minAtI = []
        minPrice = prices[0] 
        for i in range(len(prices)):
            minPrice = min(prices[i],minPrice)
            minAtI.append(minPrice)

        for i in range(len(prices)):
            profit = max(profit, prices[i] - minAtI[i])
        return profit

        