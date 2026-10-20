# 2126. 红队获胜：模素数的中心三项式系数

[Timus 2126](https://acm.timus.ru/problem.aspx?space=1&num=2126) · 难度 1654 · math, combinatorics

原题作者 Alexander Zimin，出自 2018 年夏季彼得罗扎沃茨克集训营 t.me/umnik_team 专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 个人中的每一个独立地加入红队、加入蓝队或观战，概率各为 1/3。人数多的队获胜。设 t 为红队获胜的概率，输出 t · 3ⁿ 对素数 p 取模的值，即 3ⁿ 种选择中红队人数更多的选择数。时间限制 1 秒，内存限制 64 MB。

## 输入

n 和 p（1 ≤ n ≤ 10¹⁸，5 ≤ p < 10⁶，p 为素数）。

## 输出

该数对 p 取模。

## 样例

### 样例 1

输入：

```
5 5
```

输出：

```
1
```

### 样例 2

输入：

```
5 7
```

输出：

```
5
```

## 解法

交换两种颜色可知红队和蓝队获胜的次数相同，所以答案是 (3ⁿ − D) / 2，其中 D 是平局数。给每个人赋权：红队为 x，观战为 1，蓝队为 x⁻¹，则 D 是 (x + 1 + x⁻¹)ⁿ 的常数项，即中心三项式系数 Tₙ。除以 2 就是乘以 (p + 1) / 2。

由于模 p 有 (1 + x + x²)ᵖ ≡ 1 + xᵖ + x²ᵖ，这些系数满足 Lucas 性质：Tₙ 等于 n 的各个 p 进制数位 d 对应的 T_d 之积。数位都小于 p < 10⁶，而 Tₖ 满足递推

(k + 1) T_{k+1} = (2k + 1) Tₖ + 3k T_{k−1}。

为了避免每一步都做除法，程序维护 Fₖ = k! · Tₖ，它满足 F_{k+1} = (2k + 1) Fₖ + 3k² F_{k−1}，最后再统一除以阶乘；数位已排序，所以一次扫描就能到达所有数位。大于 (p − 1) / 2 的数位先用 T_{p−1−d} ≡ (−3)^{(p−1)/2 − d} T_d (mod p) 反射，所以扫描不会超过 (p − 1) / 2。3ⁿ 用快速幂求得，总工作量 O(p)。

第一个样例中 T₅ = 51，3⁵ = 243，(243 − 51) / 2 = 96 ≡ 1 (mod 5)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2126_math_combinatorics.cpp](2126_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(p + log n) | AC | 0.015 s | 396 KB |
| [2126_math_combinatorics.go](2126_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(p + log n) | AC | 0.046 s | 1124 KB |
| [2126_math_combinatorics.java](2126_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(p + log n) | AC | 0.109 s | 456 KB |
| [2126_math_combinatorics.py](2126_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(p + log n) | AC | 0.140 s | 544 KB |
| [2126_math_combinatorics.rs](2126_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(p + log n) | AC | 0.046 s | 232 KB |
