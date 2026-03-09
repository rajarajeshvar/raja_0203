class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        n=""
        if num==0:
            return "0"
        if num>0:
            while num!=0:
                r=num%7
                n=str(r)+n
                num=(num//7) 
        if num<0:
            num=-num
            while num!=0:
                r=num%7
                n=str(r)+n
                num=(num//7) 
            n="-"+n
        return n

        