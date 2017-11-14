"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        # write your code here
        if n > 0:
            return self.helper(1, n)
        if n == 0:
            return [None]
        
    def helper(self, start,end):
        if start > end:
	    """
	    Here, [] or [None] is different for the next procedure
	    """
            return [None]
            
        result = []
        for n in range(start, end+1):
            left = self.helper(start, n-1)
            right = self.helper(n + 1, end)
            
            for l in left:
                for r in right:
                    root = TreeNode(n)
                    root.left = l
                    root.right = r
                    result.append(root)
            
        return result
