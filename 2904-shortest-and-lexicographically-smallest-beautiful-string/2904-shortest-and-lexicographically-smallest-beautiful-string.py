class Solution:
    def shortestBeautifulSubstring(self, s, k):
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            while ones == k:
                # Remove leading zeroes
                while s[left] == '0':
                    left += 1

                current = s[left:right + 1]

                if ans == "" or len(current) < len(ans) or \
                   (len(current) == len(ans) and current < ans):
                    ans = current

                # Remove the first 1
                ones -= 1
                left += 1

        return ans