# 2162. 统计数组中表示简单图的连续段

[Timus 2162](https://acm.timus.ru/problem.aspx?space=1&num=2162) · 难度 1114 · hashing, segment_tree

原题作者 Valentin Zuev，出自 2021 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

简单图写作 N、M，然后是 M 对 1 到 N 之间的顶点，要求 N ≥ 1、没有自环、没有重边。统计 K 个数的数组中有多少个连续段恰好是这样的记录。时间限制 2 秒，内存限制 256 MB。

## 输入

K（1 ≤ K ≤ 10⁵），然后是这些数，每个在 0 到 10⁹ 之间。

## 输出

段的个数。

## 样例

### 样例 1

输入：

```
12
2 2 2 2 1 1 2 1 2 1 0 0
```

输出：

```
3
```

## 解法

起点 s 决定了整个段：N = a[s]，M = a[s + 1]，边就是其后的 M 对数，所以候选至多 K 个。候选合法当且仅当 N ≥ 1、段放得下，且其中的数对：

- 不含 0，也没有两数相等的对；
- 没有重复的无序对；
- 只用到不超过 N 的数。

一个候选的数对都从同一奇偶性的位置开始，所以前两个条件对两种奇偶性各从右往左预处理：对每个数对位置 p，good(p) 是从 p 开始的合格数对序列必须停止的位置，即最早的坏数对或已出现数对的下一次出现，用一个从无序对到其最近后续位置的哈希表求出。候选的终点不超过 good(s + 2) 时就满足这两个条件。第三个条件是区间最大值，由线段树给出。M = 0 时记录就是 "N 0"。工作量 O(K log K)。

样例中三个合法记录是 "2 1 1 2"、"2 1 2 1" 和 "1 0"。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2162_hashing_segment_tree.cpp](2162_hashing_segment_tree.cpp) | G++ 13.2 x64 | hashing, segment_tree | O(K log K) | AC | 0.031 s | 3988 KB |
| [2162_hashing_segment_tree.go](2162_hashing_segment_tree.go) | Go 1.14 x64 | hashing, segment_tree | O(K log K) | AC | 0.046 s | 8964 KB |
| [2162_hashing_segment_tree.java](2162_hashing_segment_tree.java) | Java 1.8 | hashing, segment_tree | O(K log K) | AC | 0.125 s | 13232 KB |
| [2162_hashing_segment_tree.py](2162_hashing_segment_tree.py) | Python 3.12 x64 | hashing, segment_tree | O(K log K) | AC | 0.687 s | 15264 KB |
| [2162_hashing_segment_tree.rs](2162_hashing_segment_tree.rs) | Rust 1.75 x64 | hashing, segment_tree | O(K log K) | AC | 0.031 s | 5560 KB |
