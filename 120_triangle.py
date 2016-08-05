class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        result=[triangle[0][0]]
        
        min_value=triangle[0][0]
        
        for r in range(1, len(triangle)):
            tmp=list()
            
            for l in range(len(triangle[r])):
                tmp_value=triangle[r][l]
                if l == 0:
                    tmp_value+=result[l]
                elif l == len(triangle[r])-1:
                    tmp_value+=result[l-1]
                else:
                    tmp_value+=min(result[l-1],result[l])
                tmp.append(tmp_value)
                if r== len(triangle)-1 and l==0:
                    min_value=tmp_value
                if r== len(triangle)-1 and l and min_value > tmp_value :
                    min_value=tmp_value

            result=tmp
            
        return min_value
