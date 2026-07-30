class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1=max(nums)
        m2=min(nums)
        while m2!=0:
            m1,m2=m2,m1%m2
        return m1
        
        