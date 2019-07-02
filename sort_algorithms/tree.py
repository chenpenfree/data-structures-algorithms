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

    def find(self, data):

        temp_node = self.__tree

        while temp_node:
            if temp_node.data == data:
                return temp_node.data
            if temp_node.data < data:
                temp_node = temp_node.right
            else:
                temp_node = temp_node.left

    def delete(self, data):
        """
        分三种情况：删除节点无子节点，有一个子节点，有两个子节点
        :param data:
        :return:
        """

        if self.__tree is None:
            return

        parent_node = None
        target_node = self.__tree
        while target_node and target_node.data != data:  # 查找目标节点
            parent_node = target_node
            if target_node.data < data:
                target_node = target_node.right
            else:
                target_node = target_node.left

        if target_node is None:  # 没找到
            return

        # 目标节点有两个子节点，转化为目标节点只有一个或者没有子节点，
        # 为了保持二叉查找树将右子树最小节点赋目标节点
        if target_node.left and target_node.right:
            min_left_node = target_node.right
            min_left_node_parent = target_node

            while min_left_node.left:
                min_left_node_parent = min_left_node
                min_left_node = min_left_node.left
            target_node.data = min_left_node.data
            target_node = min_left_node
            parent_node = min_left_node_parent

        child = None
        if target_node.left:
            child = target_node.left
        if target_node.right:
            child = target_node.right

        if parent_node is None:  # 对应根节点只有一个子节点
            self.__tree = child
        elif parent_node.left == target_node:
            parent_node.left = child
        else:
            parent_node.right = child

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
            print(temp_node.data, end='')
            if temp_node.left:
                print_queue.put(temp_node.left)
            if temp_node.right:
                print_queue.put(temp_node.right)

            if print_queue.empty():
                print('')
                break
            temp_node = print_queue.get()

    def display_tree_accord_level(self):

        if self.__tree is None:
            return

        node_per_level = [self.__tree]
        node_the_tree = []

        while node_per_level:
            temp_list = []
            length = len(node_per_level)
            for _ in range(length):
                node = node_per_level.pop(0)
                temp_list.append(node.data)
                if node.left:
                    node_per_level.append(node.left)

                if node.right:
                    node_per_level.append(node.right)

            node_the_tree.append(temp_list)

        return node_the_tree

    def pre_order_traversal(self):
        """前序遍历:递归实现"""

        if self.__tree is None:
            return

        pre_order_list = []
        self.__pre_order_traversal(self.__tree, pre_order_list)
        return pre_order_list

    def post_order_traversal(self):
        """前序遍历:递归实现"""

        if self.__tree is None:
            return

        post_order_list = []
        self.__post_order_traversal(self.__tree, post_order_list)
        return post_order_list

    def in_order_traversal(self):
        """中序遍历:递归实现"""

        if self.__tree is None:
            return

        in_order_list = []
        self.__in_order_traversal(self.__tree, in_order_list)
        return in_order_list

    def __pre_order_traversal(self, node, list_param):

        if node is None:
            return

        list_param.append(node.data)
        self.__pre_order_traversal(node.left, list_param)
        self.__pre_order_traversal(node.right, list_param)

    def __in_order_traversal(self, node, list_param):

        if node is None:
            return

        self.__in_order_traversal(node.left, list_param)
        list_param.append(node.data)
        self.__in_order_traversal(node.right, list_param)

    def __post_order_traversal(self, node, list_param):

        if node is None:
            return

        self.__post_order_traversal(node.left, list_param)
        self.__post_order_traversal(node.right, list_param)
        list_param.append(node.data)



if __name__ == '__main__':
    var_list = [1, 9, 3, 0, 6, 5, 7]
    binary_search_tree = BinarySearchTree()
    for value in var_list:
        binary_search_tree.insert(value)

    binary_search_tree.display_tree()
    level_node = binary_search_tree.display_tree_accord_level()
    print(level_node)

    search_node = binary_search_tree.find(9)
    print(search_node)

    # binary_search_tree.delete(3)
    # binary_search_tree.display_tree()
    # level_node = binary_search_tree.display_tree_accord_level()
    # print(level_node)

    print(binary_search_tree.pre_order_traversal())
    print(binary_search_tree.in_order_traversal())
    print(binary_search_tree.post_order_traversal())





