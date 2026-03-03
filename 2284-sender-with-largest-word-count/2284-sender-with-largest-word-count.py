class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        d={}
        l=0
        s=""
        l1=[]
        for i in range(0,len(senders)):
            if senders[i] not in d:
                d[senders[i]]=len(messages[i].split(" "))
            else:
                d[senders[i]]=d.get(senders[i])+len(messages[i].split(" "))
            
        
        for i in d:
            if (d[i])>l:
                l=d[i]
                s=i
            elif d[i]==l and (i>s):
                s=i
                
        print(l1)
        print(s)
        return s
        