# 1004. 无向多重图中的最短环

[Timus 1004](https://acm.timus.ru/problem.aspx?space=1&num=1004) · 难度 580 · shortest_paths, graphs

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
加上边 `j-k` 和 `k-i` 构成一个以 `k` 为最大顶点的简单环。每个简单环都会在处理其最大顶点时被
找到，所以所有候选中的最小值就是答案。维护 `next` 矩阵（最短路的第一步）即可还原路径。
每组测试时间复杂度 `O(N^3)`，空间 `O(N^2)`。

注意事项：

- 两条平行边不构成合法路线：环至少要有 3 个顶点；
- 平行边中只应使用最短的那条；
- 必须在经过 `k` 松弛之前检查候选环，否则路径 `i..j` 可能经过 `k` 本身。

## 各语言说明

- **C++**、**Go**、**Rust**：普通的 `O(N^3)` 循环远低于时间限制。
- **Python**：`5 · 100^3` 次内层循环对 0.5 秒来说很紧；对 `j` 的循环使用行的局部引用
  （`di`、`dk`），并跳过 `dist[i][k]` 为无穷的行。即便如此，在 CPython 3.12 下它在第 4
  个测试上超时（0.531 秒）；同一文件在 PyPy 3.10 下以 0.187 秒通过，所以 Python 解法只能在 PyPy 下通过。
- **Java**：自己实现按字节读取，以处理多达 50 000 行的输入。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1004_shortest_paths_graphs.cpp](1004_shortest_paths_graphs.cpp) | G++ 13.2 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.046 s | 360 KB |
| [1004_shortest_paths_graphs.go](1004_shortest_paths_graphs.go) | Go 1.14 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.031 s | 3356 KB |
| [1004_shortest_paths_graphs.java](1004_shortest_paths_graphs.java) | Java 1.8 | shortest_paths, graphs | O(N^3) per test | AC | 0.125 s | 1384 KB |
| [1004_shortest_paths_graphs.py](1004_shortest_paths_graphs.py) | PyPy 3.10 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.187 s | 9912 KB |
| [1004_shortest_paths_graphs.rs](1004_shortest_paths_graphs.rs) | Rust 1.75 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.015 s | 1096 KB |
