import typing as tp


def count_sort(params: tp.List[int]):
    """
    计数排序：适用于正整数并且取值范围相差不大的数组
    :param params:
    :return:
    """
    max_value = max(params)
    count_list = [0 for _ in range(max_value + 1)]  # 计数列表

    for param in params:
        count_list[param] += 1

    params_index = 0
    for i in range(max_value + 1):
        if count_list[i] > 0:
            count_list[i] -= 1
            params[params_index] = i
            params_index += 1
            while count_list[i] > 0:
                params[params_index] = i
                params_index += 1
                count_list[i] -= 1


def count_sort_in_place(params: tp.List[int]):
    """
    计数排序：原地排序
    :param params:
    :return:
    """
    max_value = max(params)
    count_list = [0 for _ in range(max_value + 1)]

    for param in params:
        count_list[param] += 1

    for i in range(1, max_value + 1):  # 元素个数累加，得到排名序号
        count_list[i] = count_list[i] + count_list[i - 1]

    temp_list = [0 for _ in range(len(params))]
    for param in reversed(params):  # 倒序访问
        temp_list[count_list[param] - 1] = param
        count_list[param] -= 1

    params[:] = temp_list[:]


if __name__ == '__main__':
    var_list = [8, 2, 3, 5, 8, 2, 5, 4, 5, 5]
    # var_list = [3, 5, 8, 2, 5, 4]
    # count_sort(var_list)
    count_sort_in_place(var_list)
    print(var_list)
