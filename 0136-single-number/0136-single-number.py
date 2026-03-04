class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=set(nums)
        for i in num:
            if nums.count(i)==1:
                return i
        