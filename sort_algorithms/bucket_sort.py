import typing as tp


def bucket_sort(params: tp.List[int]):
    """
    桶排序
    :param params:
    :return:
    """
    max_value = max(params)
    min_value = min(params)
    params_len = len(params)

    interval = (max_value - min_value) / (params_len - 1)  # 表示每个桶所装元素的间隔
    bucket_list = [[] for _ in range(params_len)]  # 表示桶的个数，每个桶用列表表示

    # 元素分别装桶
    for param in params:
        index = int(param / interval - 1)
        if index < 0:
            index = 0
        bucket_list[index].append(param)

    temp_list = []
    for sub_list in bucket_list:
        sub_list.sort()
        temp_list.extend(sub_list)

    params[:] = temp_list[:]


if __name__ == '__main__':
    var_list = [3, 12, 8, 20, 5, 9, 15]
    bucket_sort(var_list)
    print(var_list)
