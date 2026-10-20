# 2171. 被 K 个等差数列中至少一个覆盖的不超过 N 的数

[Timus 2171](https://acm.timus.ru/problem.aspx?space=1&num=2171) · 难度 1518 · math, number_theory

原题作者 Konstantin Rychkov，出自 2022 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计 1 到 N 中至少属于 K 个无限递增等差数列 bᵢ, bᵢ + dᵢ, … 之一的整数个数。时间限制 2 秒，内存限制 256 MB。

## 输入

N 和 K（1 ≤ N ≤ 10⁹，1 ≤ K ≤ 18），然后是各对 bᵢ, dᵢ（1 ≤ bᵢ, dᵢ ≤ 10⁹）。

## 输出

个数。

## 样例

### 样例 1

输入：

```
15 2
3 5
6 2
```

输出：

```
7
```

## 解法

由容斥原理，答案等于对数列的所有非空子集求和 (−1)^(大小 + 1) 乘以不超过 N 且属于该子集中所有数列的值的个数。若干数列的公共值仍构成一个等差数列，或者为空：两个数列相交当且仅当首项之差能被公差的最大公约数整除，此时扩展欧几里得算法给出不早于两个首项的第一个公共值，公差为最小公倍数（中国剩余定理）。

按深度优先遍历子集，每次向当前交集加入一个数列。一旦交集为空或起点超过 N，就停止这一分支，因为再加入数列也不会让它恢复。当公差超过到 N 为止剩下的部分时，交集只有一个值，就用公差 0 保存，这也让数保持很小。至多访问 2¹⁸ 个子集，每个 O(log)。

样例中 3, 8, 13 与 6, 8, 10, 12, 14 有公共值 8，所以答案是 3 + 5 − 1 = 7。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2171_math_number_theory.cpp](2171_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(2^K log C) | AC | 0.031 s | 216 KB |
| [2171_math_number_theory.go](2171_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(2^K log C) | AC | 0.046 s | 900 KB |
| [2171_math_number_theory.java](2171_math_number_theory.java) | Java 1.8 | math, number_theory | O(2^K log C) | AC | 0.156 s | 312 KB |
| [2171_math_number_theory.py](2171_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(2^K log C) | AC | 0.703 s | 492 KB |
| [2171_math_number_theory.rs](2171_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(2^K log C) | AC | 0.046 s | 24 KB |
