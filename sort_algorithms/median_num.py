import typing as tp


def median_num(params1: tp.List[int], params2: tp.List[int]):
    """
    两个有序数组，获取中位数。要求时间为log(m+n)
    二分查找法
    :param params1:
    :param params2:
    :return:
    """
    params1_len = len(params1)
    params2_len = len(params2)

    # 奇、偶数通用方式
    left = (params1_len + params2_len + 1) >> 1
    right = (params1_len + params2_len + 2) >> 1

    return (median_num_recursion(params1, 0, params1_len - 1, params2, 0, params2_len - 1, left)
        + median_num_recursion(params1, 0, params1_len - 1, params2, 0, params2_len - 1, right)) * 0.5

def median_num_recursion(params1, start1, end1, params2, start2, end2, median):
    """
    递归实现
    :param params1:
    :param start1:
    :param end1:
    :param params2:
    :param start2:
    :param end2:
    :param median:
    :return:
    """
    params1_len = end1 - start1 + 1
    params2_len = end2 - start2 + 1
    if params1_len > params2_len:  # 保证一定是param1先空
        median_num_recursion(params2, start2, end2, params1, start1, end1, median)

    if params1_len == 0:
        return params2[start2 + median - 1]  # 返回中位数

    if median == 1:
        return min(params1[start1], params2[start2])

    index1 = start1 + min(params1_len, median >> 1) - 1
    index2 = start2 + min(params2_len, median >> 1) - 1
    if params1[index1] > params2[index2]:
        return median_num_recursion(params1, start1, end1, params2, index2 + 1, end2, median - (index2 - start2 + 1))
    else:
        return median_num_recursion(params1, index1 + 1, end1, params2, start2, end2, median - (index1 - start1 + 1))

if __name__ == '__main__':
    # var1 = [1, 3]
    # var2 = [2]
    var1 = [1, 2]
    var2 = [3, 4]
    print(median_num(var1, var2))