class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m=True
        s=""
        while n!=0:
            r=n%2
            s=str(r)+s
            n=n//2
        for i in range(0,len(s)-1):
            if (s[i]=="0" and s[i+1]=="0") or (s[i]=="1" and s[i+1]=="1"):
                m=False
        return m
        