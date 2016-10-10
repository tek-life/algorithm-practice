class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        return map(lambda x:x[0],sorted(collections.Counter(nums).items(),key=lambda x:x[1],reverse=True)[:k])
        
