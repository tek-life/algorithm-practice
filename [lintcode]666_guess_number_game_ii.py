class Solution:
    """
    @param: n: An integer
    @return: how much money you need to have to guarantee a win
    """
    def getMoneyAmount(self, n):
        # write your code here
        #dp[i,j] = min(k+max(dp[i,k-1],dp[k+1, j])), i<k<j 
        dp = []
        
        for _ in range(n+1):
            dp.append([-1 for _ in range(n+1)])
        
        for i in range(0, n, 1):
            dp[i][i] = 0
            dp[i][i+1] = i
        dp[-1][-1] = 0
        
        for i in xrange(n, 0, -1):
            for j in xrange(i+2, n+1, 1):
                val = sys.maxint
                for k in xrange(i+1,j):
                    val = min(val, k+max(dp[i][k-1], dp[k+1][j]))
                if val != sys.maxint:
                    dp[i][j] = val
        return dp[1][-1]
