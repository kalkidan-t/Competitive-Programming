class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyP, sellP = 0, 1
        maxP = 0
        while sellP < len(prices):
            if prices[sellP] > prices[buyP]:
                profit = prices[sellP] - prices[buyP]
                maxP = max(maxP, profit)
            else:
                buyP = sellP
            sellP += 1
        return maxP
        