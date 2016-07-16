# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Algorithm 1. May lead out of memory 
class Solution(object):
    def DFS(self,target, root, li):
        if not root: return None
        if root is target:
            return li+[root]
        else:
            left=self.DFS(target, root.left, li+[root])
            if left is None:
                    right=self.DFS(target, root.right, li+[root])
                    if right is None:
                        return None
            return left if left is not None else right 
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_list=self.DFS(p,root,[])
        q_list=self.DFS(q,root,[])
        if p_list and q_list:
            common_list = [x for x in p_list if x in q_list]
            return common_list[-1]
        else:
            return None

#Algorithm 2. This is an interesting algorithm.
#Under one node's left and right branches, if just one of them return value, then they are parent relation.
#If Both of them return value, then the parent is these common ancestor.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root is p or root is q:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        
        if left and right:
            return root
        return left if left else right 
