# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
The result is correct. But throw time limit exceeded.
"""
class Solution(object):
 
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        
        if root.left is None and root.right is None: return root.val
        
        if not root.left and root.right:
            if not root.right.left and not root.right.right:
                return root.val if root.val > root.right.val else root.right.val
        if root.left and not root.right:
            if not root.left.left and not root.left.right:
                return root.val if root.val > root.left.val else root.left.val
        if root.left and root.right:
            if not root.left.left and not root.left.right and not root.right.left and not root.right.right:
                return root.val if root.val > (root.left.val + root.right.val) else (root.left.val + root.right.val)
        
        
        child_left_left,child_left_right=0,0
        child_right_left,child_right_right=0,0
        
        if root.left:
            child_left_left=self.rob(root.left.left)
            child_left_right=self.rob(root.left.right)
        if root.right:
            child_right_left=self.rob(root.right.left)
            child_right_right=self.rob(root.right.right)
        
        sum1=root.val + child_left_left +child_left_right + child_right_left+child_right_right
        
        root_left=self.rob(root.left)
        root_right=self.rob(root.right)
        sum2=self.rob(root.left)+self.rob(root.right)
        
        return sum1 if sum1 > sum2 else sum2
