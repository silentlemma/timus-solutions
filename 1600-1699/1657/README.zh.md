# 1657. 立方蛇

[Timus 1657](https://acm.timus.ru/problem.aspx?space=1&num=1657) · 难度 1522 · backtracking

原题作者 Stanislav Vasilyev（由 Sergey Pupyrev 准备），出自 NEERC 2008 东部分区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

蛇形魔方是一串 27 个小立方块。直块（`F`）中绳子穿过相对的两个面，转弯块（`T`）中穿过相邻的两个面；两端的块
视为直块。把蛇折成 3 × 3 × 3 的立方体，输出每个块相对于前一个块的位置，或指出无法做到。

## 输入

27 个字母 `F` 和 `T`。

## 输出

26 个取自 `RLFBUD` 的字母（右、左、前、后、上、下），或 `IMPOSSIBLE`。任何合法的折法都被接受。

## 样例

### 样例 1

输入：

```
FFTTTFTTFTTTFTFTTTTFTFTFTFF
```

输出：

```
UURDFFRBBUFLLDDRBRFFLLUURR
```

### 样例 2

输入：

```
FFTFTFTFTTTTFFFTTTFTTFTTTFF
```

输出：

```
IMPOSSIBLE
```

## 解法

折叠就是一条经过立方体全部 27 个格子的路径：直块之后的下一步保持方向，转弯块之后走四个横向方向之一。深度
优先搜索依次尝试这些方向，不进入已占用的格子；一旦空闲格子分裂成不止一块，就放弃这一分支，因为剩下的蛇不
可能走遍它们。

两个观察让搜索小到 Python 也能承受。格子像棋盘一样染成两色，一色 14 个、另一色 13 个，而蛇的颜色交替，所以
必须从较多的颜色开始：角上或面的中心。立方体的对称性使所有角以及从角出发的所有第一步都等价，而从面中心出发
只有两种步：向内朝立方体中心，或沿着这个面。于是搜索只需从三种第一步开始。

易错点：

- 输入保证首尾字母均为 `F`；代码不读取这两个字母；
- 全是直块的蛇是一根长 27 的棍，永远折不起来（测试 03）；
- 折法很多，所以检查器重放每一步。

在 120 条蛇上（包括随机蛇，以及随机折法改动一块后的蛇），答案的 Yes 或 No 与一个独立的已通过实现一致，并能
通过检查器。

复杂度：`O(C * 4^C)`，C = 27 个格子，每个转弯方块之后最多四个方向。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1657_backtracking.cpp](1657_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(C * 4^C) | AC | 0.046 s | 372 KB |
| [1657_backtracking.go](1657_backtracking.go) | Go 1.14 x64 | backtracking | O(C * 4^C) | AC | 0.046 s | 5852 KB |
| [1657_backtracking.java](1657_backtracking.java) | Java 1.8 | backtracking | O(C * 4^C) | AC | 0.125 s | 6092 KB |
| [1657_backtracking.py](1657_backtracking.py) | Python 3.12 x64 | backtracking | O(C * 4^C) | AC | 0.796 s | 776 KB |
| [1657_backtracking.rs](1657_backtracking.rs) | Rust 1.75 x64 | backtracking | O(C * 4^C) | AC | 0.062 s | 220 KB |
