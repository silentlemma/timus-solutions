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

- 答案可能超过 10⁷，而 need(h) 可达 10⁴ · 10⁷，需要 64 位（测试 03）；
- 剩下的集装箱除非分到这一层的每个格子，否则不会抬高最低值（测试 05）；
- K = 10⁷ 时逐个模拟太慢。

在 199 个小仓库上，与用堆逐个放置集装箱的结果比较过。

## 各语言说明

- 所有语言都使用同样的二分查找和 64 位求和。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1279_binary_search.cpp](1279_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N · M · log K) | AC | 0.015 s | 280 KB |
| [1279_binary_search.go](1279_binary_search.go) | Go 1.14 x64 | binary_search | O(N · M · log K) | AC | 0.031 s | 1208 KB |
| [1279_binary_search.java](1279_binary_search.java) | Java 1.8 | binary_search | O(N · M · log K) | AC | 0.109 s | 600 KB |
| [1279_binary_search.py](1279_binary_search.py) | Python 3.12 x64 | binary_search | O(N · M · log K) | AC | 0.109 s | 1344 KB |
| [1279_binary_search.rs](1279_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N · M · log K) | AC | 0.031 s | 512 KB |
