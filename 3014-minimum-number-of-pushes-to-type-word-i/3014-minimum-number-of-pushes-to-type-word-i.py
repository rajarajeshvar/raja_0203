class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n=len(word)
        
        if n<=8:
            return n
        elif n<=16:
            n=((n-8)*2)+8
            return n
        elif n<=24:
            n=((n-16)*3)+24
            return n
        else:
            n=(n-24)*4+48
            return n
        

        