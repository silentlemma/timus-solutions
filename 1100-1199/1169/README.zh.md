# 1169. 恰好有 K 个关键计算机对的连通网络

[Timus 1169](https://acm.timus.ru/problem.aspx?space=1&num=1169) · 难度 728 · constructive

原题作者 Mugurel Ionut Andreica，出自 2001 年 12 月的 Romanian Open Contest（罗马尼亚公开赛）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

用双向连接把 `N ≤ 100` 台计算机连成一个网络。若删除某一条连接会使两台计算机
不再连通，则这对计算机是关键的。构造一个恰好有 `K` 个关键对的网络，或者说明
不存在。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N` 和 `K`。

## 输出

所有连接，每行一对计算机；或者 `-1`。

## 评测方式

只要连接互不相同、连接的是不同的计算机、把所有计算机连通并且恰好产生 `K` 个
关键对，就被接受；检查程序自己求桥并统计关键对。`-1` 必须与保存的答案一致。

## 样例

### 样例 1

输入：

```
7 12
```

输出：

```
1 2
1 3
2 3
3 4
4 5
4 6
4 7
5 6
5 7
6 7
```

## 解法

去掉连通网络中的桥，网络会分成若干边双连通部分，两台计算机构成非关键对当且仅当
它们在同一部分中。一个部分要么只有一台计算机，要么至少三台（两台计算机之间需要
两条连接），而任何这样的大小都能实现：把每个大小 `s ≥ 3` 的部分做成一个环，再用
单条连接把各部分串成一条链，这些连接就是桥。所以问题变成：能否把 `N` 拆成取自
`{1, 3, 4, …}` 的大小，使 `Σ s·(s − 1)/2 = N·(N − 1)/2 − K`。

这是一个小背包：`reach[m][t]` 表示能否把 `m` 台计算机拆分得到 `t` 个非关键对。
加入一个大小为 `s` 的部分，把 `reach[m − s][t]` 转移到 `reach[m][t + s(s − 1)/2]`。
从 `reach[N][target]` 倒推即可还原各部分大小。最坏 `O(N²·N²)` 次位操作，约
五千万，用位集则少得多。

注意事项：

- 不存在两台计算机的部分，所以比如一个三角形加一棵树可行，而恰好一个非关键对
  不可行；
- `N = 1` 时不需要连接，且只可能 `K = 0`；
- 树让所有对都是关键的，单个环则一个都没有。

所有判定已与另一份独立编写的解答比对：`N ≤ 12` 时的全部 `K`，以及 300 组
`N ≤ 100` 的随机输入；每个输出的网络都通过了检查程序。

## 各语言说明

- C++ 把每个 `reach[m]` 存为 bitset，Python 存为大整数，所以加入一个部分只需
  一次移位；Go、Java 和 Rust 用普通的布尔表。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1169_constructive.cpp](1169_constructive.cpp) | G++ 13.2 x64 | constructive | O(N⁴) bit steps | AC | 0.015 s | 252 KB |
| [1169_constructive.go](1169_constructive.go) | Go 1.14 x64 | constructive | O(N⁴) bit steps | AC | 0.062 s | 1676 KB |
| [1169_constructive.java](1169_constructive.java) | Java 1.8 | constructive | O(N⁴) bit steps | AC | 0.250 s | 2152 KB |
| [1169_constructive.py](1169_constructive.py) | Python 3.12 x64 | constructive | O(N⁴) bit steps | AC | 0.093 s | 572 KB |
| [1169_constructive.rs](1169_constructive.rs) | Rust 1.75 x64 | constructive | O(N⁴) bit steps | AC | 0.046 s | 620 KB |
