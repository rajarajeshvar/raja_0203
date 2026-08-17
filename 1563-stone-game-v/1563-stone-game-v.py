class Solution:
    def stoneGameV(self, A):
        n = len(A)

        dp = [[0] * n for _ in range(n)]
        mx = [[0] * n for _ in range(n)]

        # Base case
        for i in range(n):
            mx[i][i] = A[i]

        for j in range(1, n):

            mid = j
            left_sum = A[j]
            right_sum = 0

            for i in range(j - 1, -1, -1):

                left_sum += A[i]

                # Move mid while left side >= right side
                while mid > i and (right_sum + A[mid]) * 2 <= left_sum:
                    right_sum += A[mid]
                    mid -= 1

                # Equal split
                if right_sum * 2 == left_sum:
                    dp[i][j] = mx[i][mid]

                # Left side is smaller
                if mid > i:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[i][mid - 1]
                    )

                # Right side is smaller
                if mid < j:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[j][mid + 1]
                    )

                # Update maximum values
                mx[i][j] = max(
                    mx[i][j - 1],
                    dp[i][j] + left_sum
                )

                mx[j][i] = max(
                    mx[j][i + 1],
                    dp[i][j] + left_sum
                )

        return dp[0][n - 1]
