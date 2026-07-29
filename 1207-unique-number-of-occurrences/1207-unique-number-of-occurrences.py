class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d={}
        l=[]
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i] not in l:
                l.append(d[i])
            else:
                return False
        return True
            
