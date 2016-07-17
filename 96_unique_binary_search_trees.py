class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        Recursive Version:
        if n == 0 or n == 1: return 1
        if n == 2: return 2
        
        sum = 0
        for i in range(1,n+1):
            sum += self.numTrees(i-1) * self.numTrees(n-i)
            
        return sum
        """
        """
        Following is Iterative Version.
	"""
        dfs=[1,1,2]
        if n>2:
            for i in range(3, n+1):
                sum=0
                for sub_i in range(0,i):
                    sum+=dfs[sub_i]*dfs[i-sub_i-1]
                dfs.append(sum)
            
        return dfs[n]
