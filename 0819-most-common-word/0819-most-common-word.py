class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        l=[]
        s=""
        m=0
        
        for i in paragraph:
            if i in "!?',;.":
                l.append(s.lower())
                s=""
                continue
            else:
                s=s+i
            if i==" ":
                s=s[:-1]
                l.append(s.lower())
                s=""
        l.append(s.lower())
        n=len(l)
        d={}
        for i in range(n):
            if l[i]=="":
                continue
            if l[i] in d:
                d[l[i]]+=1
            else:
                d[l[i]]=1
        for i in d:
            if i not in banned and d[i]>m:
                m=d[i]
                s=i
        return s

        

        