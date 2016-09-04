class Solution(object):
    DP=[0,]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #nums=[x**2 for x in range(1,int(n**0.5)+1)]
        DP=self.DP
        
        if len(DP) >n:
            return DP[n]
        else:
            temp=len(DP)
            for x in range(temp,n+1):
                result=min(DP[x-y] for y in [z**2 for z in range(1,int(len(DP)**0.5)+1)] if x-y >=0 )
                DP.append(result+1)
            return DP[n]
