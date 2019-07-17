import typing as tp
import numpy as np


class UndirectedGraph:
    """无向图"""

    def __init__(self, vertex_num: int):
        self._vertex_num = vertex_num
        self._adjacency_matrix = np.zeros((vertex_num, vertex_num))  # 邻接矩阵
        self._adjacency_table = [[] for _ in range(vertex_num)]  # 邻接表