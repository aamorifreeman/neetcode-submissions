"""
buy - r pointer = 0
sell - l pointer = 1
max_profit = 0

for r in range(len(nums)):
    curr_profit = sell - buy
    if curr_profit less than or equal 0:
        buy += 1
    else: curr_profit greater than 0
        max_profit = max(max_profit, curr_profit)
return max_profit

        
        
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        max_profit = 0

        for sell in range(len(prices)):
            curr_profit = prices[sell] - prices[buy]
            if curr_profit <= 0:
                buy = sell
            else:
                max_profit = max(max_profit, curr_profit)
        return max_profit


        



        