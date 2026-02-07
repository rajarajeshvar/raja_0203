class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        n=0
        for i in nums:
            if i==1:
                m+=1
                if m>n:
                    n=m
            else:
                m=0
        return n