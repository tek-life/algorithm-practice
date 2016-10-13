class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp=0
        xx=x
        while xx!=0:
            tmp=tmp*10+xx%10
            xx=xx/10
        return tmp==x
