class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        visited = [False] * n
        components = 0

        for i in range(n):
            if not visited[i]:
                components += 1
                stack = [i]

                while stack:
                    curr = stack.pop()
                    if visited[curr]:
                        continue

                    visited[curr] = True

                    for k in range(n):
                        if not visited[k]:
                            if stones[curr][0] == stones[k][0] or stones[curr][1] == stones[k][1]:
                                stack.append(k)

        return n - components
        
            