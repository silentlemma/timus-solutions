# 1273. 枕木

[Timus 1273](https://acm.timus.ru/problem.aspx?space=1&num=1273) · 难度 464 · dp

原题作者 Magaz Asanov（由 Leonid Volkov 准备），出自 2003 年 10 月 25 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

两条铁轨是直线 x = 0 和 x = 1。K ≤ 100 根枕木中的每一根连接整点 (0, Y1) 与 (1, Y2)，
|Y1|, |Y2| ≤ 1000；任意两根枕木的左端点互不相同，右端点也互不相同。移走尽量少的枕木，
使剩下的任意两根都不相交。

时间限制：1 秒。内存限制：64 MB。

## 输入

K，然后是 K 对 Y1 Y2。

## 输出

最少需要移走的枕木数。

## 样例

### 样例 1

输入：

```
3
0 1
3 0
1 2
```

输出：

```
1
```

## 解法

由于端点从不重合，两根枕木相交当且仅当它们的左端点与右端点顺序相反。按左端点排序后，
无交叉的集合就是右端点递增的集合，能保留的最多枕木数就是右端点的最长上升子序列长度。
答案是 K 减去它，用以最后保留的枕木为状态的平方 DP 求出。`O(K²)`。

注意事项：

- 输入不按任何一端排序（测试 06）；
- K 可能为 0（测试 02）；
- 坐标可以为负。

在 119 个最多 12 根枕木的随机数据上，与枚举所有子集的结果比较过。

## 优化解法

排序加二分版本仍先按左端点排序，再求右端点的最长严格递增子序列。用 tails[i] 记录长度为 i+1 的递增子序列能够取得的最小末尾，代替平方动态规划。对下一个坐标，替换首个不小于它的末尾；若不存在则延长数组。更小的末尾保留所有可行的后续扩展，因此已使用的长度就是最优值，答案为 K 减去该长度。排序及二分共耗时 O(K log K)，空间 O(K)；K = 0 时输出 0。

通过评测的 Rust 1.75 x64 版本耗时 0.031 秒，基础版为 0.015 秒，内存为 56 KB，基础版为 232 KB。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1273_dp_binary_search_optimized.py`. 使用 bisect_left 查找严格递增子序列尾值的位置，保持原来的不变量和 O(n log n) 时间。 独立程序先刷新两个输出流，再调用 os._exit(0)，在完整答案写出后跳过解释器清理。这只改变进程结束方式，不改变数学算法；简单版本仍保留。

Accepted #11328532 (Python 3.12 x64): **0.078 s / 712 KB**. 历史对照: `1273_dp.py` (Python 3.12 x64) — 0.093 s / 392 KB (#11284283).

## 各语言说明

所有简单版本保留平方动态规划。新的 Go 和 Java 实现把两个平移后的坐标打包为一个整数；每个坐标在 0..2000 内，占 11 位。对打包值排序即可按左端点排序，用掩码还原右端点。C++、Rust 使用 K ≤ 100 的定长数组，Python 使用 bisect_left。Go 使用标准句柄，Rust 使用有界 C runtime 输入输出及 C 入口。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1273_dp.cpp](1273_dp.cpp) | G++ 13.2 x64 | dp | O(K²) | AC | 0.015 s | 192 KB | 11284277 |
| [1273_dp.go](1273_dp.go) | Go 1.14 x64 | dp | O(K²) | AC | 0.015 s | 1140 KB | 11284281 |
| [1273_dp.java](1273_dp.java) | Java 1.8 | dp | O(K²) | AC | 0.140 s | 2780 KB | 11284285 |
| [1273_dp.py](1273_dp.py) | Python 3.12 x64 | dp | O(K²) | AC | 0.093 s | 392 KB | 11284283 |
| [1273_dp.rs](1273_dp.rs) | Rust 1.75 x64 | dp | O(K²) | AC | 0.015 s | 232 KB | 11284290 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1273_binary_search_sorting.cpp](1273_binary_search_sorting.cpp) | G++ 13.2 x64 | binary_search, sorting | O(K log K) | AC | 0.001 s | 116 KB | 11314674 |
| [1273_binary_search_sorting.go](1273_binary_search_sorting.go) \* | Go 1.14 x64 | binary_search, sorting | O(K log K) | AC | 0.015 s | 260 KB | 11314678 |
| [1273_binary_search_sorting.java](1273_binary_search_sorting.java) | Java 1.8 | binary_search, sorting | O(K log K) | AC | 0.109 s | 392 KB | 11314681 |
| [1273_binary_search_sorting.py](1273_binary_search_sorting.py) | Python 3.12 x64 | binary_search, sorting | O(K log K) | AC | 0.093 s | 384 KB | 11314686 |
| [1273_binary_search_sorting.rs](1273_binary_search_sorting.rs) | Rust 1.75 x64 | binary_search, sorting | O(K log K) | AC | 0.031 s | 56 KB | 11314875 |
| [1273_dp_binary_search_optimized.py](1273_dp_binary_search_optimized.py) | Python 3.12 x64 | dp, binary_search | O(K log K) time; O(K) space | AC | 0.078 s | 712 KB | 11328532 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
