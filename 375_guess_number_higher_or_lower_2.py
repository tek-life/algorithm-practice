"""
From Down to Top DP.
"""
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        array=[[0]*(n+1) for _ in range(n+1)]
        
        for row in range(n-1,0,-1):
            for col in range(row+1,n+1):
                array[row][col]=min(x+max(array[row][x-1],array[x+1][col]) for x in range(row,col))
        
        return array[1][n]

"""
From Top to Down DP.
"""
class Solution(object):
    def solve(self,start,end):
        if start < end and self.solve_array[start-1][end-1]==0:    
            self.solve_array[start-1][end-1]=min(x + max(self.solve(start,x-1),self.solve(x+1,end)) for x in range(start,end))
        return self.solve_array[start-1][end-1]
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.solve_array=[[0]*(n) for _ in range(n)]
            
        return self.solve(1,n)
