class Solution:
    """
    @param: n: An integer
    @return: how much money you need to have to guarantee a win
    """
    def getMoneyAmount(self, n):
        # write your code here
        self.dp = []
        for _ in range(n+1):
            self.dp.append([-1 for _ in range(n+1)])
        return self.fun(1, n)
        
    def fun(self, left, right):
        #print left, right
        if self.dp[left][right]!= -1:
            return self.dp[left][right]
            
        if left + 1 == right:
            self.dp[left][right] = left
            return left
        if left == right:
            self.dp[left][right] = 0
            return 0
        
        l = sys.maxint
        r = sys.maxint
        result = sys.maxint
        for mid in range(left, right):
            l = self.fun(left, mid-1)
            r = self.fun(mid + 1, right)
            result = min(result, mid + max(l, r))
        
        self.dp[left][right] = result
        return result
