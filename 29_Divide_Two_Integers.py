ass Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor ==0 or divisor==-1 and dividend==-2**31: 
            return 2**31-1
        flag=0
        p=abs(dividend)
        if p!=dividend:
            flag^=1
        q=abs(divisor)
        temp=q
        if q!=divisor:
            flag^=1
        if p < q: return 0
        m=1
        res=0
        if q==1:
            res=p
        else:
            while p>=q:
                m=1
                while (q<<1)<=p:
                    q<<=1
                    m<<=1
                res+=m
                p-=q
                q=temp
                
        if flag:
            return 0-res
        else:
            return res
