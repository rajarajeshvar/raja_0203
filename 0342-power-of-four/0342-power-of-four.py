class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(0,17):
            if n==4**i:
                return True
        return False
        