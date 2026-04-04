class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        l=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        for i in d:
            if d[i]>=2:
                
                l.append(i)
        return l
        