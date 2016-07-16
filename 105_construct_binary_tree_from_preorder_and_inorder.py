# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def Build(self, pre_s, pre_e,in_s,in_e):
        if pre_s > pre_e or in_s > in_e: return None
        value=self.preorder[pre_s]
        root=TreeNode(value)
        index=self.inorder.index(value)
        left_distance=index-in_s
        root.left=self.Build(pre_s+1,pre_s+left_distance,in_s,in_s+left_distance-1)
        root.right=self.Build(pre_s+left_distance+1,pre_e,in_s+left_distance+1,in_e)
        return root
        
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        self.preorder=preorder
        self.inorder=inorder
        pre_s,in_s=0,0
        pre_e,in_e=len(preorder)-1,len(inorder)-1
        return self.Build(pre_s,pre_e,in_s,in_e)
        
