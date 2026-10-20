# 2182. 按盒子编号中 1 的个数繁殖的酒瓶

[Timus 2182](https://acm.timus.ru/problem.aspx?space=1&num=2182) · 难度 710 · dp, combinatorics

原题作者 Artyom Kutuzov，出自 2024 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

编号为 1 … 2ⁿ − 1 的酒瓶放进同编号的盒子。把一瓶酒放进盒子 k 会产生一瓶编号为 popcount(k)（k 的二进制中 1 的个数）的新酒瓶，除非它等于 k；新酒瓶放进它的盒子，同样继续产生。对 q 个盒子输出最终各有多少瓶。时间限制 1 秒，内存限制 256 MB。

## 输入

n（1 ≤ n ≤ 60），q（1 ≤ q ≤ 10⁵），然后是盒子编号（1 ≤ aᵢ ≤ 2ⁿ − 1）。

## 输出

每个被询问盒子中的瓶数。

## 样例

### 样例 1

输入：

```
5
2
8 4
```

输出：

```
1 6
```

## 解法

每瓶落入盒子 j 的酒，在 popcount(j) 不等于 j 时都会向盒子 popcount(j) 送去一瓶。所以设 c(k) 为盒子 k 的最终瓶数，

c(k) = 1 + Σ c(j)，对所有 j ≠ k 且 popcount(j) = k 的盒子求和。

编号大于 60 的盒子什么也收不到，因为小于 2⁶⁰ 的数至多有 60 个 1，所以这些盒子只有一瓶。对 k ≤ 60，popcount(j) = k 的盒子 j 共有 C(n, k) 个；除了少数不超过 60 的以外，每个都只有一瓶，所以 c(k) 等于 C(n, k) 加 1，再加上 j ≤ 60 且 popcount(j) = k 的小盒子中多出的瓶数，当 k = 1 时还要减去 j = k 的那一个。由于 j > 1 时 popcount(j) < j，从 60 往下填到 1 只会用到已算好的值。最大的瓶数约为 2⁶⁰，仍在 64 位之内，每个询问只需查表。

样例中盒子 4 得到自己的一瓶，以及来自 C(5, 4) = 5 个盒子 15、23、27、29、30 的各一瓶。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2182_dp_combinatorics.cpp](2182_dp_combinatorics.cpp) | G++ 13.2 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.140 s | 692 KB |
| [2182_dp_combinatorics.go](2182_dp_combinatorics.go) | Go 1.14 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.031 s | 4308 KB |
| [2182_dp_combinatorics.java](2182_dp_combinatorics.java) | Java 1.8 | dp, combinatorics | O(60^2 + q) | AC | 0.187 s | 24904 KB |
| [2182_dp_combinatorics.py](2182_dp_combinatorics.py) | Python 3.12 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.109 s | 13712 KB |
| [2182_dp_combinatorics.rs](2182_dp_combinatorics.rs) | Rust 1.75 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.046 s | 6904 KB |
