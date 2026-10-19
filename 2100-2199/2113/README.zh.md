# 2113. 逃离蔓延洪水的最小跳跃高度

[Timus 2113](https://acm.timus.ru/problem.aspx?space=1&num=2113) · 难度 432 · bfs, binary_search

原题作者 Anton Lipin，出自 2019 年大学学术中学生信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

兔子和水从 n × m 高度网格的不同格子出发。它们轮流行动，兔子先。兔子可以原地不动，或跳到边相邻且比当前格高出不超过 J 的格子。水会淹没每个有不低于它的已淹没邻格的格子。求使兔子能永远不进水的最小跳跃高度 J，若任何 J 都不行则输出 −1。时间限制 2 秒，内存限制 256 MB。

## 输入

n 和 m（1 ≤ n, m ≤ 100，n · m ≠ 1），高度 0 ≤ hᵢⱼ ≤ 10⁵，兔子的格子和水的格子。

## 输出

最小的 J，或者 −1。

## 样例

### 样例 1

输入：

```
2 3
6 5 4
1 2 3
2 1
1 3
```

输出：

```
3
```

### 样例 2

输入：

```
1 3
0 0 0
1 1
1 3
```

输出：

```
-1
```

## 解法

水的行为与兔子无关，所以从水的格子做一次广度优先搜索，得到每个格子 c 被淹没的回合 F(c)（水永远到不了的格子记为无穷大）。兔子的第 k 步在水的第 k 次行动之前，并且在水行动时仍站在那里，所以只有当 F(c) > k 时，兔子才能在 k 步后站在 c 上。等待没有好处：更早到达从不更差。

对固定的 J，从兔子的格子出发做第二次搜索，沿着允许的步并遵守这些期限前进。兔子能存活，当且仅当搜索到达一个永远不会被淹没的格子：其他格子迟早都会被淹没。J 越大允许的步越多，所以存活关于 J 单调。若连 J = 10⁵ 都不行，答案为 −1，否则对 J 二分查找最小值。总时间 O(n m log H)。

第一个样例中，右上角的水会淹没整个下面一行，但永远淹不到高度 5 和 6 的格子。兔子从高度 1 走到高度 2，然后恰好在水到来之前向上爬三个单位到高度 5。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2113_bfs_binary_search.cpp](2113_bfs_binary_search.cpp) | G++ 13.2 x64 | bfs, binary_search | O(n m log H) | AC | 0.015 s | 432 KB |
| [2113_bfs_binary_search.go](2113_bfs_binary_search.go) | Go 1.14 x64 | bfs, binary_search | O(n m log H) | AC | 0.031 s | 3712 KB |
| [2113_bfs_binary_search.java](2113_bfs_binary_search.java) | Java 1.8 | bfs, binary_search | O(n m log H) | AC | 0.125 s | 648 KB |
| [2113_bfs_binary_search.py](2113_bfs_binary_search.py) | Python 3.12 x64 | bfs, binary_search | O(n m log H) | AC | 0.125 s | 2492 KB |
| [2113_bfs_binary_search.rs](2113_bfs_binary_search.rs) | Rust 1.75 x64 | bfs, binary_search | O(n m log H) | AC | 0.046 s | 364 KB |
