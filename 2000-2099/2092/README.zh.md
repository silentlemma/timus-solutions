# 2092. 一张套票加单票的最低花费

[Timus 2092](https://acm.timus.ru/problem.aspx?space=1&num=2092) · 难度 1174 · greedy, binary_search

原题作者 Denis Dublennykh，出自 2014 年乌拉尔联邦大学公开个人赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 n 场音乐会，第 i 场价格为 sᵢ，单独买票有 dᵢ% 的学生折扣。第 j 类套票可包含任意 kⱼ 场或更多音乐会，按总价打 pⱼ% 的折扣，但套票内学生折扣不适用。每场音乐会去一次。求最低总花费。时间限制 1 秒，内存限制 64 MB。

## 输入

n 和 m（2 ≤ n ≤ 10⁵，1 ≤ m ≤ 10⁵），n 对 sᵢ（100 到 50 000）和 dᵢ（0 到 100），然后是 m 对 kⱼ（2 到 n）和 pⱼ（1 到 100）。

## 输出

最低花费，绝对或相对误差不超过 10⁻⁶。

## 样例

### 样例 1

输入：

```
6 2
500 0
700 0
300 0
400 0
500 50
800 0
5 10
6 15
```

输出：

```
2680.00
```

## 解法

从不需要两张套票：把它们合并成折扣较大的那张，覆盖同样的音乐会更便宜，场数也仍然足够。对折扣 p 只有提供它的最小 k 有意义，而折扣更小且 k 不更小的类型没用，所以从 100 往下尝试折扣，只保留 k 比所有更大折扣都小的那些。

所有费用都以百分之一卢布计：单票价格为 s (100 − d)，同一场在套票中为 s (100 − p)。用折扣 p 的套票时，所有 d < p 的音乐会都放进去，其余单独买；若这样不足 k 场，缺少的就取代价最小的转移，每场 d ≥ p 的音乐会增加 s (d − p)。音乐会按折扣分组，组内按价格排序并求前缀和，所以 need 个最便宜转移的代价可以对额外代价二分求出：阈值为 x 时，折扣为 d 的组贡献 s ≤ x / (d − p) 的音乐会。最终阈值上的转移代价都相同，所以多出的部分可以精确减去。每个折扣耗时 O(101 log² n)，答案取这些值与全部单独购票中的最小者。

样例中第五场以外全部放进 10% 套票，花费 2700 · 0.9 = 2430，第五场单票享受 50% 折扣花费 250：共 2680。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2092_greedy_binary_search.cpp](2092_greedy_binary_search.cpp) | G++ 13.2 x64 | greedy, binary_search | O(m + 101 log^2 n) | AC | 0.234 s | 1620 KB |
| [2092_greedy_binary_search.go](2092_greedy_binary_search.go) | Go 1.14 x64 | greedy, binary_search | O(m + 101 log^2 n) | AC | 0.046 s | 7356 KB |
| [2092_greedy_binary_search.java](2092_greedy_binary_search.java) | Java 1.8 | greedy, binary_search | O(m + 101 log^2 n) | AC | 0.125 s | 2480 KB |
| [2092_greedy_binary_search.py](2092_greedy_binary_search.py) | Python 3.12 x64 | greedy, binary_search | O(m + 101 log^2 n) | AC | 0.187 s | 26884 KB |
| [2092_greedy_binary_search.rs](2092_greedy_binary_search.rs) | Rust 1.75 x64 | greedy, binary_search | O(m + 101 log^2 n) | AC | 0.015 s | 4348 KB |
