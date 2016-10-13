class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total_area=(C-A)*(D-B)+(G-E)*(H-F)
        over_lap=(min(C,G)-max(A,E))*(min(D,H)-max(B,F))
        new_l_x=max(A,E)
        new_l_y=max(B,F)
        new_h_x=min(C,G)
        new_h_y=min(D,H)
        
        if new_l_x<new_h_x and new_l_y<new_h_y:
            total_area-=over_lap
        return total_area
