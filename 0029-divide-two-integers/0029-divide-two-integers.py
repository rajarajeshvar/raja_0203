class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==0:
            return 0
        x=float(dividend)/float(divisor) 
        print(x)
        if x<0:
            if x<-2**31:
                return -2**31
            elif x==-1:
                return -1
            else:
                return int(x)
        if x>0:     
            if x>2**31-1:
                return 2**31-1
            else:  
                return int(x)
        