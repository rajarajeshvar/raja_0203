from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s, k):
        cnt = Counter(s)

        mid = ""
        half = {}

        for ch in sorted(cnt):
            if cnt[ch] & 1:
                mid = ch
            half[ch] = cnt[ch] // 2

        m = sum(half.values())

        # factorials
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i

        # denominator = product(freq!)
        denom = 1
        for v in half.values():
            denom *= fact[v]

        # total distinct permutations of left half
        total = fact[m] // denom

        if k > total:
            return ""

        ans = []

        rem = m
        while rem:
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                # Number of permutations if ch is chosen
                ways = total * half[ch] // rem

                if ways >= k:
                    ans.append(ch)

                    total = ways
                    half[ch] -= 1
                    rem -= 1
                    break
                else:
                    k -= ways

        left = "".join(ans)
        return left + mid + left[::-1]