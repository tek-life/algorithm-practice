class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        while left < len(nums)-1 and nums[left] < nums[left+1]:
            left+=1
        return left
