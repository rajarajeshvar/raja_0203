class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"
        
        # mask to 32 bits
        num &= 0xFFFFFFFF
        
        hex_chars = "0123456789abcdef"
        res = []
        
        while num > 0:
            res.append(hex_chars[num & 15])
            num >>= 4
        
        return "".join(reversed(res))
