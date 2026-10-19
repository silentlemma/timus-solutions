# 2110. 恰好删除 k 个数后的最大按位或

[Timus 2110](https://acm.timus.ru/problem.aspx?space=1&num=2110) · 难度 1032 · bitmask, dp, backtracking

原题作者 Alexey Danilyuk，出自 2016 年乌拉尔联邦大学青少年锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

从 n 个非负整数中恰好删除 k 个，使剩下的数的按位或尽可能大。每个测试中要么 k ≤ 7，要么所有数都不超过 10⁵。时间限制 2 秒，内存限制 64 MB。

## 输入

n 和 k（0 ≤ k ≤ 100，k + 1 ≤ n ≤ 10⁵），然后是 n 个数，每个不超过 10⁹。

## 输出

最大的按位或。

## 样例

### 样例 1

输入：

```
4 1
32 16 8 7
```

输出：

```
56
```

### 样例 2

输入：

```
4 1
98765432 98765432 98765432 1
```

输出：

```
98765433
```

## 解法

设 F 为所有数的按位或，r = n − k 为保留的个数。F 的每个 1 位都有一个见证者，即含有该位的数，所以至多 popcount(F) 个数就能得到 F，其余位置可以随便填。因此若 r ≥ popcount(F)，答案就是 F。

否则 r < popcount(F) ≤ 30，只剩两种小情况。

- k ≤ 7：此时 n = r + k ≤ 36。按数值从大到小排序后做深度优先搜索，选择保留哪些数。当前按位或与后面所有数合起来都无法超过最优结果时剪枝；当剩余位置足够为每个尚缺的位各选一个见证者时，直接取这个上界。
- 所有数不超过 10⁵：此时 F < 2¹⁷，r ≤ 16 且 n ≤ 116。在按位或掩码上做背包，对每个掩码记录得到它所需的最少不同数个数；能用至多 r 个数得到的掩码是可行的，因为重复的数和其他数可以填满剩余位置而不会减小按位或。掩码按降序处理，保证每个数只用一次，一旦达到 F 就停止。

第二个样例中 98765432 的所有副本给出相同的位，所以删掉一个副本后 1 仍保留，答案为 98765433。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2110_bitmask_dp_backtracking.cpp](2110_bitmask_dp_backtracking.cpp) | G++ 13.2 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.031 s | 936 KB |
| [2110_bitmask_dp_backtracking.go](2110_bitmask_dp_backtracking.go) | Go 1.14 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.031 s | 2168 KB |
| [2110_bitmask_dp_backtracking.java](2110_bitmask_dp_backtracking.java) | Java 1.8 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.125 s | 1036 KB |
| [2110_bitmask_dp_backtracking.py](2110_bitmask_dp_backtracking.py) | Python 3.12 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.781 s | 11344 KB |
| [2110_bitmask_dp_backtracking.rs](2110_bitmask_dp_backtracking.rs) | Rust 1.75 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.031 s | 2148 KB |
