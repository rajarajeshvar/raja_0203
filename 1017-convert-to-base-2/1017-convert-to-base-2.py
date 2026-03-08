class Solution(object):
    def baseNeg2(self, n):
        if n == 0:
            return "0"
        
        res = ""
        
        while n != 0:
            remainder = n % 2
            res = str(remainder) + res
            n = -(n // 2)
        
        return res