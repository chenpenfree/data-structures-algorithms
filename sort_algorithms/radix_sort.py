import typing as tp
import time


def radix_sort(params: tp.List[int]):
    """
    基数排序
    :param params:
    :return:
    """
    max_value = max(params)
    temp_list = []
    bucket_list = [[] for _ in range(10)]

    power_num = 1
    while True:
        radix_num = pow(10, power_num - 1)
        if max_value < radix_num:  # 循环终止条件
            break

        for param in params:  # 数据入桶
            bucket_list[(param // radix_num) % 10].append(param)

        for sub_list in bucket_list:
            temp_list.extend(sub_list)
            sub_list.clear()

        params[:] = temp_list[:]
        power_num += 1
        temp_list.clear()


if __name__ == '__main__':
    start = time.perf_counter()
    # start1 = time.clock()

    var_list = [231, 432, 576, 245, 325, 19]
    # var_list = [9, 2, 1, 8, 7, 5]
    radix_sort(var_list)

    end = time.perf_counter()
    # end1 = time.clock()
    print(var_list)
    # print('耗时：', end1 - start1)
    print('耗时：', end - start)
