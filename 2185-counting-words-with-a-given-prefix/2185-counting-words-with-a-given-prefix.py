class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        n=0
        s=len(pref)
        for i in words:
            if pref==i[:s]:
                n+=1
        return n