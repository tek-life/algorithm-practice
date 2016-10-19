class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        def helper(a,n):
            if n==0:
                return 1
            if n==1:
                return a
            tmp=helper(a,n/2)%1337
            result=(tmp*tmp)%1337
            if n%2==0:
                return result
            else:
                return (result*a)%1337
        res=1
        a%=1337
        for x in b:
            res=(helper(res,10)*helper(a,x))%1337
        return res
