class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=""
        s1=""
        r=0
        m=0
        while num!=0:
            r=num%2
            s=str(r)+s
            num=num//2
        for i in s:
            if i=="0":
                s1=s1+"1"
            else:
                s1=s1+"0"
        n=len(s1)
        for i in s1:
            h=int(i)
            n=n-1
            print(h)
            m=m+(h*(2**n))
        return m


        