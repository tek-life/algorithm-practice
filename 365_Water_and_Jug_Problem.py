class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        dic={}
        m=0
        n=0
        #m pour to n
        while m!=z and n!=z and (m+n!=z):
            if m==0:
                m=x
            else:
                if n==y:
                    n=0
                else:
                    if(m+n)>=y:
                        m=m-(y-n)
                        n=y
                    else:
                        n=m+n
                        m=0
            if (m,n) not in dic:
                dic[(m,n)]=1
            else:
                return False
        return True
