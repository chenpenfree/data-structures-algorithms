import typing as tp


def selection_sort(param: tp.List[int]):
    """选择排序:升序"""
    
    param_len = len(param)
    if param_len == 0 or param_len == 1:
        return
   
    for i in range(param_len):
        min_index = i
        for j in range(min_index, param_len):
            if param[j] < param[min_index]:
                min_index = j
        param[i], param[min_index] = param[min_index], param[i]
        
        
if __name__ == '__main__':
    #var_list = [1, 9, 4, 2, 7, 8, 6]
    var_list = [1, 9, 4, 2, 7, 8]
    selection_sort(var_list)
    print(var_list)
      
