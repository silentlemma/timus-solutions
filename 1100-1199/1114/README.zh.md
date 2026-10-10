# 1114. 把至多 A 个和 B 个两种颜色的相同小球放进 N 个盒子

[Timus 1114](https://acm.timus.ru/problem.aspx?space=1&num=1114) · 难度 193 · combinatorics

原题出自保加利亚 IOI 国家队第一次选拔赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一排有 `N` 个盒子（`1 ≤ N ≤ 20`），有 `A` 个相同的红球和 `B` 个相同的蓝球（`0 ≤ A, B ≤ 15`）。每个盒子里可以放任意多个任意颜色的球，盒子可以空着，球也可以不用完。求不同放法的个数。

时间限制：0.6 秒。内存限制：64 MB。

## 输入

一行 `N A B`。

## 输出

放法的个数。

## 评测方式

输出按记号逐个比较；多余的空白字符无关紧要。

## 样例

### 样例 1

输入：

```
2 1 1
```

输出：

```
9
```

## 解法

两种颜色相互独立，所以答案是两种颜色各自方案数的乘积。把至多 `A` 个相同的球放进 `N` 个盒子，等同于把恰好 `A` 个球放进 `N + 1`
个盒子，多出的盒子装未使用的球；由隔板法，这是 `C(A + N, N)`。答案 `C(A + N, N) · C(B + N, N)` 从杨辉三角中读出。建三角为
`O((A + N)²)`，表建好后为 `O(1)`。

注意事项：

- 最大情况 `N = 20, A = B = 15` 给出 `C(35, 20)² ≈ 1.05 · 10^19`，超过有符号 64 位整数的最大值 `9.22 · 10^18`，但能放进无符号 64 位整数；
- 允许有未使用的球：若只计算把全部 `A` 个球放完的方案，得到的是 `C(A + N − 1, N − 1)`。

答案经过验证：与一个按盒子进行的动态规划比对，它统计使用每种球数的放法，再对不超过 `A` 和 `B` 的情况求和。

## 各语言说明

- C++、Go 和 Rust 用无符号 64 位整数相乘；Java 没有无符号类型，所以用 `long` 相乘（其 64 位在模 `2^64` 意义下正确），再用
  `Long.toUnsignedString` 输出；Python 的整数不会溢出。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1114_combinatorics.cpp](1114_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O((A + N)²) | AC | 0.015 s | 140 KB |
| [1114_combinatorics.go](1114_combinatorics.go) | Go 1.14 x64 | combinatorics | O((A + N)²) | AC | 0.015 s | 1060 KB |
| [1114_combinatorics.java](1114_combinatorics.java) | Java 1.8 | combinatorics | O((A + N)²) | AC | 0.109 s | 1648 KB |
| [1114_combinatorics.py](1114_combinatorics.py) | Python 3.12 x64 | combinatorics | O((A + N)²) | AC | 0.078 s | 372 KB |
| [1114_combinatorics.rs](1114_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O((A + N)²) | AC | 0.015 s | 232 KB |
