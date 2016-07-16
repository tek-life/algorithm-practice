# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DFS(self,root,li,sum):
        """
        More clear way
        if not root.left and not root.right:
            if root.val==sum:
                self.li.append(li+[root.val])
        sum-=root.val
        if root.left:self.DFS(root.left, [root.val]+li,sum)
        if root.right:self.DFS(root.right, [root.val]+li,sum)
        """
        li.append(root.val)
        if not root.left and not root.right:
            if root.val == sum:
                self.li.append(li)
                return
            else:
                return
        sum-=root.val
        """
        There is a more clear way:
        
        """
        tmp_left=li[:]
        tmp_right=li[:]
        
        if root.left:self.DFS(root.left, tmp_left, sum)
        if root.right:self.DFS(root.right,tmp_right,sum)
        
            
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.li=[]
        
        """
        More clear
        if root:
            self.DFS(root,[],sum)
        return self.li
        """
        
        li=[]
        if root is None:
            return []
        
        self.DFS(root,li,sum)
        
        return self.li
        
