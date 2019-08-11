import typing


def quick_sort(var_list: typing.List[int]):
    """快速排序"""
    
    var_list_len = len(var_list)
    
    if var_list_len == 0 or var_list_len == 1:
        return var_list
    
    sort(var_list, 0, var_list_len - 1)   

def sort(var_list: typing.List[int], start_position, end_position):
    """递归实现"""
    
    if end_position <= start_position:
        return
    
    pivot_index = partition_two(var_list, start_position, end_position)  # 支点索引
    
    sort(var_list, start_position, pivot_index - 1)
    sort(var_list, pivot_index + 1, end_position)
    
def partition_one(var_list: typing.List[int], start_position, end_position):
    """获取分割点：单边扫描，选取最后一个元素为基点"""
    
    pivot_value = var_list[end_position]
    mark = start_position
    
    for i in range(start_position, end_position):
        if var_list[i] < pivot_value:
            var_list[i], var_list[mark] = var_list[mark], var_list[i]
            mark += 1
            
    var_list[mark], var_list[end_position] = var_list[end_position], var_list[mark]  # 将基点值插入分割位置
    
    return mark

def partition_two(var_list: typing.List[int], start_position, end_position):
    """获取分割点：双边扫描，选取第一个元素为基点"""

    # 取第一个位置的元素作为基准元素
    pivot = var_list[start_position]
    left = start_position
    right = end_position

    while left != right:
        # 控制right指针比较并左移
        while left < right and var_list[right] > pivot:
            right -= 1

        # 控制left指针比较并右移
        while left < right and var_list[left] <= pivot:
            left += 1

        # # 控制right指针比较并左移
        # while left < right and var_list[right] > pivot:
        #     right -= 1

        # 交换left和right指向的元素
        if left < right:
            var_list[left], var_list[right] = var_list[right], var_list[left]

    # pivot和指针重合点交换
    var_list[left], var_list[start_position] = var_list[start_position], var_list[left]

    return left


if __name__ == '__main__':
    var = [1, 9, 5, 3, 7, 4, 0]
    # var = [9, 8, 1, 2, 5, 0, 7]

    quick_sort(var)

    print(var)
