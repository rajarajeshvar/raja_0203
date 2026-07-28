class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l=len(word1)
        w=len(word2)
        s=""
        if l>w:
            for i in range(w):
                s+=word1[i]
                s+=word2[i]
            s+=word1[w:]
            return s
        else:
            for i in range(l):
                s+=word1[i]
                s+=word2[i]
            s+=word2[l:]
            return s
