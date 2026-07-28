class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n==1:
            return s
        if n%2==0:
            s1=s[0:n/2]
        
            s1=sorted(list(s1))
            s1="".join(s1)
            return s1+s1[::-1]
        else:
            s1=s[0:n/2]
        
            s1=sorted(list(s1))
            s1="".join(s1)
            print(s1)
            return s1+s[(n/2)]+s1[::-1]