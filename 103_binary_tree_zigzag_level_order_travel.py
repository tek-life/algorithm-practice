# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        result=[]
        tmp_result=[]
        stack1=[]
        stack2=[]
        level=1
        if root:stack1.append(root)
        
        while stack1:
            
            node=stack1.pop(0)
            
                
            tmp_result.append(node.val)
            
            if node.left: stack2.append(node.left)
            if node.right:stack2.append(node.right)

            if len(stack1) ==0:
                tmp=stack1
                stack1=stack2
                stack2=tmp
                
                if not level%2:
                    tmp_result.reverse()
                
                result.append(tmp_result)
                tmp_result=[]
                level+=1
                
        return result
            
        
