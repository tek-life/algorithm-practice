class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        a=numerator
        b=denominator
        result=""
        flag=False
        dic={}
        minus=False
        if a*b<0: minus=True
        
        if a<0:
            a=-a
        if b<0:
            b=-b
        while a!=0:
            if a<b:
                if flag==False:
                    result+='.'
                    flag=True
            if a not in dic:
                dic[a]=len(result)
            else:
                result = result[:dic[a]]+'('+result[dic[a]:]+')'
                break
            
            if a<b:
                a*=10
            c=a/b
            result+=str(c)
            if a>b:
                a=a%b
                
        if result.startswith('.'):
            result='0'+result
        if result == "": 
            result='0'
        if minus:
            result='-'+result
        return result
