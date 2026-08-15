class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor = 0

        for x in nums:
            total_xor ^= x

        if total_xor != 0:
            return n

        # Total XOR is 0
        # If every element is 0, no valid subsequence exists
        if all(x == 0 for x in nums):
            return 0

        return n - 1 