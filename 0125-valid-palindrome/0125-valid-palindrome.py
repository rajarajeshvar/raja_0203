class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h=""
        for i in range(len(s)):
            if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122) or (ord(s[i])>=48 and ord(s[i])<=57):
                h+=s[i]
                
        h=h.lower()
        print(h)
        if h==h[::-1]:
            
            return True
        else:
            
            return False      
        