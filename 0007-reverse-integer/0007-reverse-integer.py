class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            s=str(-x)
            s=s[::-1]
            if int(s)<2**31-1:
                return int("-"+s)
            else:
                return 0
        if x==0:
            return 0
        if x>0 :
            s=str(x)
            s=s[::-1]
            if int(s)<2**31-1:
                return int(s)
            else:
                return 0