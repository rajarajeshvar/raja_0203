class Solution(object):
    def maxVowels(self, s, k):
        vowels = set("aeiou")
        cnt = sum(c in vowels for c in s[:k])
        ans = cnt

        for i in range(k, len(s)):
            cnt += s[i] in vowels
            cnt -= s[i-k] in vowels
            ans = max(ans, cnt)

        return ans