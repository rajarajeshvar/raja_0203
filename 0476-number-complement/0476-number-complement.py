class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=""
        r=0
        m=0
        n=0
        while num!=0:
            r=num%2
            if r==0:
                r="1"
            if r==1:
                r="0"
            s=r+s
            num=num//2
            n=n+1
        
        for i in s:
            h=int(i)
            n=n-1
            m=m+(h*(2**n))
        return m


        