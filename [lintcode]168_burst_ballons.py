class Solution:
    """
    @param: nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        # write your code here
        #dp[i,j] represent the scores from i to j
        #dp[i,j] = max{score(k) + dp[i][k-1] + dp[k+1][j]} ( i<=k<=j )
        #           score(k) = nums(i-1) * k * nums(j+1)
        length = len(nums)
        array = nums
        array.insert(0, 1)
        array.append(1)

        dp = []
        
        for _ in range(length+2):
            dp.append([0 for _ in range(length+2)])
            
        for left in range(length, 0, -1):
            for right in range(left, length+1):
                score = dp[left][right]
                for k in range(left, right+1):
                    score =max(score, array[left-1] * array[k] * array[right+1] + dp[left][k-1]+ dp[k+1][right])
                dp[left][right] = score
                
        return dp[1][length]
