# 2203. 两种食材按各自节奏用完时的购物次数

[Timus 2203](https://acm.timus.ru/problem.aspx?space=1&num=2203) · 难度 1097 · math, number_theory

原题作者 Valentin Zuev，出自 2020 年大学学术中学生信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个三明治需要 A 克面包和 B 克香肠，面包按每条 X 克出售，香肠按每根 Y 克出售。每当库存不够做下一个三明治时，就去一次商店，买够做这个三明治所需的最少条数和根数。从一无所有开始做 N 个三明治，一共要去几次商店？时间限制 1 秒，内存限制 256 MB。

## 输入

A、B、X、Y 和 N（1 ≤ A, B ≤ 100，1 ≤ X, Y, N ≤ 10⁹）。

## 输出

去商店的次数。

## 样例

### 样例 1

输入：

```
30 20 90 30 4
```

输出：

```
3
```

### 样例 2

输入：

```
5 6 7 72 100
```

输出：

```
74
```

### 样例 3

输入：

```
99 100 37 47 1000000000
```

输出：

```
1000000000
```

## 解法

若 X ≤ A，任何剩余都不足一条面包，也就不够一个三明治，所以每个三明治都要去一次；Y ≤ B 时同理。此时答案为 N。

否则每次至多买一条面包。把三明治从 0 开始编号；第 j 条面包（从 0 开始）恰好在第一次满足 (k + 1)A > jX 的三明治 k 之前购买，即 k = ⌊jX / A⌋。设 g = gcd(A, X)、P = X / g、E = A / g，则买面包的时刻是 ⌊jP / E⌋，即每 P 个三明治重复一次、含 E 次购买的模式，N 以内共有 ⌈NA / X⌉ 次。买香肠的时刻同理，有自己的 P' 和 E'。

当某个三明治编号同时属于两个模式时，一次购物同时买两样；答案是买面包的次数加买香肠的次数减去这些重合的次数。对 E · E' ≤ 10⁴ 对余数 r = ⌊iP / E⌋ 和 r' = ⌊jP' / E'⌋ 中的每一对，由中国剩余定理，满足 r + sP = r' + tP' 的编号要么不存在（当 gcd(P, P') 不整除 r' − r 时），要么构成一个公差为 lcm(P, P') 的等差数列，直接数出其中小于 N 的项。

第一个样例中买面包的时刻是 0 和 3，买香肠的时刻是 0、1 和 3，重合的是 0 和 3，答案为 2 + 3 − 2 = 3。

复杂度 O(AB + log XY)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2203_math_number_theory.cpp](2203_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(AB + log XY) | AC | 0.015 s | 184 KB |
| [2203_math_number_theory.go](2203_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(AB + log XY) | AC | 0.031 s | 912 KB |
| [2203_math_number_theory.java](2203_math_number_theory.java) | Java 1.8 | math, number_theory | O(AB + log XY) | AC | 0.093 s | 172 KB |
| [2203_math_number_theory.py](2203_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(AB + log XY) | AC | 0.093 s | 324 KB |
| [2203_math_number_theory.rs](2203_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(AB + log XY) | AC | 0.031 s | 20 KB |
