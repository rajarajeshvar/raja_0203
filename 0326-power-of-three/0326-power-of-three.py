class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n%3!=0 and n!=1) or n==0:
            return False
        for i in range(0,20):
            if n==3**i:
                return True
        return False
        
        