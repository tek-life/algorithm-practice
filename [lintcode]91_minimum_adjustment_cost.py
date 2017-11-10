class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        #dp[i][j] = abs(A[i]-target) + min(dp[i-1][start...end]) start = j - target, end =j+ target
        #dp[0...length][0....100]
        if not A:
            return 0
        dp = []
        length = len(A)
        for _ in range(0, length+1):
            dp.append([sys.maxint for _ in range(101)])
            
        for i in range(101):
            dp[0][i] = 0
            
        for i in range(1, length+1):
            for j in range(0, 101):
                start = j - target
                end = j + target
                if start < 0:
                    start = 0
                if end > 100:
                    end = 100
                val = min(dp[i-1][start:end+1])
                
                dp[i][j] = abs(j - A[i-1]) + val
                
        return min(dp[-1])
