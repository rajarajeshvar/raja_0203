class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        l=[""]*numRows
        c=0
        step=1
        for i in s:
            l[c]+=i
            if c==0:
                step=1
            if c==numRows-1:
                step=-1
            c=c+step
        return "".join(l)
            