# 1734. 残局库

[Timus 1734](https://acm.timus.ru/problem.aspx?space=1&num=1734) · 难度 2122 · combinatorics

原题作者 Igor Chevdar，出自第十四届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计 n × n 跳棋盘上恰好有 k 个棋子的局面数。棋子是白色或黑色的普通棋子或王，放在深色格上；
两种颜色都必须出现，且普通棋子不能放在会升变的那一行（白棋不在最后一行，黑棋不在第一行）。输出对 10⁹ + 7 取模的结果。

## 输入

n 和 k（4 ≤ n ≤ 1000，n 为偶数，2 ≤ k ≤ n²/4）。

## 输出

局面数对 10⁹ + 7 取模。

## 样例

### 样例 1

输入：

```
4 2
```

输出：

```
172
```

## 解法

深色格共 n²/2 个：第一行 n/2 个，最后一行 n/2 个，中间 m = n²/2 − n 个。
第一行或最后一行的深色格可放三种棋子，其他格可放四种，所以不考虑颜色条件时 k 个棋子的局面数为

Σ C(n, a)·3^a·C(m, k − a)·4^(k − a)

其中 a 是两条边行上的棋子数。

再减去单色局面，由对称性减两次。对白色而言，最后一行的格只能放王，其他格可放普通棋子或王，得到

Σ C(n/2, a)·C(m + n/2, k − a)·2^(k − a)。

由于 k ≥ 2，棋盘不会为空。用到 n²/2 为止的阶乘及其逆元计算组合数。阶乘 `O(n²)`，求和 `O(n log k)`。

当 n = 4、k = 2 时第一个和为 96 + 192 + 54 = 342，第二个为 60 + 24 + 1 = 85，所以答案为 342 − 2·85 = 172。

注意事项：

- 两条边行各少一种棋子，而不只是对方的升变行；
- 对单一颜色，两条边行不同：在己方第一行两种都可以，在己方最后一行只能放王；
- 差值必须调整回 0 … 10⁹ + 6 的范围。

在 4 × 4 棋盘的所有 k 以及 6 × 6 棋盘 k 不超过 4 时，数目与逐一列举所有局面一致；在大测试上与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1734_combinatorics.cpp](1734_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n²) | AC | 0.031 s | 7736 KB |
| [1734_combinatorics.go](1734_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n²) | AC | 0.046 s | 9672 KB |
| [1734_combinatorics.java](1734_combinatorics.java) | Java 1.8 | combinatorics | O(n²) | AC | 0.171 s | 9468 KB |
| [1734_combinatorics.py](1734_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n²) | AC | 0.281 s | 39668 KB |
| [1734_combinatorics.rs](1734_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n²) | AC | 0.046 s | 7896 KB |
