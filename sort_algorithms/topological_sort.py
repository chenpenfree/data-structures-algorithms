import typing as tp


class Graph:
    """有向无环图：拓扑排序"""

    def __init__(self, vertex_num):
        self._vertex_num = vertex_num  # 定点数
        self._result = []  # 排序结果
        self._in_degree = [0 for _ in range(self._vertex_num + 1)]  # 入度
        self._adjacency_table = [[] for _ in range(self._vertex_num + 1)]  # 邻接表存储图

    def build_graph_adjacency_table(self, start: int, end: int):
        """
        建立图的邻接表
        :param start:
        :param end:
        :return:
        """
        self._adjacency_table[start].append(end)
        self._in_degree[end] += 1

    def topological_bfs(self):
        """
        拓扑排序（bfs）
        1、从图中选择一个入度为0的顶点，输出该顶点
        2、从图中删除该顶点及其所有出边(即与之邻接的所有顶点入度减1)
        3、重复1,2步，直到所有节点全部输出，即整个拓扑排序完成。
        :return:
        """
        index = 0
        for i in range(1, self._vertex_num + 1):
            if self._in_degree[i] == 0:
                index = i
                break

        temp_list = [index]  # 入度为0的点
        while temp_list:
            temp_vertex = temp_list.pop(0)
            for vertex in self._adjacency_table[temp_vertex]:
                self._in_degree[vertex] -= 1
                if vertex not in self._result and self._in_degree[vertex] == 0:
                    temp_list.append(vertex)
                    self._vertex_num -= 1

            self._result.append(temp_vertex)

        if self._vertex_num != 0:
            print('图中有环!')
            return None

    def topological_dfs(self):
        """
        拓扑排序(dfs)
        :return:
        """
        visited = [False] * (self._vertex_num + 1)
        for vertex in range(1, self._vertex_num + 1):
            if not visited[vertex]:
                self._topological_dfs(vertex, visited)

    def _topological_dfs(self, index, visited):
        """
        递归实现
        :return:
        """
        if visited[index]:
            return

        for i in self._adjacency_table[index]:
            if not visited[i]:
                self._topological_dfs(i, visited)
        self._result.append(index)
        visited[index] = True

    def print_graph(self):
        print(self._adjacency_table)

    def print_result_bfs(self):
        print(self._result)

    def print_result_dfs(self):
        print(list(reversed(self._result)))


if __name__ == '__main__':
    graph_var = Graph(5)
    graph_var.build_graph_adjacency_table(1, 2)
    graph_var.build_graph_adjacency_table(1, 4)
    graph_var.build_graph_adjacency_table(2, 3)
    graph_var.build_graph_adjacency_table(3, 5)
    graph_var.build_graph_adjacency_table(4, 5)
    # graph_var.build_graph_adjacency_table(5, 4)
    graph_var.build_graph_adjacency_table(4, 3)

    graph_var.print_graph()
    # graph_var.topological_bfs()
    graph_var.topological_dfs()
    graph_var.print_result_dfs()
