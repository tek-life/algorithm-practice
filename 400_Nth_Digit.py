class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        tmp=0
        while True:
            digits=(10**(count+1)-10**count)*(count+1)
            if n <=digits:
                num=(n-1)/(count+1)
                tmp=10**count+num
                n-=num*(count+1)
                break
            else:
                n-=digits
            count+=1
        return int(str(tmp)[n-1])
