# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DFS(self,root):
        if root.left is None and root.right is None:
            return root

        #This subcode looks like more clear.
        """
        node=root
        node.right=self.DFS(root.left)
        right=self.DFS(root.right)
        
        while node.right:
            node=node.right
        node.right=right
        return root
        """

        left=None
        right=None
        
        if root.left: left=self.DFS(root.left)

        if root.right: right=self.DFS(root.right)

        if left is not None:
            left_right=left
            
            """
            The subcode looks like more simple
            while left_right.right is not None:
                left_right=left_right
            """
            while left_right is not None:
                if left_right.right is not None:
                    left_right=left_right.right
                else:
                    break
            
            left_right.right=right
                
            root.right=left
            root.left=None
            
        return root

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None: return None
        
        self.DFS(root)
