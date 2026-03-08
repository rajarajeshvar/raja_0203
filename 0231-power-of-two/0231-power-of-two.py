class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(0,32):
            if n==2**i :
                return True
        return False
        






















        