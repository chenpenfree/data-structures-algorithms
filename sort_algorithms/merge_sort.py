from typing import List


def merge_sort(param: List[int]):
    """
    归并排序，递归实现，升序
    :param param:
    :return 
    """
    list_len = len(param)
    sort(param, 0, list_len - 1)
    
def sort(param: List[int], start_pos, end_pos):
    
    if start_pos >= end_pos:
        return
        
    middle_pos = (start_pos + end_pos) >> 1
    sort(param, start_pos, middle_pos)
    sort(param, middle_pos + 1, end_pos)
    
    merge(param, start_pos, middle_pos, end_pos)
    
def merge(param, start_pos, middle_pos, end_pos):
    temp_list = []
    start_index = start_pos
    end_index = middle_pos + 1
    
    while start_index <= start_pos and end_index <= end_pos:
        if param[start_index] > param[end_index]:
            temp_list.append(param[end_index])
            end_index += 1
        else:
            temp_list.append(param[start_index])
            start_index += 1
            
    if start_index > middle_pos:
        temp_list += param[end_index: end_pos + 1]
    if end_index > end_pos:
        temp_list += param[start_index: middle_pos + 1]
    
    param[start_pos: end_pos + 1] = temp_list


    
    
if __name__ == '__main__':
    var_list = [9,5, 8, 6, 1, 3, 2]
    merge_sort(var_list)
    print(var_list)
