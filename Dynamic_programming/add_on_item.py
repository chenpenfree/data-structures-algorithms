import typing as tp


def dynamic_programming(prices: tp.List[int], target_price):
    """
    凑单满减，动态规划实现
    超过目标价格的2倍，无意义
    :param prices:
    :param target_price:
    :return:
    """
    prices_len = len(prices)
    if prices_len == 0:
        return

    status = [[False for _ in range(2*target_price+1)] for _ in range(prices_len)]
    status[0][0] = True
    if prices[0] <= 2*target_price:
        status[0][prices[0]] = True

    for i in range(1, prices_len):
        for j in range(2*target_price+1):
            if status[i-1][j]:
                status[i][j] = status[i-1][j]

        for j in range(2*target_price-prices[i]+1):
            if status[i-1][j]:
                status[i][j+prices[i]] = True

    temp_price = 0
    for k in range(target_price, 2*target_price+1):
        if status[prices_len-1][k]:
            temp_price = k
            break

    if temp_price == 2*target_price:
        return

    for i in reversed(range(1,prices_len)):
        if temp_price - prices[i] >= 0 and status[i-1][temp_price-prices[i]]:
            temp_price = temp_price - prices[i]
            print(prices[i])

    if temp_price != 0:
        print(prices[0])


if __name__ == '__main__':
    var_price = [10, 50, 20, 30, 90, 70, 120, 150, 11, 51]
    target_price_ = 200
    dynamic_programming(var_price, target_price_)