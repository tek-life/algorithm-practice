class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump=len(nums)-1
        for i in xrange(len(nums)-2,-1,-1):
            if nums[i]+i >= jump:
                jump=i
                
        return nums[0]>=jump

