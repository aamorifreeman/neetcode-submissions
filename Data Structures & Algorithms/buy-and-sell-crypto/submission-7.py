class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        b = 0
        max_profit = 0
        for s in range(1, len(prices)):
            if (prices[s] - prices[b]) <= 0:
                b = s
            else:
                max_profit = max(max_profit, prices[s] - prices[b])
        return max_profit

        # b = 0
        # s = 1
        # max_profit = 0

        # while(s < len(prices)):
        #     if (prices[s] - prices[b]) <= 0:
        #         b = s
        #     else:
        #         max_profit = max(max_profit, prices[s] - prices[b])
        #     s+=1
        # return max_profit

        


        



        