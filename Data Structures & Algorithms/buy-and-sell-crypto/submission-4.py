class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 #max profit
        minBuy = prices[0] #lowest buy

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
        
        