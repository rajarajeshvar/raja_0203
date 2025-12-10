class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=['A','E','I','O','U','a','e','i','o','u']
        l1=[]
        s1=""
        for i in range(len(s)):
            if s[i] in l:
                l1.append(s[i])    
        for i in range(len(s)):
            if s[i] in l:
                s1=s1+l1[-1]
                l1.pop()
                
            else:
                s1=s1+s[i]
        return s1