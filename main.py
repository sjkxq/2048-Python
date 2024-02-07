# 导入所需的模块
from tkinter import Frame, Label, CENTER
import random
import logic
import constants as c


# 定义生成随机索引的函数，返回一个在指定范围内的整数
def gen() -> int:
    return random.randint(0, c.GRID_LEN - 1)


# 定义 GameGrid 类，该类用于创建游戏界面并处理逻辑
class GameGrid(Frame):
    def __init__(self) -> None:
        # 初始化父类 Frame
        super().__init__()

        # 设置窗口标题、布局，并绑定键盘事件
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)

        # 创建按键命令字典，键为按键名称，值为对应的方向移动函数
        self.commands: dict[str, callable[[list[list[int]]], tuple[list[list[int]], bool]]] = {
            c.KEY_UP: logic.up,
            c.KEY_DOWN: logic.down,
            c.KEY_LEFT: logic.left,
            c.KEY_RIGHT: logic.right,
            # 其他可能的快捷键映射（示例代码中并未定义这些常量）
            c.KEY_UP_ALT1: logic.up,
            c.KEY_DOWN_ALT1: logic.down,
            c.KEY_LEFT_ALT1: logic.left,
            c.KEY_RIGHT_ALT1: logic.right,
            c.KEY_UP_ALT2: logic.up,
            c.KEY_DOWN_ALT2: logic.down,
            c.KEY_LEFT_ALT2: logic.left,
            c.KEY_RIGHT_ALT2: logic.right,
        }

        # 初始化格子列表
        self.grid_cells: list[list[Label]] = []
        self.init_grid()

        # 创建新的游戏矩阵，并初始化历史记录矩阵列表
        self.matrix: list[list[int]] = logic.new_game(c.GRID_LEN)
        self.history_matrixs: list[list[list[int]]] = []

        # 更新游戏格子内容
        self.update_grid_cells()

        # 进入主循环以保持窗口打开
        self.mainloop()

    # 初始化游戏网格，包括背景和所有单元格
    def init_grid(self) -> None:
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(
                    background,
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    width=c.SIZE / c.GRID_LEN,
                    height=c.SIZE / c.GRID_LEN
                )
                cell.grid(
                    row=i,
                    column=j,
                    padx=c.GRID_PADDING,
                    pady=c.GRID_PADDING
                )

                t = Label(
                    master=cell,
                    text="",
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    justify=CENTER,
                    font=c.FONT,
                    width=5,
                    height=2
                )
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    # 更新游戏单元格的内容以反映当前矩阵状态
    def update_grid_cells(self) -> None:
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]

                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number),
                        bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number]
                    )
        self.update_idletasks()

    # 处理键盘按键事件
    def key_down(self, event) -> None:
        key = event.keysym

        if key == c.KEY_QUIT:
            exit()

        if key == c.KEY_BACK and len(self.history_matrixs) > 1:
            self.matrix = self.history_matrixs.pop()
            self.update_grid_cells()
            print('回到上一步，剩余步骤总数:', len(self.history_matrixs))

        elif key in self.commands:
            moved_matrix, done = self.commands[key](self.matrix)
            self.matrix = moved_matrix

            if done:
                self.matrix = logic.add_two(self.matrix)
                # 记录移动后的矩阵状态
                self.history_matrixs.append(self.matrix.copy())
                self.update_grid_cells()

                # 检查游戏结果
                game_state = logic.game_state(self.matrix)
                if game_state == 'win':
                    self.display_win_message()
                elif game_state == 'lose':
                    self.display_lose_message()

    # 显示胜利消息
    def display_win_message(self) -> None:
        self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    # 显示失败消息
    def display_lose_message(self) -> None:
        self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    # 生成下一个数字到空单元格
    def generate_next(self) -> None:
        index = (gen(), gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (gen(), gen())
        self.matrix[index[0]][index[1]] = 2


# 当作为主脚本运行时，实例化GameGrid类并开始游戏
if __name__ == '__main__':
    game_grid = GameGrid()
