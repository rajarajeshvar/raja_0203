class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num=set(nums)
        if len(num)==len(nums):
            return False
        else:
            return True
        