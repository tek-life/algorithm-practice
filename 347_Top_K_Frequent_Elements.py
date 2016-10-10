class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        import collections
        heap=[]
        count=collections.Counter(nums)
        
        for key,cnt in count.items():
            if len(heap)<k:
                heapq.heappush(heap,(cnt,key))
            else:
                if cnt>heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(cnt,key))
                    
        return [x[1] for x in heap]
