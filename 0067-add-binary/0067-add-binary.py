class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a=="0" and b=="0":
            return "0"
        a = int(a, 2)
        b=int(b,2)
        a=a+b
        s=""
        while a!=0:
            r=a%2
            s=str(r)+s
            a=a//2
        return s