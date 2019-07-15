import typing as tp


def insert_sort(param: tp.List[int]):
    """
    插入排序,升序:划分有序区和无序区
    :param param:
    :return:
    """
    param_len = len(param)
    if param_len == 0 or param_len == 1:
        return

    for i in range(param_len):
        temp_value = param[i]
        temp_index = i
        for j in reversed(range(i)):
            if param[j] > temp_value:
                param[j+1] = param[j]
                temp_index = j
            else:  # 找到合适位置
                break
        param[temp_index] = temp_value


if __name__ == '__main__':
    var_list = [0, 8, 7, 3, 4, 9, 6]
    insert_sort(var_list)
    print(var_list)
