# 1022. 让祖先排在前面的家族排序

[Timus 1022](https://acm.timus.ru/problem.aspx?space=1&num=1022) · 难度 142 · graphs, bfs, dfs

原题出自 2000 年 10 月 7 日斯维尔德洛夫斯克州第二届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

`N` 个成员（`1 ≤ N ≤ 100`），编号 `1..N`，之间有“父母—孩子”关系：一个成员可以有任意多个父母和孩子，且
没有环。输出所有成员的一个顺序，使每个成员都排在其所有后代之前。任何这样的顺序都可接受。

时间限制：1 秒。内存限制：64 MB。

## 输入

先是 `N`，然后 `N` 行：第 `i` 行以任意顺序列出成员 `i` 的孩子，并以 `0` 结尾（只有 `0` 的一行表示没有孩子）。

## 输出

按所选顺序输出 `N` 个编号，以空格分隔。

## 评测方式

接受任何合法顺序。检查器验证输出是 `1..N` 的一个排列，且每个成员都在其每个孩子之前（由归纳即得在所有后代
之前）。

## 样例

### 样例 1

输入：

```
4
0
1 0
1 4 0
1 0
```

输出：

```
2 3 4 1
```

### 样例 2

输入：

```
1
0
```

输出：

```
1
```

## 题解

成员和关系构成一个有向无环图，所要的顺序就是它的 **拓扑序**。

**Kahn 算法（BFS）。** 统计每个成员的父母数。没有父母的成员可以最先发言，把它们放入队列。依次从队列取出
成员；对它的每个孩子把父母计数减一，计数降为零的孩子入队——它的所有父母都已发言。按入队顺序排列的队列
就是答案。

**深度优先搜索。** 从每个未访问的成员出发做 DFS，当一个成员的 DFS 结束时（即在其所有后代之后）把它加入
列表。把列表反转，每个成员就都在其后代之前。

两种方法都是 `O(N + E)`，`E` 为关系数，这里至多约 5 000。

注意事项：

- 输入给出的是孩子而不是父母：从列表统计入度；
- 只有 `0` 的一行是空列表，而不是输入结束。

## 优化解法

优化的 C++ Kahn 算法解法把关系存放在固定的 101 × 101 `bool` 矩阵中，由于
`N ≤ 100`，只占约 10 KB，队列也放在固定数组里，而不是用随每条关系增长的 `vector`
嵌套 `vector`。从队列取出一个成员时，它扫描矩阵的整行，总共 `O(N²)`，对 100 个成
员来说微不足道：{1022_bfs_graphs_optimized.cpp}。

优化的 Java Kahn 算法解法从 4 KB 缓冲区中手工解析数字，而不是用 `Scanner`；关系
存放在 (N + 1) × (N + 1) 的 `boolean` 矩阵中，由于 `N ≤ 100`，矩阵很小，队列放在
`int` 数组里，而不是用装箱 `Integer` 对象的列表。从队列取出一个成员时，它扫描矩
阵的整行，总共 `O(N²)`：{1022_bfs_graphs_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1022_bfs_graphs_optimized.cpp`: 时间降低 +0.00%; 内存降低 +45.10%; 基础版本: `1022_bfs_graphs.cpp`.

- `1022_bfs_graphs_optimized.java`: 时间降低 +25.60%; 内存降低 +80.31%; 基础版本: `1022_bfs_graphs.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1022_bfs_graphs.go](1022_bfs_graphs.go).
- [1022_dfs_graphs.rs](1022_dfs_graphs.rs).

- **C++**、**Go**、**Java**：Kahn 算法。
- **C++**、**Rust**：递归 DFS（深度至多 100）；**Python**：用显式迭代器栈实现同样的 DFS。

## 题解代码

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1022_bfs_graphs.cpp](1022_bfs_graphs.cpp) | G++ 13.2 x64 | bfs, graphs | O(N + E) | AC | 0.015 s | 204 KB | 11278266 |
| [1022_dfs_graphs.cpp](1022_dfs_graphs.cpp) | G++ 13.2 x64 | dfs, graphs | O(N + E) | AC | 0.015 s | 196 KB | 11278269 |
| [1022_bfs_graphs.go](1022_bfs_graphs.go) | Go 1.14 x64 | bfs, graphs | O(N + E) | AC | 0.015 s | 1124 KB | 11278272 |
| [1022_bfs_graphs.java](1022_bfs_graphs.java) | Java 1.8 | bfs, graphs | O(N + E) | AC | 0.125 s | 1828 KB | 11278276 |
| [1022_dfs_graphs.py](1022_dfs_graphs.py) | Python 3.12 x64 | dfs, graphs | O(N + E) | AC | 0.078 s | 512 KB | 11278274 |
| [1022_dfs_graphs.rs](1022_dfs_graphs.rs) | Rust 1.75 x64 | dfs, graphs | O(N + E) | AC | 0.015 s | 236 KB | 11278277 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1022_bfs_graphs_optimized.cpp](1022_bfs_graphs_optimized.cpp) | G++ 13.2 x64 | bfs, graphs | O(N²) | AC | 0.015 s | 112 KB | 11304480 |
| [1022_bfs_graphs_optimized.java](1022_bfs_graphs_optimized.java) \* | Java 1.8 | bfs, graphs | O(N²) | AC | 0.093 s | 360 KB | 11304481 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
