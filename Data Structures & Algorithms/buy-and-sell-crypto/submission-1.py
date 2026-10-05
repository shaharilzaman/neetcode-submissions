class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        currbuy = prices[0]
        for i in prices:
            if i < currbuy:
                currbuy = i
            else:
                profit = max(profit, i - currbuy)
        return profit 