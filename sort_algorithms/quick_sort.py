import typing


def quick_sort(var_list: typing.List[int]):
    """快速排序"""
    
    var_list_len = len(var_list)
    
    if var_list_len == 0 or var_list_len == 1:
        return var_list
    
    sort(var_list, 0, var_list_len)
    
    return var_list

def sort(var_list: typing.List[int], start_position, end_position):
    """递归实现"""
    
    if end_position <= start_position:
        return
    
    pivot_index = partition(var_list, start_position, end_position)  # 支点索引
    
    sort(var_list, start_position, pivot_index - 1)
    sort(var_list, pivot_index + 1, end_position)
    
def partition(var_list: typing.List[int], start_position, end_position):
    """获取分割点：单边扫描，选取最后一个元素为基点"""
    
    pivot_value = var_list[end_position]
    mark = start_position
    
    for i in range(start_position, end_position):
        if var_list[i] < pivot_value:
            var_list[i], var_list[mark] = var_list[mark], var_list[i]
            mark += 1
            
    var_list[mark], var_list[end_position] = var_list[end_position], var_list[mark]
    
    return mark
