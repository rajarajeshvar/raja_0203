from collections import defaultdict

class Solution(object):
    def removeStones(self, stones):
        n = len(stones)

        rows = defaultdict(list)
        cols = defaultdict(list)

        for i in range(n):
            r, c = stones[i]
            rows[r].append(i)
            cols[c].append(i)

        visited = [False] * n
        components = 0

        for i in range(n):
            if visited[i]:
                continue

            components += 1
            stack = [i]

            while stack:
                curr = stack.pop()

                if visited[curr]:
                    continue

                visited[curr] = True
                r, c = stones[curr]

                for nxt in rows[r]:
                    if not visited[nxt]:
                        stack.append(nxt)

                for nxt in cols[c]:
                    if not visited[nxt]:
                        stack.append(nxt)

        return n - components
            