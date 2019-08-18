import typing as tp


MIN_EDIT_DISTANCE = float('inf')
str_list1 = 'mitcmu'
str_list2 = 'mtacnu'
len1 = len(str_list1)
len2 = len(str_list2)


def str_compare_trace_back(str1, index1, str2, index2, distance):
    """
    回溯法：莱文斯坦距离求解两个字符串的最小编辑距离
    :param str1:
    :param index1:
    :param str2:
    :param index2:
    :param distance:
    :return:
    """
    if index1 == len1 or index2 == len2:
        if index1 < len1:  # 当两个字符串不是同时到达末尾时，剩余的不匹配需要加在编辑距离上
            distance += len1 - index1
        if index2 < len2:
            distance += len2 - index2
        global MIN_EDIT_DISTANCE
        if distance < MIN_EDIT_DISTANCE :  # 最小编辑距离
            MIN_EDIT_DISTANCE = distance
        return

    # 每个决策阶段有两种可能:相等、不相等
    if str1[index1] == str2[index2]:
        str_compare_trace_back(str1, index1+1, str2, index2+1, distance)  # 相等编辑距离不变
    else:
        str_compare_trace_back(str1, index1+1, str2, index2, distance+1)  # str1删除字符或者str2增加一个字符
        str_compare_trace_back(str1, index1, str2, index2+1, distance+1)  # str2删除字符或者str1增加一个字符
        str_compare_trace_back(str1, index1+1, str2, index2+1, distance+1)  # 将str1[index1]或者str[2]替换


def str_compare_dynamic_programming(str1, str2):
    """
    动态规划: 莱文斯坦距离求解两个字符串的最小编辑距离
    状态 (i, j) 可能从 (i-1, j)，(i, j-1)三个状态中的任意一个转移过来
    :param str1:
    :param str2:
    :return:
    """
    str1_len1 = len(str1)  # 行
    str2_len2 = len(str2)  # 列
    status = [[-1 for _ in range(str2_len2)] for _ in range(str1_len1)]

    for i in range(str2_len2):  # 列
        if str1[0] == str2[i]:
            status[0][i] = i
        elif i != 0:  # 不相等
            status[0][i] = status[0][i-1] + 1
        else:
            status[0][i] = 1

    for j in range(str1_len1):  # 行
        if str2[0] == str1[j]:
            status[j][0] = j
        elif j != 0:
            status[j][0] = status[j-1][0] + 1
        else:
            status[j][0] = 1

    for i in range(1, str1_len1):  # 行
        for j in range(1, str2_len2):  # 列
            if str1[i] == str2[j]:
                status[i][j] = min(status[i-1][j]+1, status[i][j-1]+1, status[i-1][j-1])
            else:
                status[i][j] = min(status[i-1][j]+1, status[i][j-1]+1, status[i-1][j-1]+1)

    return status[str1_len1-1][str2_len2-1]


def str_compare_max_len_sub_str(str1, str2):
    """
    动态规划：最长公共子串长度求最大相似度
    :param str1:
    :param str2:
    :return:
    """
    str1_len = len(str1)  # 行
    str2_len = len(str2)  # 列
    status = [[-1 for _ in range(str2_len)] for _ in range(str1_len)]

    # 初始化
    for i in range(str2_len):  # 列
        if str1[0] == str2[i]:
            status[0][i] = 1
        elif i != 0:
            status[0][i] = status[0][i-1]
        else:
            status[0][i] = 0

    for j in range(str2_len):  # 行
        if str1[j] == str2[0]:
            status[j][0] = 1
        elif j != 0:
            status[j][0] = status[j-1][0]
        else:
            status[j][0] = 0

    for i in range(1, str1_len):
        for j in range(1, str2_len):
            if str1[i] == str2[j]:
                status[i][j] = max(status[i-1][j], status[i][j-1], status[i-1][j-1]+1)
            else:
                status[i][j] = max(status[i-1][j], status[i][j-1], status[i-1][j-1])

    return status[str1_len-1][str2_len-1]


if __name__ == '__main__':
    # 初始化两个字符串初始索引为0，编辑距离初始为0.
    # str_compare_trace_back(str_list1, 0, str_list2, 0, 0)
    # print(MIN_EDIT_DISTANCE)
    # result = str_compare_dynamic_programming(str_list1, str_list2)
    result = str_compare_max_len_sub_str(str_list1, str_list2)
    print(result)