class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        for i in range(0,len(nums)):
            nums[i]=int(nums[i])
        nums=sorted(nums)
        return str(nums[-k])
        