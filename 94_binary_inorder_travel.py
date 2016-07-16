# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        result=[]
        node=root
        while True:
            while node:
                stack.append(node)
                node=node.left
            if not stack: break
            node=stack.pop()
            result.append(node.val)
            node=node.right
        return result     
