class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        y=int(date[:4])
        m=int(date[5:7])
        d=int(date[8:10])
        s=""
        while d!=0:
            r=d%2
            s=str(r)+s
            d=(d//2)
        s="-"+s
        while m!=0:
            r=m%2
            s=str(r)+s
            m=(m//2)
        s="-"+s
        while y!=0:
            r=y%2
            s=str(r)+s
            y=(y//2)
        return s
        