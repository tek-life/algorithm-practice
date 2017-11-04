class Solution:
    """
    @param: nums: an integer array and all positive numbers, no duplicates
    @param: target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target)ckPackVI(self, nums, target):
        self.result = 0
        self.fun(nums, target, [], result)
        
        return self.result
        
    def fun(self, nums, target, tmp, result):
        if tmp and sum(tmp) > target:
            return
        if tmp and sum(tmp) == target:
	    self.result += 1
	    return

        for x in nums:
            self.fun(nums, target, tmp+[x], result)
