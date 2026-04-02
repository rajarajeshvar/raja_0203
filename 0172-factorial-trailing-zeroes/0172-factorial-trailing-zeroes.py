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
        m=str(m)
        i=-1
        while m[i]=="0":
            z+=1
            i=i-1
        return z