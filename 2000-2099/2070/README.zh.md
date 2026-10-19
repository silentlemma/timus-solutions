# 2070. 因数个数为质数的质数幂

[Timus 2070](https://acm.timus.ru/problem.aspx?space=1&num=2070) · 难度 234 · number_theory

原题作者 Alexey Danilyuk，出自 2015 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个人认为整数是质数时有趣，另一个人认为整数的正因数个数是质数时有趣。若两人看法一致（都认为有趣或都认为无趣），这个数就令人满意。统计 [L; R] 中令人满意的整数个数。时间限制 2 秒，内存限制 64 MB。

## 输入

L 和 R（2 ≤ L ≤ R ≤ 10¹²）。

## 输出

[L; R] 中令人满意的整数个数。

## 样例

### 样例 1

输入：

```
3 7
```

输出：

```
4
```

### 样例 2

输入：

```
2 2
```

输出：

```
1
```

### 样例 3

输入：

```
77 1010
```

输出：

```
924
```

## 解法

质数有 2 个因数，而 2 是质数，所以每个质数两人都认为有趣。合数只要因数个数不是质数就令人满意。对 x = p₁^a₁ · … · pₛ^aₛ，因数个数为 (a₁ + 1) · … · (aₛ + 1)，乘积是质数只可能在只有一个因子时。所以不满意的数恰好是质数的幂 p^k，其中 k ≥ 2 且 k + 1 为质数，答案是 R − L + 1 减去它们在 [L; R] 中的个数。

由于 k ≥ 2 时 p^k ≤ 10¹²，这样的 p 都不超过 10⁶。筛出 10⁶ 以内的质数，对每个满足 p² ≤ R 的质数 p，依次枚举 p²、p³、… 直到 R，统计不小于 L 且指数加一为质数的那些。大于 10⁴ 的质数只有平方一项，所以枚举很短；主要耗时在筛法，O(N log log N)，N = 10⁶。

第一个样例中 4 = 2² 有 3 个因数，是 3 … 7 中唯一不满意的数，答案为 4。

## 各语言说明

乘法前先把幂与 R / p 比较，所以它不会超过 10¹² · 10⁶，保持在 64 位以内。Python 解法用筛表的一次切片统计 √L 与 √R 之间的质数（即平方项），只对不超过 ∛R 的质数枚举更高次幂，这样在 CPython 上也足够快。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2070_number_theory.cpp](2070_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log log N) | AC | 0.031 s | 304 KB |
| [2070_number_theory.go](2070_number_theory.go) | Go 1.14 x64 | number_theory | O(N log log N) | AC | 0.031 s | 2136 KB |
| [2070_number_theory.java](2070_number_theory.java) | Java 1.8 | number_theory | O(N log log N) | AC | 0.140 s | 2632 KB |
| [2070_number_theory.py](2070_number_theory.py) | Python 3.12 x64 | number_theory | O(N log log N) | AC | 0.109 s | 2816 KB |
| [2070_number_theory.rs](2070_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log log N) | AC | 0.062 s | 1212 KB |
