# 2182. 按盒子编号中 1 的个数繁殖的酒瓶

[Timus 2182](https://acm.timus.ru/problem.aspx?space=1&num=2182) · 难度 663 · dp, combinatorics

原题作者 Artyom Kutuzov，出自 2024 年乌拉尔团队程序设计竞赛。

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

编号大于 60 的盒子什么也收不到，因为小于 2⁶⁰ 的数至多有 60 个 1，所以这些盒子只有一瓶。对 k ≤ 60，popcount(j) = k 的盒子 j 共有 C(n, k) 个；除了少数不超过 60 的以外，每个都只有一瓶，所以 c(k) 等于 C(n, k) 加 1，再加上 k < j ≤ 60 且 popcount(j) = k 的小盒子中多出的瓶数，当 k = 1 时还要减去 j = k 的那一个。由于 j > 1 时 popcount(j) < j，从 60 往下填到 1 只会用到已算好的值。最大的瓶数约为 2⁶⁰，仍在 64 位之内，每个询问只需查表。

样例中盒子 4 得到自己的一瓶，以及来自 C(5, 4) = 5 个盒子 15、23、27、29、30 的各一瓶。

## 优化解法

依次计算二项式系数，无需构造杨辉三角。每个编号小的盒子把额外的瓶子传给编号为其二进制置位数的唯一更小盒子。预先保存计数的文本表示，并逐个读取和回答查询。

**优化版本的 Timus 提交记录**

`2182_dp_combinatorics_optimized.cpp` (G++ 13.2 x64) №11320975 · `2182_dp_combinatorics_optimized.java` (Java 1.8) №11317427 · `2182_dp_combinatorics_optimized.py` (Python 3.12 x64) №11317438.

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11321973 · Go 1.14 x64 №11321784 · Java 1.8 №11321975 · Python 3.12 x64 №11321977 · Rust 1.75 x64 №11321980.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [2182_dp_combinatorics.cpp](2182_dp_combinatorics.cpp) | G++ 13.2 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.125 s | 668 KB | 11321973 |
| [2182_dp_combinatorics.go](2182_dp_combinatorics.go) | Go 1.14 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.031 s | 4308 KB | 11321784 |
| [2182_dp_combinatorics.java](2182_dp_combinatorics.java) | Java 1.8 | dp, combinatorics | O(60^2 + q) | AC | 0.14 s | 24916 KB | 11321975 |
| [2182_dp_combinatorics.py](2182_dp_combinatorics.py) | Python 3.12 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.109 s | 12936 KB | 11321977 |
| [2182_dp_combinatorics.rs](2182_dp_combinatorics.rs) | Rust 1.75 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.046 s | 6904 KB | 11321980 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [2182_dp_combinatorics_optimized.java](2182_dp_combinatorics_optimized.java) | Java 1.8 | dp, combinatorics | O(n + q) | AC | 0.14 s | 500 KB | 11317427 |
| [2182_dp_combinatorics_optimized.py](2182_dp_combinatorics_optimized.py) | Python 3.12 x64 | dp, combinatorics | O(n + q) | AC | 0.109 s | 1876 KB | 11317438 |
| [2182_dp_combinatorics_optimized.cpp](2182_dp_combinatorics_optimized.cpp) | G++ 13.2 x64 | dp, combinatorics | O(n + q) | AC | 0.031 s | 160 KB | 11320975 |
| [2182_dp_combinatorics_optimized.go](2182_dp_combinatorics_optimized.go) | Go 1.14 x64 | dp, combinatorics | O(n + q) | AC | 0.046 s | 924 KB | 11322385 |
| [2182_dp_combinatorics_optimized.rs](2182_dp_combinatorics_optimized.rs) | Rust 1.75 x64 | dp, combinatorics | O(n + q) | AC | 0.031 s | 212 KB | 11322386 |
