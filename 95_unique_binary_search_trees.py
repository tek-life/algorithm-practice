# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def DFS(self, start, root_i, end):
        result,left,right=[],[],[]
        
        if start == root_i:
            left=[None,]
        elif start == (root_i - 1):
            left=[TreeNode(start),]
        else:
            for index_left in range(start, root_i):
                left += self.DFS(start, index_left, root_i-1)
        
        if root_i == end:
            right=[None,]
        elif (root_i == end-1):
            right=[TreeNode(end),]
        else:
            for index_right in range(root_i+1, end+1):
                right += self.DFS(root_i+1, index_right, end)
        
        for i_left in left:
            for i_right in right:
                root = TreeNode(root_i)
                root.left=i_left
                root.right=i_right
                result.append(root)
        return result
                
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        result=[]
        for i in range(1,n+1):
            result+=self.DFS(1,i,n)
        return result
        
