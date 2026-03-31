class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        banned = set(banned)
        d = {}
        word = ""
        res = ""
        m = 0

        for c in paragraph + " ":
            if c.isalnum():
                word += c.lower()
            else:
                if word:
                    if word not in banned:
                        if word in d:
                            d[word] += 1
                        else:
                            d[word] = 1
                        
                        if d[word] > m:
                            m = d[word]
                            res = word
                    word = ""
        return res
        

        