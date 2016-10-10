class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=[]
        temp={}
        t=0
        secret={'A':0,'C':1,'G':2,'T':3}
        for i in range(len(s)):
            t<<=2
            t&=~0x300000
            t|=secret[s[i]]
            if i>=9:
                if t in temp:
                    if temp[t]==1:
                        result.append(s[i-9:i+1])
                    temp[t]+=1
                else:
                    temp[t]=1
            
        return result
