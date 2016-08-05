class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int +=1
        """
        array=[[0 for y in range(n)] for z in range(m)]
        for x in range(m):
            for y in range(n):
               if x==0 or y==0: array[x][y]=1
               else: array[x][y]=0
               
        for x in range(1,m):
            for y in range(1,n):
                array[x][y]=array[x-1][y]+array[x][y-1]
                
        return array[m-1][n-1] if array else 0

