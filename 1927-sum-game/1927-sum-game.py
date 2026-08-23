class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # If number of ? is odd, Alice can always force a win
        if (left_q + right_q) % 2 == 1:
            return True

        # Difference in number of ? between the two halves
        q_diff = left_q - right_q

        # Difference in known digit sums
        sum_diff = left_sum - right_sum

        # Bob can balance only if this exact condition holds
        return sum_diff != -9 * (q_diff // 2)