class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        litter = {}
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        k = len(litter)

        if k == 0:
            return 0

        full = (1 << k) - 1

        best = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]

        best[sr][sc][0] = energy

        q = [(sr, sc, 0, energy)]
        steps = 0

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            nq = []

            for r, c, mask, e in q:

                if mask == full:
                    return steps

                if best[r][c][mask] != e:
                    continue

                if e == 0:
                    continue

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1
                    nmask = mask

                    cell = classroom[nr][nc]

                    if cell == 'R':
                        ne = energy

                    elif cell == 'L':
                        nmask |= 1 << litter[(nr, nc)]

                    if ne <= best[nr][nc][nmask]:
                        continue

                    best[nr][nc][nmask] = ne
                    nq.append((nr, nc, nmask, ne))

            q = nq
            steps += 1

        return -1