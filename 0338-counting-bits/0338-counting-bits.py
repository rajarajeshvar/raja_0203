class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        for i in range(0,n+1):
            c=0
            while i!=0:
                r=i%2
                if r==1:
                    c+=1
                i=i//2
            l.append(c)
        return l

        