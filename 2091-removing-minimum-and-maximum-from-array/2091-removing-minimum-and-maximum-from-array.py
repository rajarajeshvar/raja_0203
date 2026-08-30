class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        if mn > mx:
            mn, mx = mx, mn

        front = mx + 1

        back = n - mn

        both = mn + 1 + n - mx

        return min(front, back, both)