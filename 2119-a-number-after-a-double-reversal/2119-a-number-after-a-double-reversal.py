class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        nums=str(num)
        print(nums[-1])
        if num==0:
            return True
        if nums[0]=='0' or nums[-1]=='0':
            return False
        return True
        