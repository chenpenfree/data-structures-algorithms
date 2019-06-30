import queue


class Node:
    """
    树的节点
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    二叉查找树
    """

    def __init__(self):
        self.__tree = None

    def insert(self, data):
        """
        插入数据
        :param data:
        :return:
        """
        if self.__tree is None:
            self.__tree = Node(data)
            return

        temp_node = self.__tree
        while temp_node:
            if temp_node.data < data:
                if temp_node.right is None:
                    temp_node.right = Node(data)
                    return
                temp_node = temp_node.right
            else:
                if temp_node.left is None:
                    temp_node.left = Node(data)
                    return
                temp_node = temp_node.left

    def display_tree(self):
        """
        按层遍历树
        :return:
        """
        if self.__tree is None:
            return

        print_queue = queue.Queue()

        print_queue.put(self.__tree)
        temp_node = print_queue.get()
        while temp_node:
            print(temp_node.data)
            if temp_node.left:
                print_queue.put(temp_node.left)
            if temp_node.right:
                print_queue.put(temp_node.right)

            if print_queue.empty():
                break
            temp_node = print_queue.get()


if __name__ == '__main__':
    var_list = [1, 9, 3, 0, 6, 5, 7]
    binary_search_tree = BinarySearchTree()
    for value in var_list:
        binary_search_tree.insert(value)

    binary_search_tree.display_tree()


