import typing as tp


MAX_VALUE = float('-inf')

def  back_tracking(params: tp.List[int], weights, num, actual_weight, index):
    """
    回溯算法(即：穷举搜索),递归实现
    :param params: 数组
    :param weights: 背包重量
    :param num: 物品个数
    :param actual_weight: 实际重量
    :param index: 物品索引
    :return: 满足条件的最大重量
    """

    if actual_weight == weights or index == num:  # 背包装满或者物品考察完毕
        global MAX_VALUE
        if actual_weight > MAX_VALUE:
            MAX_VALUE = actual_weight
        return

    # 第index个物品不装
    back_tracking(params, weights, num, actual_weight, index+1)
    # 第index个物品装包
    if actual_weight + params[index] <= weights:
        back_tracking(params, weights, num, actual_weight+params[index], index + 1)


# 5为素组元素个数，10为背包容量加1
back_tracking_status = [[False for _ in range(10)] for _ in range(5)]
def  back_tracking_update(params: tp.List[int], weights, num, actual_weight, index):
    """
    回溯算法(即：穷举搜索),递归实现,避免重复计算
    :param params: 数组
    :param weights: 背包重量
    :param num: 物品个数
    :param actual_weight: 实际重量
    :param index: 物品索引
    :return: 满足条件的最大重量
    """

    if actual_weight == weights or index == num:  # 背包装满或者物品考察完毕
        global MAX_VALUE
        if actual_weight > MAX_VALUE:
            MAX_VALUE = actual_weight
        return

    if back_tracking_status[index][actual_weight]:
        return
    back_tracking_status[index][actual_weight] = True

    # 第index个物品不装
    back_tracking(params, weights, num, actual_weight, index+1)
    # 第index个物品装包
    if actual_weight + params[index] <= weights:
        back_tracking(params, weights, num, actual_weight+params[index], index + 1)


def dynamic_programming(params: tp.List[int], weights):
    """
    动态规划
    :param params:
    :param weights:
    :return:
    """
    params_len = len(params)

    # 5为素组元素个数，10为背包容量加1
    dynamic_programming_status = [[False for _ in range(10)] for _ in range(5)]

    # 第一个元素特殊处理
    dynamic_programming_status[0][0] = True
    if params[0] <= weights:
        dynamic_programming_status[0][params[0]] = True

    # 剩下的其他元素，则根据前面的状态推
    for i in range(1, params_len):
        # 第i个元素不装包
        for j in range(weights+1):
            if dynamic_programming_status[i-1][j]:
                dynamic_programming_status[i][j] = dynamic_programming_status[i-1][j]

        # 第i个元素装包
        for k in range(weights+1-params[i]):
            if dynamic_programming_status[i-1][k]:
                dynamic_programming_status[i][k+params[i]] = True

    for weight in reversed(range(weights+1)):
        if dynamic_programming_status[params_len-1][weight]:
            return weight


def dynamic_programming_update(params: tp.List[int], weights):
    """
    动态规划：缩小空间消耗
    :param params:
    :param weights:
    :return:
    """

    status = [False for _ in range(10)]
    params_len = len(params)

    # 初始化初始状态
    status[0] = True
    if params[0] <= weights:
        status[params[0]] = True

    for i in range(1, params_len):
        # for j in range(weights - params[i] + 1):  # 会重复计算
        for j in reversed(range(weights-params[i]+1)):
            if status[j]:
                status[j+params[i]] = True

    for weight in reversed(range(weights+1)):
        if status[weight]:
            return weight




if __name__ == '__main__':
    var_list = [2, 2, 4, 6, 3]
    var_weights = 9
    var_num = len(var_list)
    # back_tracking(var_list, var_weights, var_num, 0, 0)
    # back_tracking_update(var_list, var_weights, var_num, 0, 0)
    # print(MAX_VALUE)
    # result = dynamic_programming(var_list, var_weights)
    result = dynamic_programming_update(var_list, var_weights)
    print(result)