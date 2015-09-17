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
        area = (D - B) * (C - A) + (G - E) * (H - F)
        if (E >= C or A >= G or B >= H or F >= D):
            return area
        return area - (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
