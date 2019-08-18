import typing as tp


def min_coin_num(money_list: tp.List[int], money):
    """
    动态规划：状态转移表法
    :param money_list:
    :param money:
    :return:
    """

    if money in money_list:
        return 1

    # 状态数组
    status = [[False for _ in range(money+1)] for _ in range(money)]

    # 初始化状态数组
    for value in money_list:
        if value < money:
            status[0][value] = True

    count = 0
    for i in range(money):
        for j in range(money+1):
            if not status[i-1][j]:
                continue

            for value in money_list:
                if j + value <= money:
                    status[i][j+value] = True

            if status[i][money]:
                count = i + 1
                break

        if count > 0:
            break

    return count



if __name__ == '__main__':
    var_list = [1, 3, 5]
    var_money = 9
    result = min_coin_num(var_list, var_money)
    print('')
    print(result)
