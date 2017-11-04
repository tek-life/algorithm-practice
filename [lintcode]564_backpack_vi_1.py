class Solution:
    """
    @param: nums: an integer array and all positive numbers, no duplicates
    @param: target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        #dp[i] = dp[t-v[i]]+vi if dp[t-v[i]] >= 1 dp[i] +=dp[t-v[i]]
        dp= [0 for _ in range(target + 1)]
        dp[0] = 1
        
        for v in range(1, target + 1):
            for i in range(1, len(nums)+1):
	    	#when dp[v-nums[i-1]] == 0, it could be processed.So optimize here.
                if v >= nums[i-1]:# and dp[v-nums[i-1]] > 0:
                    dp[v] += dp[v-nums[i-1]]
                    
        return dp[-1]

