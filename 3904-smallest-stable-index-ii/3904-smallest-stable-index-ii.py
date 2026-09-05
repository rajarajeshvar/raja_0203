class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # suffix minimum
        right = [0] * n
        right[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            right[i] = min(nums[i], right[i + 1])

        # prefix maximum + check
        left = 0

        for i in range(n):
            left = max(left, nums[i])

            if left - right[i] <= k:
                return i

        return -1