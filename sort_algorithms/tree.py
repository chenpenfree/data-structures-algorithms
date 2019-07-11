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

    def target_node_next(self, data):
        """
        目标节点的后继节点
        :param data:
        :return:
        """
        if self.__tree is None:
            return

        temp_node = self.__tree
        while temp_node:
            if temp_node.data == data:
                break
            elif temp_node.data > data:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        result_list = []
        if temp_node.left:
            result_list.append(temp_node.left.data)
        if temp_node.right:
            result_list.append(temp_node.right.data)

        return result_list

    def target_node_before(self, data):
        """
        目标节点之前的节点
        :param data:
        :return:
        """
        if self.__tree is None:
            return

        parent_node = None
        temp_node = self.__tree
        while temp_node:
            if temp_node.data == data:
                break
            elif temp_node.data < data:
                parent_node = temp_node
                temp_node = temp_node.right
            else:
                parent_node = temp_node
                temp_node = temp_node.left

        if parent_node is None or temp_node is None:  # 根节点没有父节点
            return

        return parent_node.data

    def invert_tree(self):
        """
        二叉树翻转：按层遍历
        :return:
        """
        if self.__tree is None:
            return

        list_queue = [self.__tree]
        while len(list_queue) > 0:
            temp_node = list_queue.pop(0)
            if temp_node.left:
                list_queue.append(temp_node.left)
            if temp_node.right:
                list_queue.append(temp_node.right)

            temp_node.left, temp_node.right = temp_node.right, temp_node.left

    def invert_tree_recursion(self):
        """
        二叉树翻转：递归实现
        :return:
        """
        if self.__tree is None:
            return

        self.__invert_tree_recursion(self.__tree)

    def __invert_tree_recursion(self, node):

        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.__invert_tree_recursion(node.left)
        self.__invert_tree_recursion(node.right)

    def max_depth(self):
        """
        树的最大深度，二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
        :return:
        """
        if self.__tree is None:
            return 0

        list_queue = [self.__tree]
        level = 0

        while list_queue:
            for node in range(len(list_queue)):
                temp_node = list_queue.pop(0)

                if temp_node.left:
                    list_queue.append(temp_node.left)
                if temp_node.right:
                    list_queue.append(temp_node.right)
            level += 1

        return level

    def has_sum_path(self,num: int) -> bool:
        """
        求是否存在满足num的路径
        :param num:
        :return:
        """
        temp_node = self.__tree
        return self._has_sum_path(temp_node, num)

    def _has_sum_path(self, node, num: int) -> bool:
        if node is None:
            return False

        if not node.left and not node.right:
            return node.data == num

        return self._has_sum_path(node.left, num - node.data) or self._has_sum_path(node.right, num - node.data)


if __name__ == '__main__':
    var_list = [1, 9, 3, 0, 6, 5, 7]
    binary_search_tree = BinarySearchTree()
    for value in var_list:
        binary_search_tree.insert(value)

    binary_search_tree.display_tree()
    level_node = binary_search_tree.display_tree_accord_level()
    print(level_node)

    print(binary_search_tree.max_depth())
    # binary_search_tree.invert_tree()
    binary_search_tree.invert_tree_recursion()
    level_node = binary_search_tree.display_tree_accord_level()
    print(level_node)


    # search_node = binary_search_tree.find(9)
    # print(search_node)
    # print(binary_search_tree.target_node_next(1))
    # print(binary_search_tree.target_node_before(10))

    # binary_search_tree.delete(3)
    # binary_search_tree.display_tree()
    # level_node = binary_search_tree.display_tree_accord_level()
    # print(level_node)

    # print(binary_search_tree.pre_order_traversal())
    # print(binary_search_tree.in_order_traversal())
    # print(binary_search_tree.post_order_traversal())
