# 2188. 最早且之后再也不会被反超的超越

[Timus 2188](https://acm.timus.ru/problem.aspx?space=1&num=2188) · 难度 1769 · prefix_sums, binary_search

原题作者 Artyom Kutuzov，出自 2024 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

海盗的小艇起初领先 D 英尺，第 i 秒前进 bᵢ 英尺；吉姆的小艇在这一秒可以前进 0 到 aᵢ 之间的任意整数英尺。吉姆希望自己第一次在某秒末严格领先的那一秒 t 尽可能早，并且之后直到第 n 秒末一直严格领先。对 D 的 q 个猜测，分别求出这个 t，或 −1。时间限制 1 秒，内存限制 256 MB。

## 输入

n 和 q（1 ≤ n, q ≤ 10⁵），然后是 a₁ … a_n 和 b₁ … b_n（取值 0 到 10⁹），然后是 d₁ … d_q（1 ≤ dⱼ ≤ 10⁹）。

## 输出

每个猜测的答案。

## 样例

### 样例 1

输入：

```
10 10
7 4 7 0 5 6 4 4 5 4
5 3 5 1 2 3 3 7 2 0
1 2 3 4 5 6 7 8 14 15
```

输出：

```
1
2
3
5
5
5
6
10
10
-1
```

### 样例 2

输入：

```
1 4
4
1
1 2 3 4
```

输出：

```
1
1
-1
-1
```

## 解法

设 x(i) 为吉姆走过的路程减去海盗走过的路程，于是 x(i) > D 时吉姆在第 i 秒末领先；设 G(i) 为 aᵢ − bᵢ 的前缀和，即全速时的 x。两艇在一秒内都匀速运动，所以在一秒的两端都领先就意味着整秒都领先。

在 t 之前吉姆不能领先，所以最好的做法是全速前进但不超过 D。这条被截断的路径结束于 x = G(i) − max(0, Mᵢ − D)，其中 Mᵢ 是 0, G(1), …, G(i) 中的最大值。从第 t 秒起吉姆全速前进，所以设 M 为 t 之前的最大值、S 为 i ≥ t 时 G(i) 的最小值，吉姆保持领先当且仅当

S − max(0, M − D) > D，即 S > max(D, M)。

因此只有 S > M 时第 t 秒才可能可行，此时它对所有 D < S 都可行。后缀最小值 S 随 t 增大，所以有用的秒对应的阈值 S 递增，每个查询就是二分查找第一个大于 D 的阈值。

第二个样例中 G(1) = 3，所以 D = 1 和 D = 2 在第一秒超越，而 D = 3 和 D = 4 永远无法领先。

前缀和与后缀最小值需要 O(n)，查询需要 O(q log n)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2188_prefix_sums_binary_search.cpp](2188_prefix_sums_binary_search.cpp) | G++ 13.2 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.078 s | 2732 KB |
| [2188_prefix_sums_binary_search.go](2188_prefix_sums_binary_search.go) | Go 1.14 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.062 s | 12984 KB |
| [2188_prefix_sums_binary_search.java](2188_prefix_sums_binary_search.java) | Java 1.8 | prefix_sums, binary_search | O(n + q log n) | AC | 0.156 s | 5764 KB |
| [2188_prefix_sums_binary_search.py](2188_prefix_sums_binary_search.py) | Python 3.12 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.281 s | 32712 KB |
| [2188_prefix_sums_binary_search.rs](2188_prefix_sums_binary_search.rs) | Rust 1.75 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.046 s | 7212 KB |
