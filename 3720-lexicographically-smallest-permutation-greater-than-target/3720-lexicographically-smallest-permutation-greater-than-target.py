class Solution:
    def lexGreaterPermutation(self, s, target):
        n = len(s)

        for i in range(n - 1, -1, -1):
            cnt = [0] * 26

            for ch in s:
                cnt[ord(ch) - 97] += 1

            possible = True

            for j in range(i):
                x = ord(target[j]) - 97
                if cnt[x] == 0:
                    possible = False
                    break
                cnt[x] -= 1

            if not possible:
                continue

            x = ord(target[i]) - 97

            for c in range(x + 1, 26):
                if cnt[c]:
                    ans = target[:i] + chr(c + 97)
                    cnt[c] -= 1

                    for k in range(26):
                        ans += chr(k + 97) * cnt[k]

                    return ans

        return ""