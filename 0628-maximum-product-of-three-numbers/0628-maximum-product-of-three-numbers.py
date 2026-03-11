class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=1
        m=1
        nums=sorted(nums,reverse=True)
        m=nums[-1]*nums[-2]*nums[0]
        for i in range(0,3):
            n*=nums[i]
        if n>m:   
            return n
        else:
            return m
        