class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=0
        i=1
        while s==0:
            if k*i not in nums:
                s=k*i
            i+=1
        return s
        