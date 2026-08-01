class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
        return -1