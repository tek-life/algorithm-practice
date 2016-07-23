class Solution(object):
    def DFS(self,start):
            if start[0]==self.target[0] and start[1]==self.target[1]:
                self.total_path+=1
            if start[0] <0 or start[0] > self.target[0]:
                return
            if start[1] <0 or start[1] > self.target[1]:
                return
            self.DFS((start[0]+1,start[1]))
            self.DFS((start[0],start[1]+1))
            
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int +=1
        """
        self.start=(0,0)
        self.target=(m-1,n-1)
        self.total_path=0
        
        self.DFS(self.start)
        
        return self.total_path
        #return len(self.total_path)
        
