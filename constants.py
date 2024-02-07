from typing import Dict

# 游戏区域总宽度
SIZE: int = 400

# 游戏网格的行数和列数
GRID_LEN: int = 4

# 游戏网格单元格之间的内边距
GRID_PADDING: int = 10

# 游戏区域背景颜色
BACKGROUND_COLOR_GAME: str = "#92877d"

# 空单元格背景颜色
BACKGROUND_COLOR_CELL_EMPTY: str = "#9e948a"

# 定义背景颜色字典，键为整数（表示游戏中的数字），值为字符串（十六进制颜色代码）
BACKGROUND_COLOR_DICT: Dict[int, str] = {
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
    4096: "#eee4da",
    8192: "#edc22e",
    16384: "#f2b179",
    32768: "#f59563",
    65536: "#f67c5f",
}

# 定义单元格颜色字典，键和值的类型同上
CELL_COLOR_DICT: Dict[int, str] = {
    2: "#776e65",
    4: "#776e65",
    8: "#f9f6f2",
    16: "#f9f6f2",
    32: "#f9f6f2",
    64: "#f9f6f2",
    128: "#f9f6f2",
    256: "#f9f6f2",
    512: "#f9f6f2",
    1024: "#f9f6f2",
    2048: "#f9f6f2",
    4096: "#776e65",
    8192: "#f9f6f2",
    16384: "#776e65",
    32768: "#776e65",
    65536: "#f9f6f2",
}

# 游戏字体设置，类型为包含字体名称、大小和样式（粗体）的元组
FONT: tuple[str, int, str] = ("Verdana", 40, "bold")

# 游戏退出按键
KEY_QUIT: str = "Escape"

# 游戏回退操作按键
KEY_BACK: str = "b"

# 游戏方向键
KEY_UP: str = "Up"
KEY_DOWN: str = "Down"
KEY_LEFT: str = "Left"
KEY_RIGHT: str = "Right"

# 方向键备用输入方式1
KEY_UP_ALT1: str = "w"
KEY_DOWN_ALT1: str = "s"
KEY_LEFT_ALT1: str = "a"
KEY_RIGHT_ALT1: str = "d"

# 方向键备用输入方式2
KEY_UP_ALT2: str = "i"
KEY_DOWN_ALT2: str = "k"
KEY_LEFT_ALT2: str = "j"
KEY_RIGHT_ALT2: str = "l"
