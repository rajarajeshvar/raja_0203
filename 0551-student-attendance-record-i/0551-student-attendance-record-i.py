class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s.count('A')>=2:
            return False
        elif 'LLL' in s:
            return False
        else:
            return True
        