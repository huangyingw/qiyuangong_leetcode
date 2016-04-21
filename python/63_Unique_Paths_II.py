class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dmap = []
        for i in range(m):
            temp = [0] * n
            dmap.append(temp)
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                dmap[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] != 1:
                dmap[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                l = u = 0
                if i - 1 >= 0:
                    u = dmap[i - 1][j]
                if j - 1 >= 0:
                    l = dmap[i][j - 1]
                dmap[i][j] = l + u
        return dmap[m - 1][n - 1]