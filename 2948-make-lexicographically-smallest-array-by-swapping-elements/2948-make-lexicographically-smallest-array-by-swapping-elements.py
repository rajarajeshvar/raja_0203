class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original index)
        arr = sorted((num, i) for i, num in enumerate(nums))

        ans = [0] * n
        i = 0

        while i < n:
            j = i + 1

            # Find one connected group
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            # Original indices of this group
            indices = sorted(idx for _, idx in arr[i:j])

            # Smallest values go to smallest indices
            for idx, (value, _) in zip(indices, arr[i:j]):
                ans[idx] = value

            i = j

        return ans