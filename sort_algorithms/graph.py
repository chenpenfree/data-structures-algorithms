import typing as tp
import numpy as np


class UndirectedGraph:
    """无向图"""

    def __init__(self, list_param: tp.List[int]):
        self._vertex_num = max(list_param) + 1
        self._adjacency_matrix = np.zeros((self._vertex_num, self._vertex_num))  # 邻接矩阵
        self._adjacency_table = [[] for _ in range(self._vertex_num)]  # 邻接表
        self._found = False

    def matrix_save_edge(self, vertex_one, vertex_tow):
        """
        邻接矩阵存储边
        :param vertex_one:
        :param vertex_tow:
        :return:
        """
        self._adjacency_matrix[vertex_one][vertex_tow] = 1
        self._adjacency_matrix[vertex_tow][vertex_one] = 1

    def table_save_edge(self, vertex_one, vertex_tow):
        """
        邻接表存储边：无向图每条边存储两次
        :param vertex_one:
        :param vertex_tow:
        :return:
        """
        self._adjacency_table[vertex_one].append(vertex_tow)
        self._adjacency_table[vertex_tow].append(vertex_one)

    def print_table(self):
        """
        打印邻接表
        :return:
        """
        print(self._adjacency_table)

    def print_matrix(self):
        """
        打印邻接矩阵
        :return:
        """
        print(self._adjacency_matrix)

    def breadth_first_find(self, vertex_one: int, vertex_two: int):
        """
        广度优先搜索
        :param vertex_one:
        :param vertex_two:
        :return:
        """

        if vertex_one == vertex_two:
            return

        visited = [False for _ in range(self._vertex_num)]  # 存储访问过的定点
        visited[vertex_one] = True
        prev_vertex = [-1 for _ in range(self._vertex_num)]  # 存储每个定点的前一个顶点
        level_list = [vertex_one]  # 方便按层遍历图

        while level_list:
            temp_vertex = level_list.pop(0)
            for vertex in self._adjacency_table[temp_vertex]:
                if not visited[vertex]:
                    prev_vertex[vertex] = temp_vertex
                    if vertex == vertex_two:
                        self.print_bfs(prev_vertex, vertex_one, vertex_two)
                        return
                    visited[vertex] = True
                    level_list.append(vertex)

    def print_bfs(self, prev_vertex, vertex_one, vertex_two):
        """
        打印广度优先搜索, 递归逆序打印
        :param prev_vertex:
        :param vertex_one:
        :param vertex_two:
        :return:
        """
        if prev_vertex[vertex_two] != -1 and vertex_one != vertex_two:
            self.print_bfs(prev_vertex, vertex_one, prev_vertex[vertex_two])

        print(vertex_two, end=' ')

    def depth_first_find(self, vertex_one, vertex_two):
        """
        深度优先搜索
        :param vertex_one:
        :param vertex_two:
        :return:
        """
        if vertex_one == vertex_two:
            return

        prev_vertex = [-1 for _ in range(self._vertex_num)]  # 节点的前驱节点
        visited = [False for _ in range(self._vertex_num)]

        self.recursion_dfs(prev_vertex, visited, vertex_one, vertex_two)
        self.print_bfs(prev_vertex, vertex_one, vertex_two)


    def recursion_dfs(self, prev_vertex, visited, vertex_one, vertex_two):
        """
        递归实现
        :param prev_vertex:
        :param visited:
        :param vertex_one:
        :param vertex_two:
        :return:
        """
        if self._found:
            return

        visited[vertex_one] = True

        if vertex_one == vertex_two:
            self._found = True
            return

        for vertex in self._adjacency_table[vertex_one]:
            if not visited[vertex]:
                prev_vertex[vertex] = vertex_one
                self.recursion_dfs(prev_vertex, visited, vertex, vertex_two)



if __name__ == '__main__':
    var_list = [1, 2, 3, 5]
    undirected_graph = UndirectedGraph(var_list)
    undirected_graph.table_save_edge(1, 2)
    undirected_graph.table_save_edge(1, 5)
    undirected_graph.table_save_edge(2, 3)
    undirected_graph.table_save_edge(2, 5)
    undirected_graph.table_save_edge(3, 5)

    undirected_graph.matrix_save_edge(1, 2)
    undirected_graph.matrix_save_edge(1, 5)
    undirected_graph.matrix_save_edge(2, 3)
    undirected_graph.matrix_save_edge(2, 5)
    undirected_graph.matrix_save_edge(3, 5)

    undirected_graph.print_table()
    undirected_graph.print_matrix()

    undirected_graph.breadth_first_find(1, 3)
    print('')

    undirected_graph.depth_first_find(1, 3)


# class DirectedGraph:
#     """有向图"""
#
#     def __init__(self, param_list: tp.List[int]):
#         self._adjacency_matrix = np.zeros((max(param_list) + 1, max(param_list) + 1))
#         self._adjacency_table = [[] for _ in range(max(param_list) + 1)]
#
#     def matrix_save_edge(self, vertex_one, vertex_two):
#         """
#         邻接矩阵:有向图中每条边存储一次
#         :param vertex_one:
#         :param vertex_two:
#         :return:
#         """
#         self._adjacency_matrix[vertex_one][vertex_two] = 1
#
#     def table_save_edge(self, vertex_one, vertex_two):
#         """
#         邻接表:有向图中每条边存储一次
#         :param vertex_one:
#         :param vertex_two:
#         :return:
#         """
#         self._adjacency_table[vertex_one].append(vertex_two)
#
#     def print_table(self):
#         """
#         打印邻接表
#         :return:
#         """
#         print(self._adjacency_table)
#
#     def print_matrix(self):
#         """
#         打印邻接矩阵
#         :return:
#         """
#         print(self._adjacency_matrix)
#
#
# if __name__ == '__main__':
#     var_list = [1, 2, 3, 5]
#     directed_graph = DirectedGraph(var_list)
#     directed_graph.table_save_edge(1, 2)
#     directed_graph.table_save_edge(1, 5)
#     directed_graph.table_save_edge(2, 3)
#     directed_graph.table_save_edge(5, 2)
#     directed_graph.table_save_edge(5, 3)
#
#     directed_graph.matrix_save_edge(1, 2)
#     directed_graph.matrix_save_edge(1, 5)
#     directed_graph.matrix_save_edge(2, 3)
#     directed_graph.matrix_save_edge(5, 2)
#     directed_graph.matrix_save_edge(5, 3)
#
#     directed_graph.print_table()
#     directed_graph.print_matrix()