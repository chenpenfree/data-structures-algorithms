import typing as tp


def shell_sort(param: tp.List[int]):
    """希尔排序"""
    
    param_len = len(param)
    if param_len == 0 or param_len == 1:
        return
        
    gap = param_len >> 1  # 获取区间
    
    while gap >= 1:
        for i in range(gap, param_len):
            temp_value = param[i]
            j = i - gap
            while j >= 0 and param[j] > temp_value:  # 右移数据
                param[j+gap] = param[j]
                j -= gap
            param[j+gap] = temp_value  # 前面多减了一个gap
        gap -=1  # 缩小区间
        
        
if __name__ == '__main__':
    var_list = [9, 2, 6, 1, 0, 8, 7]
    shell_sort(var_list)
    print(var_list)
