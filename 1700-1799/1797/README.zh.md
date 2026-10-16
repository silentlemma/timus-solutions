# 1797. Summit Online Judge（第二版）

[Timus 1797](https://acm.timus.ru/problem.aspx?space=1&num=1797) · 难度 4736 · number_theory

原题作者 Xie Lingxi，改编自 Alex Samsonov 的第 1720 题。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每场比赛有 x 道或 y 道题。若若干场比赛（至少一场）合起来恰好有某个数目的题，这个数目就是正确的卷大小。统计 l 到 r 之间正确的大小个数。最多 100 组数据。

## 输入

数据组数，然后每组给出 x、y、l、r（1 ≤ x, y, l, r ≤ 10¹⁸，l ≤ r）。

## 输出

每组数据输出正确大小的个数。

## 样例

### 样例 1

输入：

```
1
4 5 7 13
```

输出：

```
5
```

## 解法

统计不超过 N 的 a·x + b·y（a, b ≥ 0，不全为零）；答案是到 r 的个数减去到 l − 1 的个数。把 x、y 和 N 都除以 g = gcd(x, y)，使 x 与 y 互质。
此时每个可达的大小恰好有一种 0 ≤ b < x 的表示，所以到 N 的个数是 b 从 0 到 B = min(x − 1, ⌊N/y⌋) 的 ⌊(N − b·y)/x⌋ + 1 之和，再减去零这一个。
令 i = B − b，和式变为 i 从 0 到 B 的 Σ ⌊(y·i + (N − y·B))/x⌋，即一个取整求和，用类欧几里得的化简在 O(log) 步内算出：
先提出斜率和截距的整数部分，再交换斜率与模数的角色。所有中间结果都不超过最终的个数，只有乘积"斜率 × 项数 + 截距"需要 128 位。
每组 `O(log max(x, y))`。

样例中用 4 和 5 可以凑出 8、9、10、12 和 13，而 7 和 11 不行。

注意事项：

- x 与 y 可能有公因子，这时只有它的倍数才算；
- B 和区间都可达 10¹⁸，所以不能逐项累加关于 b 的和；
- 取整求和中的乘积会超出 64 位；Java 解法使用 BigInteger，Go 解法使用 bits.Mul64 和 bits.Div64；
- 零（没有比赛）不算一种大小。

在 3000 个小情形上，答案与直接统计可达大小的结果一致；在 4500 个大情形上（包括公因子、大小为 1 和相等的大小），与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1797_number_theory.cpp](1797_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log max(x, y)) per case | AC | 0.015 s | 408 KB |
| [1797_number_theory.go](1797_number_theory.go) | Go 1.14 x64 | number_theory | O(log max(x, y)) per case | AC | 0.015 s | 1092 KB |
| [1797_number_theory.java](1797_number_theory.java) | Java 1.8 | number_theory | O(log max(x, y)) per case | AC | 0.109 s | 2492 KB |
| [1797_number_theory.py](1797_number_theory.py) | Python 3.12 x64 | number_theory | O(log max(x, y)) per case | AC | 0.078 s | 440 KB |
| [1797_number_theory.rs](1797_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log max(x, y)) per case | AC | 0.015 s | 236 KB |
