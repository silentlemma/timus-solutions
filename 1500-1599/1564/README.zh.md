# 1564. 数 1

[Timus 1564](https://acm.timus.ru/problem.aspx?space=1&num=1564) · 难度 681 · binary_search

原题作者 Sergey Pupyrev，出自 2007 年 10 月 6 日第十二届乌拉尔国立大学程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Petya 从 1 层起沿楼梯爬一座摩天大楼，一路数楼层号中的数字 1。给定数到的个数 k（1 ≤ k ≤ 10¹⁸），输出数到
最后一个 1 的楼层；若没有哪层恰好给出 k 个 1，输出 `Petr lies`。

时间限制：1 秒。内存限制：64 MB。

## 输入

数 k。

## 输出

楼层号或 `Petr lies`。

## 样例

### 样例 1

输入:

```
4
```

输出:

```
11
```

### 样例 2

输入:

```
3
```

输出:

```
Petr lies
```

## 解法

设 f(x) 为 1, …, x 中 1 的个数。它按数位计数：在数位 p（1, 10, 100, …）上，不超过 x 的数构成
⌊x / 10p⌋ 个完整的 10p 个数的块，每块在该位上有 p 个 1；最后一个不完整的块，若该位数字大于 1 则再加 p
个，若等于 1 则加上 x 在该位以下的部分再加 1，若为 0 则不加。

f 只增不减，所以数到第 k 个 1 的楼层是第一个使 f(x) ≥ k 的 x，用二分查找在 1 … 10¹⁸ 中求得（f(10¹⁸)
约为 1.8·10¹⁸）。若 f(x) 大于 k，说明第 x 层一下子带来了好几个 1，数的过程中从未出现过 k，于是 Petya 在
撒谎。查找约 60 步，每步 O(log x)。结果已与对 25000 以内所有 k 逐层行走的做法对照。

注意事项：

- 像 11 这样的楼层一次加两个 1，所以有些个数永远不会出现（第二个样例）；
- k = 10¹⁸ 时答案约为 5.2·10¹⁷，数位到达 10¹⁸，所以不能在 64 位之外计算 p · 10（测试 05）；
- 比全是 1 的楼层处的总数少一的个数是谎言（测试 08）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1564_binary_search.cpp](1564_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(log^2 k) | AC | 0.015 s | 128 KB |
| [1564_binary_search.go](1564_binary_search.go) | Go 1.14 x64 | binary_search | O(log^2 k) | AC | 0.031 s | 1072 KB |
| [1564_binary_search.java](1564_binary_search.java) | Java 1.8 | binary_search | O(log^2 k) | AC | 0.125 s | 1608 KB |
| [1564_binary_search.py](1564_binary_search.py) | Python 3.12 x64 | binary_search | O(log^2 k) | AC | 0.078 s | 424 KB |
| [1564_binary_search.rs](1564_binary_search.rs) | Rust 1.75 x64 | binary_search | O(log^2 k) | AC | 0.015 s | 220 KB |
