class Solution:
    """
    @param: matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        #dp[i][j], the largest full 1 squire's right corner is [i][j]
        #dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
        if not matrix:
            return 0
            
        width_c = len(matrix[0])+1
        width_r = len(matrix)+1
        
        dp = []
        for _ in range(width_r):
            dp.append([0 for _ in range(width_c)])
        
        val = 0
        for r in range(1, width_r):
            for c in range(1, width_c):
                if matrix[r-1][c-1] == 1:
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1
                    val = max(dp[r][c], val)
                
        return val * val
