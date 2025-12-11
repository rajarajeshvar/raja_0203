class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(n)
        m=1
        s=0
        for i in n:
            i=int(i)
            m=m*i
            s=s+i
        res=m-s
        return res


        