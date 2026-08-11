class Solution:
    def missingInteger(self, nums):
        # Find sum of longest sequential prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Store all numbers for O(1) lookup
        s = set(nums)

        # Find smallest missing number >= total
        while total in s:
            total += 1

        return total
        if m<=ma:
            return ma+1
        else:
            return m
            