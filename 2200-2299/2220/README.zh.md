# 2220. 所有不超过 N 的数对上 1 / gcd 的平均值

[Timus 2220](https://acm.timus.ru/problem.aspx?space=1&num=2220) · 难度 685 · number_theory

原题作者 Vadim Barinov，出自 2025 年 ICPC 乌拉尔赛区资格赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

求所有数对 1 ≤ i ≤ j ≤ N 上 1 / gcd(i, j) 的平均值，对 10⁹ + 7 取模。时间限制 1.5 秒，内存限制 512 MB。

## 输入

N（1 ≤ N ≤ 10⁷）。

## 输出

平均值，以 p · q⁻¹ 对 10⁹ + 7 取模的形式输出。

## 样例

### 样例 1

输入：

```
2
```

输出：

```
833333340
```

### 样例 2

输入：

```
3
```

输出：

```
805555562
```

### 样例 3

输入：

```
1
```

输出：

```
1
```

## 解法

按最大公约数 d 对数对分组。令 i = da、j = db，则 gcd 为 d 的数对就是互质数对 a ≤ b ≤ ⌊N / d⌋，共有 Φ(⌊N / d⌋) 个，其中 Φ(m) = φ(1) + … + φ(m)。所以和为

对 d 求和 Φ(⌊N / d⌋) / d，

最后再除以数对总数 N(N + 1) / 2。

⌊N / d⌋ 只有 O(√N) 个不同的值，在商相同的每一段 d 上，需要该商的 Φ 乘以模质数意义下的调和数之差 H(right) − H(left − 1)。

- 所有商处的 Φ 由一个上界以内的 φ 筛法得到，上界以上用恒等式 Φ(x) = x(x + 1) / 2 − 对 d ≥ 2 求和 Φ(⌊x / d⌋)，同样按商分组，从较小的参数算起。
- 调和数本需要对 10⁷ 以内的每个 d 求逆元。解法改为维护 F = d! 和 W = d! · H(d)，按 W ← W · d + F、F ← F · d 更新，每一段只对 F 求一次逆元。Python 版本利用八个因子的乘积及其导数，把连续八步合并为一步。

第一个样例中数对 (1, 1)、(1, 2)、(2, 2) 给出 1 + 1 + 1/2 = 5/2，平均值为 5/6。

调和数需要 O(N) 次乘法，欧拉函数前缀和约需 O(N^(3/4))。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2220_number_theory.cpp](2220_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N + N^(3/4)) | AC | 0.062 s | 1000 KB |
| [2220_number_theory.go](2220_number_theory.go) | Go 1.14 x64 | number_theory | O(N + N^(3/4)) | AC | 0.093 s | 1704 KB |
| [2220_number_theory.java](2220_number_theory.java) | Java 1.8 | number_theory | O(N + N^(3/4)) | AC | 0.437 s | 1064 KB |
| [2220_number_theory.py](2220_number_theory.py) | PyPy 3.10 x64 | number_theory | O(N + N^(3/4)) | AC | 1.265 s | 4892 KB |
| [2220_number_theory.rs](2220_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N + N^(3/4)) | AC | 0.062 s | 800 KB |
