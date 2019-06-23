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


if __name__ == '__main__':
    # var_array = [4, 6, 3, 9, 1, 2]
    var_array = [4, 6, 3, 9, 1, 2, 3]
    # var_array = [1, 2, 3, 4, 6, 9]
    # heap_sort(var_array)
    build_heap_func(var_array, len(var_array))
    print(var_array)
