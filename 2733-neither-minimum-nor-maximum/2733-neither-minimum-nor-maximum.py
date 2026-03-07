class Solution(object):
    def findNonMinOrMax(self, nums):
        if len(nums) < 3:
            return -1
        
        a, b, c = nums[0], nums[1], nums[2]
        return a + b + c - max(a, b, c) - min(a, b, c)