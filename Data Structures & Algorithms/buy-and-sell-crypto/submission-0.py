class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currbuy = prices[0]
        profit = 0
        for i in prices:
            if currbuy > i:
                currbuy = i
            elif i - currbuy > profit:
                profit = i - currbuy 
        return profit