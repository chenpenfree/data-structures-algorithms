from typing import 


def bubble_sort(var_list: List[int]):
  """
  冒泡排序，从左到右，小值冒泡。
  ：param var_list: 列表
  ：return:
  """
  
  length = len(var_list)
  
  for i in range(length):
    order_flag = True  # 是否有序标志
    for j in range(length-i-1):
      if var_list[j] <= var_list[j+1]:
        var_list[j], var_list[j+1] = var_list[j+1], var_list[j]
        order_flag = False
        
      if order_flag:
        return
        
        
if __name__ == '__main__':
  temp_list = [1, 9, 2, 6, 4, 8, 0]
  temp_list = [9, 8, 6, 4, 2, 1, 0]
  bubble_sort(temp_list)
  print(temp_list)
