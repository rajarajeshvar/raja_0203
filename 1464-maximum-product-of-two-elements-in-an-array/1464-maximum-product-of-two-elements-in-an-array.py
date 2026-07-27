class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        h1=0
        h2=0
        for i in range(len(nums)):
            if nums[i]>=h1:
                h1=nums[i]
                j=i
                
        for i in range(len(nums)):
            if nums[i]<=h1 and i!=j and nums[i]>=h2:
                h2=nums[i]
        return (h1-1)*(h2-1)

        
        