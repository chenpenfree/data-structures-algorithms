from typing import List


class Solution:
    island_num = 0
    grid_len = 0
    element_max_len = 0

    def num_islands(self, grid: List[List[int]]) -> int:
        """
        求岛屿的数量
        :param grid:
        :return:
        """
        self.grid_len = len(grid)
        if self.grid_len == 0:
            return 0

        self.element_max_len = max([len(sub) for sub in grid])
        # 因为[0] * 5是一个一维数组的对象，* 3的话只是把对象的引用复制了3次
        # visited = [[0] * 5] * 3
        visited = [[False] * self.element_max_len  for _ in range(self.grid_len)]
        for i in range(self.grid_len):
            for j in range(self.element_max_len):
                if not visited[i][j] and grid[i][j] != 0:
                    self._num_islands(grid, visited, i, j)
                    self.island_num += 1

        return self.island_num

    def _num_islands(self, grid: List[List[int]], visited, i, j):

        if i < 0 or j < 0:
            return

        if i >= self.grid_len or j >= self.element_max_len:
            return

        if visited[i][j] or grid[i][j] == 0:  # 访问过的节点
            return

        self._num_islands(grid, visited, i, j - 1)
        self._num_islands(grid, visited, i, j + 1)
        self._num_islands(grid, visited, i - 1, j)
        self._num_islands(grid, visited, i + 1, j)

        visited[i][j] = True


if __name__ == '__main__':
    # matrix_list = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
    # matrix_list = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
    matrix_list = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]

    instance = Solution()
    instance.num_islands(matrix_list)
    print(instance.island_num)




