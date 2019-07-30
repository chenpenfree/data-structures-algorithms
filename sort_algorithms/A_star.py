import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


class Point:
    """坐标点"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.cost = sys.maxsize


class RandomMap:
    """地图"""
    def __init__(self, size=50):
        self.size = size
        self.obstacle = size // 8
        self.obstacle_point = []
        self.generate_obstacle()

    def generate_obstacle(self):
        """
        产生障碍物
        :return:
        """
        self.obstacle_point.append(Point(self.size // 2, self.size // 2))
        self.obstacle_point.append(Point(self.size // 2, self.size // 2 - 1))

        for i in range(self.size//2-4, self.size//2):
            self.obstacle_point.append(Point(i, self.size-i))
            self.obstacle_point.append(Point(i, self.size-i-1))
            self.obstacle_point.append(Point(self.size-i, i))
            self.obstacle_point.append(Point(self.size-i, i-1))

        for i in range(self.obstacle-1):
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
            self.obstacle_point.append(Point(x, y))

            if np.random.rand() > 0.5: # Random boolean
                for l in range(self.size//4):
                    self.obstacle_point.append(Point(x, y+l))
            else:
                for l in range(self.size//4):
                    self.obstacle_point.append(Point(x+l, y))

    def is_obstacle(self, i ,j):
        """
        判断是否是障碍物
        :param i:
        :param j:
        :return:
        """
        for p in self.obstacle_point:
            if i==p.x and j==p.y:
                return True
        return False


class AStar:
    def __init__(self, map_param):
        self.map=map_param
        self.open_set = []  # 还没访问的点
        self.close_set = []  # 已经访问过的点

    @staticmethod
    def base_cost(p):
        x_dis = p.x
        y_dis = p.y

        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def heuristic_cost(self, p):
        x_dis = self.map.size - 1 - p.x
        y_dis = self.map.size - 1 - p.y

        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def total_cost(self, p):
        return self.base_cost(p) + self.heuristic_cost(p)

    def is_valid_point(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= self.map.size or y >= self.map.size:
            return False

        return not self.map.is_obstacle(x, y)

    @staticmethod
    def is_in_point_list(p, point_list):
        for point in point_list:
            if point.x == p.x and point.y == p.y:
                return True
        return False

    def is_in_open_list(self, p):
        return self.is_in_point_list(p, self.open_set)

    def is_in_close_list(self, p):
        return self.is_in_point_list(p, self.close_set)

    @staticmethod
    def is_start_point(p):
        return p.x == 0 and p.y ==0

    def is_end_point(self, p):
        return p.x == self.map.size-1 and p.y == self.map.size-1

    @staticmethod
    def save_image(plt_var):
        millis = int(round(time.time() * 1000))
        filename = './' + str(millis) + '.png'
        plt_var.savefig(filename)

    def process_point(self, x, y, parent):
        if not self.is_valid_point(x, y):
            return

        p = Point(x, y)
        if self.is_in_close_list(p):
            return

        # print('Process Point [', p.x, ',', p.y, ']', ', cost: ', p.cost)
        if not self.is_in_open_list(p):
            p.parent = parent
            p.cost = self.total_cost(p)
            self.open_set.append(p)

    def select_point_in_open_list(self):
        """
        选择综合路径最小点
        :return:
        """
        index = 0
        selected_index = -1
        min_cost = sys.maxsize
        for p in self.open_set:
            cost = self.total_cost(p)
            if cost < min_cost:
                min_cost = cost
                selected_index = index
            index += 1
        return selected_index

    def build_path(self, p, ax, plt, start_time):
        path = []
        while True:
            path.insert(0, p)
            if self.is_start_point(p):
                break
            else:
                p = p.parent
        for p in path:
            rec = Rectangle((p.x, p.y), 1, 1, color='g')
            ax.add_patch(rec)
            plt.draw()
            # self.save_image(plt)
        plt.show()
        end_time = time.time()
        print('===== Algorithm finish in', int(end_time - start_time), ' seconds')

    def run_and_save_image(self, ax, plt):
        start_time = time.time()

        start_point = Point(0, 0)
        start_point.cost = 0
        self.open_set.append(start_point)

        while True:
            index = self.select_point_in_open_list()  # 选择最小值
            if index < 0:
                print('No path found, algorithm failed!!!')
                return
            p = self.open_set[index]  # 取出节点
            rec = Rectangle((p.x, p.y), 1, 1, color='c')
            ax.add_patch(rec)
            # self.save_image(plt)

            if self.is_end_point(p):
                return self.build_path(p, ax, plt, start_time)

            del self.open_set[index]
            self.close_set.append(p)

            x = p.x
            y = p.y
            self.process_point(x - 1, y + 1, p)
            self.process_point(x - 1, y, p)
            self.process_point(x - 1, y - 1, p)
            self.process_point(x, y - 1, p)
            self.process_point(x + 1, y - 1, p)
            self.process_point(x + 1, y, p)
            self.process_point(x + 1, y + 1, p)
            self.process_point(x, y + 1, p)

if __name__ == '__main__':
    plt.figure(figsize=(8, 8))

    map_var = RandomMap()

    ax_var = plt.gca()  # 当前的图表和子图可以使用plt.gcf()和plt.gca()获得
    ax_var.set_xlim([0, map_var.size])
    ax_var.set_ylim([0, map_var.size])

    # 给格子上色，区分障碍物
    for i in range(map_var.size):
        for j in range(map_var.size):
            if map_var.is_obstacle(i, j):
                rec = Rectangle((i, j), width=1, height=1, color='gray')
                ax_var.add_patch(rec)
            else:
                rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
                ax_var.add_patch(rec)

    # 起点
    rec = Rectangle((0, 0), width=1, height=1, facecolor='b')
    ax_var.add_patch(rec)

    # 终点
    rec = Rectangle((map_var.size - 1, map_var.size - 1), width=1, height=1, facecolor='r')
    ax_var.add_patch(rec)

    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    # plt.show()

    a_star = AStar(map_var)
    a_star.run_and_save_image(ax_var, plt)