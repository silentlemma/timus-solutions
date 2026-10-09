# 1060. 使 4 × 4 棋盘同色的最少翻转次数

[Timus 1060](https://acm.timus.ru/problem.aspx?space=1&num=1060) · 难度 375 · bruteforce, bitmask

原题出自 2000–2001 年 ACM ICPC 东北欧区域赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

4 × 4 的棋盘上放着棋子，朝上的一面为黑（`b`）或白（`w`）。一步操作选择一个格子，翻转该格的棋子以及它上下左右
存在的相邻棋子。求使所有棋子朝上颜色相同（任一颜色）的最少步数；若已经相同输出 `0`；若做不到输出 `Impossible`。

时间限制：2 秒。内存限制：64 MB。

## 输入

四行，每行四个 `b` 或 `w` 字符。

## 输出

最少步数，或 `Impossible`。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
bwbw
wwww
bbwb
bwwb
```

输出：

```
Impossible
```

### 样例 2

输入：

```
bwwb
bbwb
bwwb
bwww
```

输出：

```
4
```

## 题解

把棋盘写成 16 位；在一个格子上操作就是把棋盘与一个固定的、最多五位的掩码异或。异或满足交换律，同一掩码用两次
会抵消，所以操作顺序无关紧要，任何格子都不需要操作两次：一个解就是一个格子集合。

共有 `2^16 = 65536` 个集合。对每个集合，把其中各格的掩码异或到棋盘上，记录结果为全 0 或全 1 的最小集合。
`O(2^16 · 16)`。

65536 个局面中只有 4096 个可解，而且都不超过六步（用于核对测试的、遍历所有局面的广度优先搜索表明了这一点）。

注意事项：

- 全白和全黑都是目标；
- 边上和角上的格子翻转的棋子更少；
- 已经同色的局面需要 0 步。

## 各语言说明

- **C++**、**Go**、**Java**、**Rust**：遍历全部 65536 个集合。
- **Python**：逐个格子构造所有集合对应的棋盘，每次把列表加倍（新格子把自己的掩码异或到已有的每个棋盘上），
  从而避免对每个集合的 16 位做 Python 循环。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1060_bruteforce_bitmask.cpp](1060_bruteforce_bitmask.cpp) | G++ 13.2 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.015 s | 124 KB |
| [1060_bruteforce_bitmask.go](1060_bruteforce_bitmask.go) | Go 1.14 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.031 s | 1068 KB |
| [1060_bruteforce_bitmask.java](1060_bruteforce_bitmask.java) | Java 1.8 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.109 s | 1580 KB |
| [1060_bruteforce_bitmask.py](1060_bruteforce_bitmask.py) | Python 3.12 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.109 s | 4840 KB |
| [1060_bruteforce_bitmask.rs](1060_bruteforce_bitmask.rs) | Rust 1.75 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.015 s | 232 KB |
