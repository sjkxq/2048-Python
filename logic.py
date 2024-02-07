# 导入所需的模块
import random
from typing import List, Tuple

import constants as c


# Task 1a: 创建新游戏矩阵并初始化为全0，然后随机添加两个2


def new_game(n: int) -> List[List[int]]:
    """
    创建一个新的n x n的游戏矩阵，并在其中随机生成两个值为2的元素。

    参数:
        n (int): 矩阵的边长

    返回:
        list[list[int]]: 初始化后的游戏矩阵
    """
    matrix: List[List[int]] = []
    for _ in range(n):
        matrix.append([0] * n)
    matrix = add_two(matrix)
    matrix = add_two(matrix)
    return matrix


# Task 1b: 在矩阵的空位置处随机添加一个值为2的元素


def add_two(mat: List[List[int]]) -> List[List[int]]:
    """
    在给定矩阵中找到一个值为0的位置，并将该位置设置为2。

    参数:
        mat (List[List[int]]): 游戏矩阵

    返回:
        List[List[int]]: 更新后包含新生成2的矩阵
    """
    a, b = random.randint(0, len(mat) - 1), random.randint(0, len(mat) - 1)
    while mat[a][b] != 0:
        a, b = random.randint(0, len(mat) - 1), random.randint(0, len(mat) - 1)
    mat[a][b] = 2
    return mat


# Task 1c: 判断游戏状态（赢、未结束或输）


def game_state(mat: List[List[int]]) -> str:
    """
    根据给定矩阵判断当前游戏的状态：'win'（胜利）、'not over'（未结束）或 'lose'（失败）。

    参数:
        mat (List[List[int]]): 游戏矩阵

    返回:
        str: 游戏状态字符串标识符
    """
    # 检查是否出现2048，如果存在则返回'win'
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'

    # 检查是否存在空格（值为0），如果有则返回'not over'
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'

    # 检查是否存在相邻且相同的元素，若有则返回'not over'
    for i in range(len(mat) - 1):
        for j in range(len(mat[0]) - 1):
            if mat[i][j] == mat[i + 1][j] or mat[i][j + 1] == mat[i][j]:
                return 'not over'

    # 检查最后一行和最后一列的相邻元素
    for k in range(len(mat) - 1):
        if mat[len(mat) - 1][k] == mat[len(mat) - 1][k + 1]:
            return 'not over'
    for j in range(len(mat) - 1):
        if mat[j][len(mat) - 1] == mat[j + 1][len(mat) - 1]:
            return 'not over'

    # 如果上述条件都不满足，则返回'lose'
    return 'lose'


# Task 2a: 矩阵按行翻转


def reverse(mat: List[List[int]]) -> List[List[int]]:
    """
    将输入矩阵按行进行镜像翻转。

    参数:
        mat (List[List[int]]): 需要翻转的矩阵

    返回:
        List[List[int]]: 翻转后的新矩阵
    """
    new: List[List[int]] = []
    for i in range(len(mat)):
        new_row = [mat[i][len(mat[0]) - j - 1] for j in range(len(mat[0]))]
        new.append(new_row)
    return new


# Task 2b: 矩阵转置


def transpose(mat: List[List[int]]) -> List[List[int]]:
    """
    将输入矩阵进行转置操作，即交换矩阵的行与列。

    参数:
        mat (List[List[int]]): 需要转置的矩阵

    返回:
        List[List[int]]: 转置后的新矩阵
    """
    new: List[List[int]] = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return new


# Task 3: 实现上、下、左、右四个方向的移动逻辑


def cover_up(mat: List[List[int]]) -> Tuple[List[List[int]], bool]:
    """
    将矩阵同一行非零元素压缩在一起，并用0填充剩余空位，同时返回是否发生合并操作的标志。

    参数:
        mat (List[List[int]]): 游戏矩阵

    返回:
        Tuple[List[List[int]], bool]: 新矩阵及合并操作完成标志
    """
    new: List[List[int]] = [[0] * c.GRID_LEN for _ in range(c.GRID_LEN)]
    done: bool = False
    for i in range(c.GRID_LEN):
        count: int = 0
        for j in range(c.GRID_LEN):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done


def merge(mat: List[List[int]], done: bool) -> Tuple[List[List[int]], bool]:
    """
    合并矩阵中相同且相邻的元素，更新矩阵并将合并操作完成标志设为True。

    参数:
        mat (List[List[int]]): 需要合并的矩阵
        done (bool): 是否已执行过合并操作

    返回:
        Tuple[List[List[int]], bool]: 更新后的新矩阵及合并操作完成标志
    """
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                done = True
    return mat, done


def up(game: List[List[int]]) -> Tuple[List[List[int]], bool]:
    """
    将矩阵向上移动一格，通过转置、压缩、合并、再压缩实现。

    参数:
        game (List[List[int]]): 当前游戏矩阵

    返回:
        Tuple[List[List[int]], bool]: 移动后的新矩阵及是否有变动标志
    """
    print("up")
    game = transpose(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(game)
    return game, done


def down(game: List[List[int]]) -> Tuple[List[List[int]], bool]:
    """
    将矩阵向下移动一格，通过转置、反转、压缩、合并、再压缩和转置实现。

    参数:
        game (List[List[int]]): 当前游戏矩阵

    返回:
        Tuple[List[List[int]], bool]: 移动后的新矩阵及是否有变动标志
    """
    print("down")
    game = reverse(transpose(game))
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return game, done


def left(game: List[List[int]]) -> Tuple[List[List[int]], bool]:
    """
    将矩阵向左移动一格，通过压缩、合并、再压缩实现。

    参数:
        game (List[List[int]]): 当前游戏矩阵

    返回:
        Tuple[List[List[int]], bool]: 移动后的新矩阵及是否有变动标志
    """
    print("left")
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    return game, done


def right(game: List[List[int]]) -> Tuple[List[List[int]], bool]:
    """
    将矩阵向右移动一格，通过反转、压缩、合并、再压缩和反转实现。

    参数:
        game (List[List[int]]): 当前游戏矩阵

    返回:
        Tuple[List[List[int]], bool]: 移动后的新矩阵及是否有变动标志
    """
    print("right")
    game = reverse(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = reverse(game)
    return game, done
