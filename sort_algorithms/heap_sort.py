from typing import List


def heap_sort(var_list: List[int]):
  """
  堆排序，大顶堆(优先级队列)
  """
  length = len(var_List)
  if length == 0 or length == 1:
    return
  
  build_heap(var_list, length)  #建堆
  for i in reversed(range(1, length)):
    var_list[0], var_list[i] = var_list[i], var_list[0]  # 队首元素和对尾元素交换
    sort(var_list, 1, i)  # 堆化
    
    
def build_heap(var_list: List[int], len_list: int):
  """
  建堆
  """
  max_index = int(len_list/2) + 1
  for i in reversed(range(1, max_index)):
    sort(var_list, i. len_list)
    
    
def sort(var_list: List[int], index: int, len_list: int):
  """
  下沉堆化
  """
  left_node = 2*index
  right_node = 2*index + 1
  temp_index = index
  
  if left_node <= len_list and var_list[left_node-1] > var_list[temp_index-1]:
    temp_index = left_node
    
  if right_node <= len_list and var_list[right_node -1] > var_list[temp_index-1]:
    temp_index = right_node
    
  if temp_index != index:
    var_list[index-1], var_list[temp_index-1] = var_list[temp_index-1], var_list[index-1]
    sort(var_list, temp_index, len_list)  # 递归堆化
    
    
if __name__ == '__main__':
  var_array = [4, 6, 3, 9, 1, 2]
  heap_sort(var_array)
  print(var_array)
