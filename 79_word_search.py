class Solution(object):
    def dfs(self,(row,col),index):
        if row < 0 or col < 0: return False
        if row > self.row_limit or col > self.col_limit or index >self.word_limit: return False
      
        if self.pos[row][col] == 1: return False
        
        if self.board[row][col] == self.word[index]:
            if index == self.word_limit:
                self.pos[row][col] = 1
                return True
            else:
                index +=1
                for couple in [(-1,0),(1,0),(0,-1),(0,1)]:
                    self.pos[row][col] = 1
                    result = self.dfs((row+couple[0],col+couple[1]),index)
                    if result:
                        return True
                    else:
                        self.pos[row][col]=0
                
        else:
            return False
        
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        loc=[(i,j) for i,sub in enumerate(board) for j,x in enumerate(sub) if x==word[0]]
        
        self.word=word
        self.board=board
        self.row_limit=len(board)-1
        self.col_limit=len(board[0])-1
        self.word_limit=len(word)-1
        
        for num in xrange(len(loc)):
            self.pos=[]
            for i in xrange(len(board)):
                tmp=[0]*len(board[0])
                self.pos.append(tmp)
            if self.dfs(loc[num],0):
                return True
        return False
        
