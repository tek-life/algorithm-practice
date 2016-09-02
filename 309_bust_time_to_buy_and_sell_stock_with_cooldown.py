class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0

        max_buy=-prices[0]
        i=1
        last_sell=max_sell=0
        
        while i<len(prices):
            temp_sell=(max_buy+prices[i])
            
            if i==1:
                if -prices[i] > max_buy:
                    max_buy=-prices[i]
            else:
                tmp=max_sell-prices[i]
                if tmp>max_buy:
                    max_buy=tmp
            
            if last_sell>max_sell:
                max_sell=last_sell
            last_sell=temp_sell
            
            i+=1

        return max(last_sell,max_sell)
