# 1748. 最复杂的数

[Timus 1748](https://acm.timus.ru/problem.aspx?space=1&num=1748) · 难度 268 · number_theory

原题作者 Petr Lezhankin，出自 2009 年 8 月彼得罗扎沃茨克夏季集训的乌法国立航空技术大学专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个数的复杂度是它的约数个数。对每个给定的 n，求 1 到 n 中最复杂的数（有多个时取最小的）及其复杂度。

## 输入

t（1 ≤ t ≤ 100），然后是 t 个数 n（1 ≤ n ≤ 10¹⁸）。

## 输出

对每个 n 输出该数及其约数个数。

## 样例

### 样例 1

输入：

```
5
1
10
100
1000
10000
```

输出：

```
1 1
6 4
60 12
840 32
7560 64
```

## 解法

p₁^a₁ · p₂^a₂ · … 的约数个数为 (a₁ + 1)(a₂ + 1)…，只取决于指数。把最大的指数放在最小的素数上，得到具有这些指数的最小的数，
所以答案总是形如 2^a · 3^b · 5^c · …，在连续素数上满足 a ≥ b ≥ c ≥ …。10¹⁸ 以内这样的数只有几万个，
所需素数到 53 为止，因为 2 · 3 · … · 53 已超过 10¹⁸。

通过对指数的搜索把它们全部列出、排序，再从小到大扫描并记录当前最优：只有约数严格更多时才替换最优，
这样相同时保留较小者。每个询问就是二分查找不超过 n 的最后一个数。列表中有 K = 32 749 个数，复杂度 `O(K log K + t log K)`。

当 n = 100 时答案是 60 = 2² · 3 · 5，有 3 · 2 · 2 = 12 个约数。

注意事项：

- 在接近 10¹⁸ 时相乘可能溢出 64 位，应在相乘前用除法检查边界；
- 相同时较小的数胜出：2 和 3 都有两个约数。

在 100 个不超过 20 000 的随机询问上，答案与约数个数筛法一致；在 30 个不超过 10¹⁸ 以及纪录保持者附近的随机测试上，
与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1748_number_theory.cpp](1748_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log K + t log K) | AC | 0.015 s | 1924 KB |
| [1748_number_theory.go](1748_number_theory.go) | Go 1.14 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 5404 KB |
| [1748_number_theory.java](1748_number_theory.java) | Java 1.8 | number_theory | O(K log K + t log K) | AC | 0.187 s | 8084 KB |
| [1748_number_theory.py](1748_number_theory.py) | Python 3.12 x64 | number_theory | O(K log K + t log K) | AC | 0.156 s | 6608 KB |
| [1748_number_theory.rs](1748_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 1368 KB |
