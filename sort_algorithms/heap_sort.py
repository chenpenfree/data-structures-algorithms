from typing import List


# **********递归堆排序**************************
def heap_sort(var_list: List[int]):
    """
    堆排序，大顶堆(优先级队列)
    """
    length = len(var_list)
    if length == 0 or length == 1:
        return

    build_heap(var_list, length)  # 建堆
    for i in reversed(range(1, length)):
        var_list[0], var_list[i] = var_list[i], var_list[0]  # 队首元素和对尾元素交换
        sort(var_list, 1, i)  # 堆化


def build_heap(var_list: List[int], len_list: int):
    """
    建堆
    """
    max_index = int(len_list / 2) + 1
    for i in reversed(range(1, max_index)):
        sort(var_list, i, len_list)


def sort(var_list: List[int], index: int, len_list: int):
    """
    下沉堆化（递归）
    """
    left_node = 2 * index
    right_node = 2 * index + 1
    temp_index = index

    if left_node <= len_list and var_list[left_node - 1] > var_list[temp_index - 1]:
        temp_index = left_node

    if right_node <= len_list and var_list[right_node - 1] > var_list[temp_index - 1]:
        temp_index = right_node

    if temp_index != index:
        var_list[index - 1], var_list[temp_index - 1] = var_list[temp_index - 1], var_list[index - 1]
        sort(var_list, temp_index, len_list)  # 递归堆化


# **************循环堆排序**********************
def build_heap_func(param_list: List[int], len_list: int):
    """
    建堆
    :param param_list: 数组
    :param len_list: 数组长度
    :return:
    """
    parent_node_index = int(len_list/2)
    for i in reversed(range(parent_node_index)):
        big_top_heap(param_list, i, len_list)  # 大顶堆
        # small_top_heap(param_list, i, len_list)  # 小顶堆


def small_top_heap(param_list: List[int], node_index: int, len_list: int):
    """
    小顶堆
    :param param_list: 数组
    :param node_index:  节点索引
    :param len_list:  数组长度
    :return:
   """
    while True:
        min_index = node_index
        if 2 * node_index + 1 < len_list and param_list[2 * node_index + 1] < param_list[min_index]:
            min_index = 2 * node_index + 1

        if 2 * node_index + 2 < len_list and param_list[2 * node_index + 2] < param_list[min_index]:
            min_index = 2 * node_index + 2

        if min_index == node_index:
            break

        param_list[node_index], param_list[min_index] = param_list[min_index], param_list[node_index]

        # 从上往下堆化
        node_index = min_index


def big_top_heap(param_list: List[int], node_index: int, len_list: int):
    """
    大顶堆
    :param param_list: 数组
    :param node_index: 节点索引
    :param len_list: 数组长度
    :return:
    """
    while True:
        max_index = node_index
        if 2 * node_index + 1 < len_list and param_list[2 * node_index + 1] > param_list[max_index]:
            max_index = 2 * node_index+1

        if 2 * node_index+2 < len_list and param_list[2  *node_index + 2] > param_list[max_index]:
            max_index = 2 * node_index + 2

        if max_index == node_index:
            break

        param_list[node_index], param_list[max_index] = param_list[max_index], param_list[node_index]

        # 从上往下堆化
        node_index = max_index


def heap_sort_func(param_list: List[int]):
    """
    堆排序(从小到大)
    :param param_list:
    :return:
    """
    length = len(param_list)
    build_heap_func(param_list, length)
    # print(param_list)
    temp_index = length - 1

    while temp_index > 0:
        param_list[0], param_list[temp_index] = param_list[temp_index], param_list[0]
        big_top_heap(param_list, 0, temp_index)
        temp_index -= 1


# ****************最大topK************************
class FindTopK:

    def __init__(self, top_k: int):
        self._top_k = top_k
        self._top_k_list = []
        self._list = []
        self._count = 0

    def insert(self, param: int):
        """
        插入数据
        :param param:
        :return:
        """
        self._list.append(param)

        if self._count == self._top_k:
            # 将值赋给堆顶元素，同时向下堆化
            if param > self._top_k_list[0]:
                self._top_k_list[0] = param
                temp_index = 0
                while True:
                    min_index = temp_index

                    if 2 * temp_index + 1 < self._count and self._top_k_list[2 * temp_index + 1] < self._top_k_list[min_index]:
                        min_index = 2 * temp_index + 1

                    if 2 * temp_index + 2 < self._count and self._top_k_list[2 * temp_index + 2] < self._top_k_list[min_index]:
                        min_index = 2 * temp_index + 2

                    if min_index == temp_index:
                        break

                    self._top_k_list[temp_index], self._top_k_list[min_index] = self._top_k_list[min_index], self._top_k_list[temp_index]
                    temp_index = min_index
            return

        self._top_k_list.append(param)
        self._count += 1
        node_index = self._count - 1

        while (node_index>>1) >= 0 and self._top_k_list[node_index] < self._top_k_list[(node_index>>1)]:
            self._top_k_list[node_index], self._top_k_list[(node_index>>1)] = self._top_k_list[(node_index>>1)], self._top_k_list[node_index]
            node_index = (node_index>>1)

    def delete(self, param: int):
        """
        删除数据
        :param param:
        :return:
        """

    def get_top_k(self):
        """
        最大的k个值
        :return:
        """
        return self._top_k_list

    def get_list(self):

        return self._list


if __name__ == '__main__':
    # var_array = [4, 6, 3, 9, 1, 2]
    var_array = [4, 6, 3, 9, 1, 2, 3]
    # var_array = [9, 6, 4, 3, 2, 1]
    # var_array = [1, 2, 3, 4, 6, 9]
    # heap_sort(var_array)
    # build_heap_func(var_array, len(var_array))
    # heap_sort_func(var_array)
    # print(var_array)
    top_k_class = FindTopK(4)
    for i in var_array:
        top_k_class.insert(i)
    top_k_class.insert(10)
    top_k_class.insert(1)
    print(top_k_class.get_top_k())
    print(top_k_class.get_list())
