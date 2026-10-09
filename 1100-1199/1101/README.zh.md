# 1101. 由布尔表达式操纵的机器人

[Timus 1101](https://acm.timus.ru/problem.aspx?space=1&num=1101) · 难度 532 · parsing, simulation

原题作者 Pavel Atnashev，出自 2001 年 5 月 Tetrahedron Team Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

机器人从场地 `[−N..N] × [−N..N]`（`N ≤ 100`）中的 `(0, 0)` 出发，朝方向 `(1, 0)` 每次移动一格。在 `M ≤ 100` 个岔口
中的每一个，它计算一个布尔表达式（最多 250 个字符，包含按优先级从高到低的 `NOT`、`AND`、`OR`，括号，`TRUE`、
`FALSE`，以及开始时全为 `FALSE` 的寄存器 `A`–`Z`），值为 `TRUE` 时右转，否则左转。另外 `K ≤ 100` 个格子中的每一个，
在机器人位于其上时翻转一个寄存器。输出机器人路线上的每个格子，直到它离开场地。

时间限制：1 秒。内存限制：64 MB。

## 输入

表达式；`N`、`M` 和 `K`；`M` 行岔口；`K` 行，每行一个格子和它翻转的寄存器。

## 输出

路线上的格子，每行一个。

## 评测方式

按记号逐个比较输出；多余的空白不影响结果。

## 样例

### 样例 1

输入：

```
NOT((A OR NOT B) AND (A OR B)) OR NOT (A AND NOT B OR TRUE)
1 5 2
1 0
1 1
1 -1
-1 -1
-1 1
0 1 A
-1 0 D
```

输出：

```
0 0
1 0
1 -1
0 -1
-1 -1
-1 0
-1 1
0 1
1 1
```

## 题解

把表达式拆成单词（`NOT`、`AND`、`OR`、`TRUE`、`FALSE`、寄存器）和括号，然后用递归下降一次性建出语法树，每个
优先级一个函数：由若干 `AND` 组成的 `OR`，`AND` 由 `NOT` 组成，`NOT` 作用于原子，原子是常量、寄存器或括号中的
表达式。

然后开始走。在场地内的每个格子上：输出它；如果是开关，翻转对应的寄存器；如果是岔口，计算语法树，`TRUE` 时右转
（`(dx, dy) → (dy, −dx)`），`FALSE` 时左转（`(dx, dy) → (−dy, dx)`）；向前走一步。机器人一离开场地就停止。
路线长 `L`、表达式长 `|E|` 时为 `O(L · |E|)`。

注意事项：

- `NOT A AND B` 表示 `(NOT A) AND B`，`A OR B AND C` 表示 `A OR (B AND C)`；
- 单词可能紧挨着括号，如 `NOT(A OR(B))`，所以要从文本中切出单词，而不是按空格拆分；
- 转向取决于机器人到达岔口那一刻的寄存器值，即经过之前开关之后的值。

答案与另一种走法做了核对：把表达式翻译成 Python 中优先级相同的 `not`、`and`、`or`，再用 `eval` 计算。

## 各语言说明

- Rust 用带 `Box` 子节点的 `enum` 保存语法树；Go 和 Java 使用结点结构体；C++ 把结点存放在 vector 中。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1101_parsing.cpp](1101_parsing.cpp) | G++ 13.2 x64 | parsing | O(L·len(E)) | AC | 0.015 s | 628 KB |
| [1101_parsing.go](1101_parsing.go) | Go 1.14 x64 | parsing | O(L·len(E)) | AC | 0.031 s | 1780 KB |
| [1101_parsing.java](1101_parsing.java) | Java 1.8 | parsing | O(L·len(E)) | AC | 0.093 s | 2192 KB |
| [1101_parsing.py](1101_parsing.py) | Python 3.12 x64 | parsing | O(L·len(E)) | AC | 0.078 s | 1408 KB |
| [1101_parsing.rs](1101_parsing.rs) | Rust 1.75 x64 | parsing | O(L·len(E)) | AC | 0.015 s | 552 KB |
