# 1279. 仓库

[Timus 1279](https://acm.timus.ru/problem.aspx?space=1&num=1279) · 难度 424 · binary_search

原题作者 Sergey Volchenkov、Vladimir Pinaev 和 Michael Kopachev，出自 2003 年 10 月 15–16 日在雷宾斯克举行的 ACM ICPC 2003–2004 俄罗斯中部赛区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个由 N × M 个区格（N, M ≤ 100）组成的仓库里堆着集装箱，每格高度在 1 到 1000 之间。
新到 K ≤ 10⁷ 个集装箱，每次放到某个最低的区格上。求全部放完后的最低高度。

时间限制：1 秒。内存限制：64 MB。

## 输入

N、M 和 K，然后是 N 行，每行 M 个高度。

## 输出

放完集装箱后的最低高度。

## 样例

### 样例 1

输入：

```
2 2 3
1 3
2 4
```

输出：

```
3
```

### 样例 2

输入：

```
3 3 10
1 2 3
4 5 6
7 8 9
```

输出：

```
5
```

## 解法

总往最低的格子上放，就像往里灌水：最后所有低于某个水位 h 的格子都升到了 h，剩下的集装箱
又把其中一部分（但不是全部）抬到了 h + 1。把所有格子升到 h 需要
need(h) = Σ max(0, h − 高度) 个集装箱，它随 h 递增。所以答案是满足 need(h) ≤ K 的最大 h，
在最低高度与它加 K 之间二分查找即可。`O(N · M · log K)`。

注意事项：

- 答案可能超过 10⁷，而 need(h) 可达 10⁴ · 10⁷，需要 64 位（测试 03、12）；
- 剩下的集装箱除非分到这一层的每个格子，否则不会抬高最低值（测试 05）；
- K = 10⁷ 时逐个模拟太慢。

在 199 个小仓库上，与用堆逐个放置集装箱的结果比较过。

## 优化解法

新的 Go、Rust 利用初始高度 H=1000 的上界。统计各高度的堆数，从高度 1 逐层提高水位。在离开高度 h 前把该高度的堆加入活跃数；下一完整层需要每个活跃堆各一个集装箱。预算不足则最终最小值就是 h。所有堆活跃后，用剩余预算除以 N·M 直接跳跃，不完整的一层不影响最小值。时间 O(N·M+H)、空间 O(H)，无需排序或重复可行性扫描。预算使用 64 位整数。保留二分基础版，C++、Java、Python 的基础版也覆盖快速集合。

已通过评测的基础实现 [1279_binary_search.cpp](1279_binary_search.cpp), [1279_binary_search.java](1279_binary_search.java), [1279_binary_search.py](1279_binary_search.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1279_sorting_optimized.py`. 排序所有区段高度，逐步把最低前缀提升到下一高度；容器不足时，用剩余量除以前缀长度。以排序后单次扫描替代高度二分，时间 O(nm log(nm))，空间 O(nm)。 独立程序先刷新两个输出流，再调用 os._exit(0)，在完整答案写出后跳过解释器清理。这只改变进程结束方式，不改变数学算法；简单版本仍保留。

Accepted #11328665 (Python 3.12 x64): **0.062 s / 1296 KB**. 历史对照: `1279_binary_search.py` (Python 3.12 x64) — 0.109 s / 1344 KB (#11284394).

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1279_binary_search_implementation_optimized.rs`. C 入口直接调用求解函数，返回前刷新 Rust 输出；保留普通入口的原实现。

Accepted #11328966 (Rust 1.75 x64): **0.015 s / 460 KB**. 历史对照: `1279_binary_search.rs` (Rust 1.75 x64) — 0.031 s / 512 KB (#11284398).

## 各语言说明

以下说明针对基础实现。

- 所有语言的二分查找相同；Python 用任意精度整数求和，其余用 64 位整数。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1279_binary_search.cpp](1279_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N · M · log K) | AC | 0.015 s | 280 KB | 11284386 |
| [1279_binary_search.go](1279_binary_search.go) | Go 1.14 x64 | binary_search | O(N · M · log K) | AC | 0.031 s | 1208 KB | 11284389 |
| [1279_binary_search.java](1279_binary_search.java) | Java 1.8 | binary_search | O(N · M · log K) | AC | 0.109 s | 600 KB | 11284396 |
| [1279_binary_search.py](1279_binary_search.py) | Python 3.12 x64 | binary_search | O(N · M · log K) | AC | 0.109 s | 1344 KB | 11284394 |
| [1279_binary_search.rs](1279_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N · M · log K) | AC | 0.031 s | 512 KB | 11284398 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1279_greedy.go](1279_greedy.go) | Go 1.14 x64 | greedy | O(N·M + H) | AC | 0.015 s | 320 KB | 11314936 |
| [1279_greedy.rs](1279_greedy.rs) \* | Rust 1.75 x64 | greedy | O(N·M + H) | AC | 0.031 s | 56 KB | 11314955 |
| [1279_sorting_optimized.py](1279_sorting_optimized.py) | Python 3.12 x64 | sorting | O(nm log(nm)) time; O(nm) space | AC | 0.062 s | 1296 KB | 11328665 |
| [1279_binary_search_implementation_optimized.rs](1279_binary_search_implementation_optimized.rs) | Rust 1.75 x64 | binary_search, implementation | O(N · M · log K) | AC | 0.015 s | 460 KB | 11328966 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
