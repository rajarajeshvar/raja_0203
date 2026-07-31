from collections import Counter

class Solution:
    def minimumPushes(self, word):
        freq = Counter(word)
        print(freq)
        counts = sorted(freq.values(), reverse=True)
        print(counts)
        ans = 0

        for i, f in enumerate(counts):
            ans += ((i // 8) + 1) * f

        return ans