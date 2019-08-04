from typing import List
from collections import defaultdict


def is_valid_sudoku(board: List[List[str]]) -> bool:
    """
    用一个字典，分别记录行，列，和小正方形！
    行,列我们直接可以用数字表示，小正方形如何表示呢？
    这里,我们发现一个规律,我们可以把小正方形变成用二维唯一标识,比如(0,0)表示左上角那个,(1,1)表示中间那个,
    他们和行列的关系就是(i//3,j//3)，
    所以任何位置我们都能找出它在哪个行，哪个列，哪个小正方形里！
    时间复杂度都是常数级的。
    :param board:
    :return:
    """
    board_len = len(board)
    if board_len == 0:
        return False

    rows = defaultdict(set)  # 当键不存在时，初值为set
    cols = defaultdict(set)
    small_square = defaultdict(set)

    for i in range(board_len):
        for j in range(9):
            if board[i][j].isdigit():
                if board[i][j] not in rows[i] \
                        and board[i][j] not in cols[j] \
                        and board[i][j] not in small_square[(i // 3, j // 3)]:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    small_square[(i // 3, j // 3)].add(board[i][j])
                else:
                    return False

    return True


if __name__ == '__main__':
    var_param = [
        ['5','3','.','.','7','.','.','.','.'],
        ['6','.','.','1','9','5','.','.','.'],
        ['.','9','8','.','.','.','.','6','.'],
        ['8','.','.','.','6','.','.','.','3'],
        ['4','.','.','8','.','3','.','.','1'],
        ['7','.','.','.','2','.','.','.','6'],
        ['.','6','.','.','.','.','2','8','.'],
        ['.','.','.','4','1','9','.','.','5'],
        ['.','.','.','.','8','.','.','7','9']
        ]
    # var_param = [
    #     ['8','3','.','.','7','.','.','.','.'],
    #     ['6','.','.','1','9','5','.','.','.'],
    #     ['.','9','8','.','.','.','.','6','.'],
    #     ['8','.','.','.','6','.','.','.','3'],
    #     ['4','.','.','8','.','3','.','.','1'],
    #     ['7','.','.','.','2','.','.','.','6'],
    #     ['.','6','.','.','.','.','2','8','.'],
    #     ['.','.','.','4','1','9','.','.','5'],
    #     ['.','.','.','.','8','.','.','7','9']
    # ]
    print(isValidSudoku(var_param))
