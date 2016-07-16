# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def Build(self, in_s, in_e, post_s,post_e):
        if in_s > in_e or post_s > post_e:
            return None
        value=self.postorder[post_e]
        root=TreeNode(value)
        index=self.inorder.index(value)
        left_distance=index-in_s
        right_distance=in_e-index
        root.left=self.Build(in_s, in_s+left_distance-1,post_s,post_s+left_distance-1)
        root.right=self.Build(index+1, in_e,post_e-right_distance, post_e-1)
        return root
        
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder=inorder
        self.postorder=postorder
        
        in_s,post_s=0,0
        in_e,post_e=len(inorder)-1,len(postorder)-1
        
        return self.Build(in_s,in_e,post_s,post_e)
