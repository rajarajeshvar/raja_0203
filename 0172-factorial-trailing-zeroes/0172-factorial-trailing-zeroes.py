class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        z=0
        m=1
        for i in range(0,n):
            m=m*n
            n=n-1
        s=str(m)
        while s[-1]=="0":
            z+=1
            s=s[:-1]
        return z