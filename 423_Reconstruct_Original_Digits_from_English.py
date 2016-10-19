class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        
        cnts=collections.Counter(s)
        
        keys=['z','w','u','x','g','r','f','s','o','i']
        values=['zero','two','four','six','eight','three','five','seven','one','nine']
        digits=[0,2,4,6,8,3,5,7,1,9]
        result=[]
        
        for i,key in enumerate(keys):
            num=cnts[key]
            result.append(num*str(digits[i]))
            for x in values[i]:
                cnts[x]-=num
                    
        result=sorted(result)
        return "".join(result)
