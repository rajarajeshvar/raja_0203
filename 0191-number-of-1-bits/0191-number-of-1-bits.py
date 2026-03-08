class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=""
        c=0
        while n!=0:
            r=n%2
            if r==1:
                c+=1
                
            
            n=(n//2)
        return c
        