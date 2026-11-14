# 1004. 无向多重图中的最短环

[Timus 1004](https://acm.timus.ru/problem.aspx?space=1&num=1004) · 难度 581 · shortest_paths, graphs

原题出自 1999 年中欧信息学奥林匹克竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

无向图有 `N` 个顶点（`3 ≤ N ≤ 100`）和 `M` 条边（`3 ≤ M ≤ N·(N-1)`），边长为正整数
`1 ≤ l ≤ 300`。同一对顶点之间可能有多条边，但没有自环。

求一个至少包含 3 个顶点、总长度最小的简单环：互不相同的顶点 `x1, ..., xk`（`k ≥ 3`），使得
`x1-x2, ..., x(k-1)-xk` 以及 `xk-x1` 都是边。环的长度为这些边的长度之和。若不存在这样的环，
需要报告。

输入包含 `T ≤ 5` 组这样的测试。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

各组测试依次给出。每组测试为：一行 `N M`，以及 `M` 行 `a b l`，表示 `a` 与 `b`（`a ≠ b`）之间
一条长度为 `l` 的边。以一行 `-1` 结束输入。

## 输出

每组测试输出一行：按顺序给出最短环的顶点 `x1 ... xk`，用单个空格分隔；若图中不存在至少
3 个顶点的环，则输出 `No solution.`。

## 评测方式

接受任意一个最短环，可以从任意顶点开始、沿任意方向：检查器会验证顶点互不相同、相邻顶点
之间有边相连，并且总长度最小。

## 样例

### 样例 1

输入：

```
5 7
1 2 2
2 3 2
3 1 2
3 4 1
4 5 1
5 3 1
1 5 10
4 3
1 2 5
2 3 5
3 4 5
-1
```

输出：

```
4 5 3
No solution.
```

### 样例 2

输入：

```
3 3
1 2 1
1 2 1
2 1 3
-1
```

输出：

```
No solution.
```

## 题解

两个顶点之间只有最短的那条边有意义，因此维护一个最轻直接边的矩阵；仅由平行边无法构成合法
的环（至少需要 3 个不同顶点）。

运行 Floyd-Warshall 算法，在允许顶点 `k` 作为中间点之前，枚举所有与 `k` 有边相连的顶点对
`i < j < k`：此时 `dist[i][j]` 是只经过小于 `k` 的顶点时 `i` 与 `j` 之间的最短路，因此这条路
加上边 `j-k` 和 `k-i` 构成一个以 `k` 为最大顶点的简单环。一个最短环会在处理其最大顶点时被
找到，所以所有候选中的最小值就是答案。维护 `next` 矩阵（最短路的第一步）即可还原路径。
每组测试时间复杂度 `O(N^3)`，空间 `O(N^2)`。

注意事项：

- 两条平行边不构成合法路线：环至少要有 3 个顶点；
- 平行边中只应使用最短的那条；
- 必须在经过 `k` 松弛之前检查候选环，否则路径 `i..j` 可能经过 `k` 本身。

## 优化解法

优化后的 C++ 版本沿用 Floyd–Warshall 递推。每对顶点只更新一次，并保持距离矩阵对称。由于边权为正，长度不小于已知最短环的路径无法帮助找到更短的环。距离用 16
位存储，下一顶点编号用 8 位存储。提交 11316956 耗时 0.015 秒、使用 136 KB；基础版本为 0.046 秒和 360 KB。

Go 版本同样对称更新距离，并跳过过长的路径。距离用 16 位存储，下一顶点编号用 8 位存储，输入和输出均使用缓冲。提交 11317015 耗时 0.015 秒、使用 988 KB；基础版本为 0.031 秒和 3356 KB。

Rust 版本对称更新距离，并跳过无法改进最短环的路径。距离用 16 位存储，下一顶点编号用 8 位存储。提交 11317149 耗时 0.015 秒、使用 244 KB；基础版本为 0.015 秒和 1096 KB。

PyPy 版本对称更新距离，跳过无法改进最短环的路径，并用字节数组存储下一顶点。提交 11317152 耗时 0.187 秒，使用 4452 KB；基础版在 PyPy 下耗时 0.187 秒，使用 9912 KB。

Java 版本对称更新距离，并跳过无法改进最短环的路径。距离用 short 数组存储，下一顶点用字节数组存储。提交 11317153 耗时 0.109 秒，使用 844 KB；基础版耗时 0.125 秒，使用 1384 KB。

## 各语言说明

- **C++**、**Go**、**Rust**：普通的 `O(N^3)` 循环远低于时间限制。
- **Python**：`5 · 100^3` 次内层循环对 0.5 秒来说很紧；对 `j` 的循环使用行的局部引用
  （`di`、`dk`），并跳过 `dist[i][k]` 为无穷的行。即便如此，在 CPython 3.12 下它在第 4
  个测试上超时（0.531 秒）；同一文件在 PyPy 3.10 下以 0.187 秒通过，所以 Python 解法只能在 PyPy 下通过。
- **Java**：自己实现按字节读取，以处理多达 50 000 行的输入。

## 题解代码

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1004_shortest_paths_graphs.cpp](1004_shortest_paths_graphs.cpp) | G++ 13.2 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.046 s | 360 KB | 11277433 |
| [1004_shortest_paths_graphs.go](1004_shortest_paths_graphs.go) | Go 1.14 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.031 s | 3356 KB | 11277584 |
| [1004_shortest_paths_graphs.java](1004_shortest_paths_graphs.java) | Java 1.8 | shortest_paths, graphs | O(N^3) per test | AC | 0.125 s | 1384 KB | 11277599 |
| [1004_shortest_paths_graphs.py](1004_shortest_paths_graphs.py) | PyPy 3.10 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.187 s | 9912 KB | 11277592 |
| [1004_shortest_paths_graphs.rs](1004_shortest_paths_graphs.rs) | Rust 1.75 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.015 s | 1096 KB | 11277603 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1004_shortest_paths_graphs_optimized.cpp](1004_shortest_paths_graphs_optimized.cpp) | G++ 13.2 x64 | shortest_paths, graphs | O(N^3) | AC | 0.015 s | 136 KB | 11316956 |
| [1004_shortest_paths_graphs_optimized.go](1004_shortest_paths_graphs_optimized.go) \* | Go 1.14 x64 | shortest_paths, graphs | O(N^3) | AC | 0.015 s | 988 KB | 11317015 |
| [1004_shortest_paths_graphs_optimized.rs](1004_shortest_paths_graphs_optimized.rs) | Rust 1.75 x64 | shortest_paths, graphs | O(N^3) | AC | 0.015 s | 244 KB | 11317149 |
| [1004_shortest_paths_graphs_optimized.py](1004_shortest_paths_graphs_optimized.py) | PyPy 3.10 x64 | shortest_paths, graphs | O(N^3) | AC | 0.187 s | 4452 KB | 11317152 |
| [1004_shortest_paths_graphs_optimized.java](1004_shortest_paths_graphs_optimized.java) | Java 1.8 | shortest_paths, graphs | O(N^3) | AC | 0.109 s | 844 KB | 11317153 |

\* 已通过评测。排名快照中没有其他作者的可比 Go 提交，因而尚未确认达到排名目标。
