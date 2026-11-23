# 1330. 区间

[Timus 1330](https://acm.timus.ru/problem.aspx?space=1&num=1330) · 难度 95 · prefix_sums

原题作者 Den Raskovalov，出自 2004 年 10 月 16 日第十届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N ≤ 10 000 个传感器给出 −10 000 到 10 000 之间的整数读数。回答最多 100 000 个问题：第 i 到第 j 个传感器
（i ≤ j）读数之和。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

N，然后 N 个读数，然后 Q 和 Q 对 i, j。

## 输出

每行一个和。

## 样例

### 样例 1

输入：

```
5
1
2
3
-1
4
3
1 5
4 4
1 4
```

输出：

```
9
-1
5
```

## 解法

维护 before[i]，即前 i 个读数之和，before[0] = 0。从 i 到 j 的和就是 before[j] − before[i − 1]，每个问题
一次减法。`O(N + Q)`。

注意事项：

- 和在 −10⁸ 到 10⁸ 之间，32 位整数放得下；
- 可能根本没有问题（测试 03）；
- 有 100 000 个问题时，输入输出要大块读写，才能在 0.5 秒内完成。

## 优化解法

`1330_prefix_sums_optimized.py`. 保留前缀和及区间 [i,j] 的 before[j]-before[i-1]。用 split/map 解析 65536 字节块，跨边界保留部分数字，不再逐行通过另一生成器解析。Python 列表保存前缀，最多 4096 个答案一批输出。N 个数、Q 个查询下仍为 O(N+Q) 时间、O(N) 状态及有界输入/输出批次，不保存查询列表或全部输出。

精确源代码 CPython 3.12 Accepted #11326660：0.156 s / 2648 KB。2026-11-20 保存的当前编译器比较：时间排名 5/34，内存排名 5/34。两项必需指标均通过严格前十或前 15%（百分比界限向上取整）。星号表示 Python 单独的双指标第一名目标。

此前记录的优化提交 #11303743（Python 3.12 x64）为 0.203 s / 1440 KB。当前 CPython 3.12 记录时间更低、内存更高。这是不同评测运行的成对测量，比较包含解释器选择及运行波动。 保留简单版记录为 0.125 s，更快；此版侧重较低内存。

- `1330_prefix_sums_optimized.py`: 0.156 s / 2648 KB; 保留教学基础版 `1330_prefix_sums.py` (Python 3.12 x64): 0.125 s / 27608 KB.

优化的 C++ 和 Java 解法用 32 位整数保存前缀和，这对 −10⁸ 到 10⁸ 之间的和已经足够。
C++ 通过 4 KB 的缓冲区手工解析数字、手工写出答案，并把前缀和放在静态数组中：
0.015 s，而不是 0.125 s；132 KB，而不是 2784 KB。

优化的 Java 解法按 4 KB 分块读入并手工解析，而不是使用 `StreamTokenizer`，答案写 进 4 KB 的字节缓冲区，而不是拼接字符串：0.125 s，而不是 0.156 s；452 KB，而不是 7324 KB。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1330_prefix_sums_optimized.rs`. 保留原有算法及整数类型，直接转换十进制词元，避免通用字符串解析。负数按负值累积，因此最小有符号整数也不会在取绝对值时溢出。输入存储和算法复杂度不变。

Accepted #11328541 (Rust 1.75 x64): **0.015 s / 3676 KB**. 历史对照: `1330_prefix_sums.rs` (Rust 1.75 x64) — 0.046 s / 3736 KB (#11285004).

## 各语言说明

- 简单的 Java 解法用能处理负数读数的 `StreamTokenizer` 读入，并把答案收集成一个
  字符串。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1330_prefix_sums.cpp](1330_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 2784 KB | 11284999 |
| [1330_prefix_sums.go](1330_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 2828 KB | 11285000 |
| [1330_prefix_sums.java](1330_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + Q) | AC | 0.156 s | 7324 KB | 11303461 |
| [1330_prefix_sums.py](1330_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 27608 KB | 11285001 |
| [1330_prefix_sums.rs](1330_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 3736 KB | 11285004 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1330_prefix_sums_optimized.cpp](1330_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(N + Q) | AC | 0.015 s | 132 KB | 11303598 |
| [1330_prefix_sums_optimized.java](1330_prefix_sums_optimized.java) | Java 1.8 | prefix_sums | O(N + Q) | AC | 0.125 s | 452 KB | 11303742 |
| [1330_prefix_sums_optimized.py](1330_prefix_sums_optimized.py) | Python 3.12 x64 | prefix_sums | O(N+Q) time; O(N+B+S) space | AC | 0.156 s | 2648 KB | 11326660 |
| [1330_prefix_sums_optimized.rs](1330_prefix_sums_optimized.rs) | Rust 1.75 x64 | prefix_sums | O(N + Q) | AC | 0.015 s | 3676 KB | 11328541 |
