# 2079. 可以跟在给定值后面的斐波那契余数

[Timus 2079](https://acm.timus.ru/problem.aspx?space=1&num=2079) · 难度 4671 · number_theory

原题作者 Vladislav Isenbaev。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

斐波那契数对素数 p 取模：x₀ = 0，x₁ = 1，xₙ = (xₙ₋₁ + xₙ₋₂) mod p。给定值 x，求所有可能跟在它后面的值，即对所有满足 x_k = x 的下标 k，不同的 x_{k+1}（下标远超周期）。时间限制 0.5 秒，内存限制 256 MB。

## 输入

素数 p（2 ≤ p < 10⁹）和 x（0 ≤ x < p）。

## 输出

不同后继值的个数，然后按升序输出这些值；若 x 从不出现，只输出 0。

## 样例

### 样例 1

输入：

```
7 0
```

输出：

```
2
1 6
```

### 样例 2

输入：

```
7 3
```

输出：

```
1
5
```

### 样例 3

输入：

```
11 4
```

输出：

```
0
```

## 解法

关键是两个事实。卡西尼恒等式 F(k+1)² − F(k+1) F(k) − F(k)² = (−1)ᵏ 在模 p 下同样成立，所以跟在 x 后面的 y 满足 y² − x y − (x² + s) = 0，其中 s = 1 或 −1。由此至多得到四个候选 y = (x ± √(5x² + 4s)) / 2，平方根用 Tonelli–Shanks 算法求。

但候选不一定真的出现：p = 61 时，尽管方程有根，x = 14 从不出现。为了检验候选，在环 F_p[t] / (t² − t − 1) 中计算，其中 tᵏ = F(k) t + F(k − 1)。数对 (x, y) 出现当且仅当 x t + (y − x) 是 t 的幂，这是离散对数问题。数列的周期在 p mod 5 为 1 或 4 时整除 p − 1，否则整除 2(p + 1)，所以用小步大步法——存 m ≈ √p 或 √(2p) 个小步 tⁱ，大步乘以 t⁻ᵐ = (t − 1)ᵐ——使用哈希表时预期耗时 O(√p)，C++ 使用排序表时为 O(√p log p)。不超过 50 的素数（包括公式不适用的 2 和 5）直接遍历整个周期，周期长度至多 4p + 4。

第一个样例中 x = 0 给出模 7 下 y² = ±1；−1 不是平方数，而 1（k = 0）和 6（k = 8，F(9) = 34）都会出现。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2079_number_theory.cpp](2079_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt p log p) | AC | 0.015 s | 1264 KB |
| [2079_number_theory.go](2079_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt p) | AC | 0.031 s | 2528 KB |
| [2079_number_theory.java](2079_number_theory.java) | Java 1.8 | number_theory | O(sqrt p) | AC | 0.156 s | 4712 KB |
| [2079_number_theory.py](2079_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt p) | AC | 0.140 s | 8656 KB |
| [2079_number_theory.rs](2079_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt p) | AC | 0.062 s | 2436 KB |
