class Solution:
    """
    @param k: an integer
    @param prices: a list of integer
    @return: an integer which is maximum profit
    """
    def maxProfit(self, k, prices):
        # write your code here
        # mustsell[i][j]: maximum value(ith day, must tranction).
        # global_profile[i][j]: maximum value(ith day)
        # Function 1: mustsell[i][j] = max(global_profile[i-1][j-1] + diff,
        #                                mustsell[i - 1][j - 1] + diff,
        #                                mustsell[i-1][j] + diff)
        # Function 2: global_profile[i][j] = max(mustsell[i][j], global_profile[i-1][j])
        # initialization: mustsell[0...i][0] = 0
        #                 global_profile[0...i][0] = 0
        #                 mustsell[0/1][0...i] = 0
        #                 global_profile[0/1][0....i] = 0
        # answer: global_profile[-1][-1]
        if k >= (len(prices) + 1) / 2:
            tmp = 0
            for i in range(1, len(prices)):
                tmp +=max(prices[i] - prices[i - 1], 0)
            return tmp
        
        
        must_sell = [[0] * (k + 1) for _ in range(len(prices) + 1)]
        profit = [[0] * (k + 1) for _ in range(len(prices) + 1) ]
        
        days = len(prices)
        
        for day in range(2, days + 1):
            diff = prices[day - 1] - prices[day - 2]
            for j in range(1, k + 1):
                must_sell[day][j] = max(profit[day - 1][j - 1] + diff, 
                            must_sell[day - 1][j - 1] + diff,
                            must_sell[day - 1][j] + diff)
                profit[day][j] = max(profit[day - 1][j], must_sell[day][j])
                
        return profit[-1][-1]
