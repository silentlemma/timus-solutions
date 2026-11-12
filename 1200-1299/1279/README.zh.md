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
| [1279_binary_search.py](1279_binary_search.py) \* | Python 3.12 x64 | binary_search | O(N · M · log K) | AC | 0.109 s | 1344 KB | 11284394 |
| [1279_binary_search.rs](1279_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N · M · log K) | AC | 0.031 s | 512 KB | 11284398 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1279_greedy.go](1279_greedy.go) \* | Go 1.14 x64 | greedy | O(N·M + H) | AC | 0.015 s | 320 KB | 11314936 |
| [1279_greedy.rs](1279_greedy.rs) \* | Rust 1.75 x64 | greedy | O(N·M + H) | AC | 0.031 s | 56 KB | 11314955 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
