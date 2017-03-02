class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if not height:
            return 0
        stack = []
        i = 0
        max_area = 0
        #print len(height)
        while i < len(height)  or len(stack) > 0:
            if len(stack) == 0 or (i < len(height) and height[i] > height[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                i_tmp = stack.pop()
                length = i
                if len(stack) > 0:
                    length = i - stack[-1] - 1
                max_area = max(max_area, height[i_tmp] * length)
        return max_area
