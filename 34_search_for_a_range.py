class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]=+
        """
        left_result,right_result=-1,-1
        l,r=0,len(nums)-1
        
        #mid=(l+r)/2
        #print "---"
        """
        if Just l < r, will not locate the lth number.
        For finding the lowest and highest limit, it is true. Because there may be one number for the subarry.
        """
        while l<= r:# and l < len(nums):
            mid=(l+r)/2
            #print l,r,mid
            if nums[mid] < target:
                l=mid+1
                
            if nums[mid] == target:
                r=mid-1
                left_result=mid
                
            if nums[mid] > target:
                r=mid-1

        l,r=0,len(nums)-1
        #mid=(l+r)/2
        while l<= r:# and l < len(nums):
            mid=(l+r)/2
            if nums[mid] < target:
                l=mid+1
            if nums[mid] == target:
                l=mid+1
                right_result=mid
            if nums[mid] > target:
                r=mid-1
        
        
        return [left_result,right_result]
