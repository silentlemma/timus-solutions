# 2216. 每条从底层到顶层的路线都必经的最少监控电梯

[Timus 2216](https://acm.timus.ru/problem.aspx?space=1&num=2216) · 难度 662 · prefix_sums

原题作者 Matvey Dmitriev，出自 2025 年 ICPC 乌拉尔赛区资格赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

大楼有 1 … N 层和 K 部电梯，第 i 部电梯可以在 [lᵢ, rᵢ] 中任意两层之间移动。在尽可能少的电梯里装摄像头，使每个从 1 层去 N 层的人至少乘坐一部有摄像头的电梯，否则输出 −1。楼层之间只能乘电梯移动，保证任意两层之间都可到达。时间限制 1 秒，内存限制 256 MB。

## 输入

N 和 K（1 ≤ N, K ≤ 10⁵），然后是 K 个区间，满足 1 ≤ lᵢ ≤ rᵢ ≤ N。

## 输出

最少的摄像头数，或 −1。

## 样例

### 样例 1

输入：

```
1984 1
1 1984
```

输出：

```
1
```

### 样例 2

输入：

```
2 2
1 2
1 2
```

输出：

```
2
```

## 解法

N = 1 时没有人需要坐电梯，任何摄像头安排都不行，答案为 −1。

否则考虑 f 层与 f + 1 层之间的间隙。每条从 1 到 N 的路线都必须跨过它，而只有满足 l ≤ f < r 的电梯跨过它，所以在这些电梯里都装上摄像头就能拍到所有人。反过来，如果某种安排使每个间隙上都至少有一部没装摄像头的电梯，那么这些电梯的区间从 1 到 N 依次重叠，构成一条不被拍到的路线。所以答案是单个间隙上电梯数的最小值。

差分数组（l 处 +1，r 处 −1）用前缀和给出每个间隙上的电梯数，对 f = 1 … N − 1 取最小值即为答案。

连通性保证 N > 1 时最小值为正。一个易错点是要求换乘电梯的区间必须覆盖同一间隙；实际上，只要有一个共同楼层就能换乘（测试 12）。

第二个样例中两部电梯都跨过唯一的间隙，所以两部都要装摄像头。

复杂度 O(N + K)。

## 优化解法

流式读取电梯区间，在紧凑的差分数组中记录端点变化。相邻楼层之间的前缀和最小值就是答案。

Python 提交 11317733 耗时 0.156 秒，使用 1560 KB。简单版本耗时 0.14 秒，使用 14948 KB。

Go 提交 11317737 耗时 0.031 秒，使用 1312 KB。简单版本耗时 0.015 秒，使用 5784 KB。

Rust 提交 11317747 耗时 0.015 秒，使用 596 KB。简单版本耗时 0.062 秒，使用 3156 KB。

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11321723 · Java 1.8 №11321729 · Go 1.14 x64 №11322089 · Python 3.12 x64 №11322090 · Rust 1.75 x64 №11322092.

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`2216_prefix_sums_parsing_optimized.py`. 流式读取输入并写入紧凑的有符号楼层差分数组，保留原来的前缀累加和区间最小值计算。 独立程序先刷新两个输出流，再调用 os._exit(0)，在完整答案写出后跳过解释器清理。这只改变进程结束方式，不改变数学算法；简单版本仍保留。

Accepted #11328766 (Python 3.12 x64): **0.14 s / 972 KB**. 历史对照: `2216_prefix_sums.py` (Python 3.12 x64) — 0.14 s / 14948 KB (#11322090).

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [2216_prefix_sums.cpp](2216_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + K) | AC | 0.046 s | 800 KB | 11321723 |
| [2216_prefix_sums.go](2216_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + K) | AC | 0.015 s | 5784 KB | 11322089 |
| [2216_prefix_sums.java](2216_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + K) | AC | 0.125 s | 960 KB | 11321729 |
| [2216_prefix_sums.py](2216_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + K) | AC | 0.14 s | 14948 KB | 11322090 |
| [2216_prefix_sums.rs](2216_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + K) | AC | 0.062 s | 3156 KB | 11322092 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [2216_prefix_sums_optimized.py](2216_prefix_sums_optimized.py) \* | Python 3.12 x64 | prefix_sums | O(N + K) | AC | 0.156 s | 1560 KB | 11317733 |
| [2216_prefix_sums_optimized.go](2216_prefix_sums_optimized.go) | Go 1.14 x64 | prefix_sums | O(N + K) | AC | 0.031 s | 1312 KB | 11317737 |
| [2216_prefix_sums_optimized.rs](2216_prefix_sums_optimized.rs) | Rust 1.75 x64 | prefix_sums | O(N + K) | AC | 0.015 s | 596 KB | 11317747 |
| [2216_prefix_sums_parsing_optimized.py](2216_prefix_sums_parsing_optimized.py) | Python 3.12 x64 | prefix_sums, parsing | O(N + K) | AC | 0.14 s | 972 KB | 11328766 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
