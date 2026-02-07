class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m=""
        n=""
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                m=m+s[j]
                if m==m[::-1] and len(m)>len(n):
                    n=m
            m=""
        return n
        