class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=""
        while n!=0:
            r=n%2
            s=str(r)+s
            n=(n//2)
        
        s="0"*(32-len(s))+s
        l=0
        for i in range(0,len(s)):
            l=l+(int(s[i])*2**i)

        return l