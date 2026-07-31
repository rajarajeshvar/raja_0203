class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="":
            return True
        i=0
        for j in t:
            if j!=s[i]:
                continue
            else:
                i+=1
                if i>=len(s):
                    break
                    
        if i==len(s):
            return True
        else:
            return False
                

            
                
        