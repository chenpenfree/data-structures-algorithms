import typing as tp


MAX_VALUE = float('-inf')
WEIGHT = 9
PARAM_LEN = 5

def back_tracking(weights: tp.List[int], values: tp.List[int], weight, value, index):
    """
    回溯法
    :param weights:
    :param values:
    :param weight: 当前背包中物品的重量
    :param value: 当前背包中物品的价值
    :param index:
    :return:
    """

    if weight == WEIGHT or index == PARAM_LEN:  # 递归终止条件
        global MAX_VALUE
        if value > MAX_VALUE:
            MAX_VALUE = value
        return

    # 第index个元素不装包
    back_tracking(weights, values, weight, value, index+1)

    # 第index个元素装包
    if weight + weights[index] <= WEIGHT:
        back_tracking(weights, values, weight+weights[index], value+values[index], index + 1)


def dynamic_programming(weights: tp.List[int], values: tp.List[int]):
    """
    动态规划：把整个求解过程分为 n 个阶段，每个阶段会决策一个物品是否放到背包中。
             每个阶段决策完之后，背包中的物品的总重量以及总价值，会有多种情况，
             也就是会达到多种不同的状态。
    :param weights:
    :param values:
    :return:
    """

    weights_len = len(weights)
    status_value = [[-1 for _ in range(10)] for _ in range(weights_len)]

    # 初始化初始状态
    status_value[0][0] = 0
    if weights[0] <= WEIGHT:
        status_value[0][weights[0]] = values[0]

    for i in range(weights_len):
        # 第i个元素不装包
        for j in range(WEIGHT+1):
            if status_value[i-1][j] >= 0:
                status_value[i][j] = status_value[i-1][j]

        # 第i个元素装包
        for j in range(WEIGHT-weights[i]+1):
            if status_value[i-1][j] >= 0:
                temp_value = values[i] + status_value[i-1][j]
                if temp_value > status_value[i][j+weights[i]]:
                    status_value[i][j + weights[i]] = temp_value

    max_value = -1
    for k in range(WEIGHT+1):
        if status_value[weights_len-1][k] > max_value:
            max_value = status_value[weights_len-1][k]

    return max_value


def dynamic_programming_update(weights: tp.List[int], values: tp.List[int]):
    """
    动态规划：少内存方式
    :param weights:
    :param values:
    :return:
    """
    weights_len = len(weights)
    if weights_len == 0:
        return

    status = [-1 for _ in range(WEIGHT+1)]
    status[0] = 0
    if weights[0] <= WEIGHT:
        status[weights[0]] = values[0]

    for i in range(1, weights_len):
        for j in reversed(range(WEIGHT-weights[i]+1)):
            if status[j] > -1:
                temp_value = status[j] + values[i]
                if status[j + weights[i]] < temp_value:
                    status[j + weights[i]] = temp_value

    for k in range(WEIGHT+1):
        global MAX_VALUE
        if status[k] > MAX_VALUE:
            MAX_VALUE = status[k]

    return MAX_VALUE



if __name__ == '__main__':
    var_weight = [2, 2, 4, 6, 3]
    var_value = [3, 4, 8, 9, 6]
    # back_tracking(var_weight, var_value, 0, 0, 0)
    # result = dynamic_programming(var_weight, var_value)
    result = dynamic_programming_update(var_weight, var_value)
    print(result)