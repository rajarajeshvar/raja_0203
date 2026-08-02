from collections import defaultdict

class Solution:
    def maxOperations(self, nums, k):
        freq = defaultdict(int)
        ans = 0

        for num in nums:
            need = k - num

            if freq[need] > 0:
                ans += 1
                freq[need] -= 1
            else:
                freq[num] += 1

        return ans