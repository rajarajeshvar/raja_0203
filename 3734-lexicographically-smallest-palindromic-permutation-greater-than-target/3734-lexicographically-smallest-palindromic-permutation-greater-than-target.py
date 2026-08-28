class Solution:
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd count
        odd = 0
        mid = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                mid = chr(i + ord('a'))

        if odd > 1:
            return ""

        # We only need half of the characters
        half = [x // 2 for x in cnt]

        # Build the left half
        left = []

        for i in range(n // 2):
            for c in range(26):
                if half[c] == 0:
                    continue

                # Try this character
                half[c] -= 1
                left.append(chr(c + ord('a')))

                # Make the largest possible completion
                rem = ""

                for j in range(25, -1, -1):
                    rem += chr(j + ord('a')) * half[j]

                candidate_left = "".join(left) + rem
                candidate = (
                    candidate_left
                    + mid
                    + candidate_left[::-1]
                )

                if candidate > target:
                    # This character can lead to an answer
                    break

                # Undo
                left.pop()
                half[c] += 1

            else:
                return ""

        left = "".join(left)
        ans = left + mid + left[::-1]

        return ans if ans > target else ""