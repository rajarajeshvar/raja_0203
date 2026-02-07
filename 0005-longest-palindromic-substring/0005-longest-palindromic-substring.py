class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        # Transform string
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        
        center = right = 0

        for i in range(n):
            mirror = 2 * center - i
            print(mirror)

            if i < right:
                p[i] = min(right - i, p[mirror])

            # Expand around center i
            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and \
                  t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

        max_len = max(p)
        center_index = p.index(max_len)
        start = (center_index - max_len) // 2

        return s[start:start + max_len]
