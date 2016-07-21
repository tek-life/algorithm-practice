class Solution(object):
    def DFS(self, index, contains, target):
        if target== 0:
            self.result.append(contains)
            return
        if target < 0:
            return
        for i in range(index, len(self.candidates)):
	    ## All essence is the index "i".
            self.DFS(i, contains+[self.candidates[i]],target-self.candidates[i])
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]+=
        """
        candidates.sort()
        self.candidates=candidates
        self.result=[]
        self.DFS(0,[],target)
        return self.result
