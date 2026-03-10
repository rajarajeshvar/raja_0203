class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        o=9
        l=9
        n1=10
        if n==1:
            return n1
        elif n==0:
            return 1
        else:
            for i in range(1,n):
                o=o*l
                n1+=o
                l-=1
        return n1
        