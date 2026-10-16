# 1816. Pollard 的麻烦

[Timus 1816](https://acm.timus.ru/problem.aspx?space=1&num=1816) · 难度 2272 · number_theory

原题出自 Tavrida NU Akai Contest，2010 年 8 月彼得罗扎沃茨克夏季集训。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

为了分解 n，程序在 n 为素数时停止。否则取 1 到 10¹⁸ 之间的随机数 r，计算 g = gcd(n, r)，当 g 为 1 或 n 时重复，然后用同样的方法分解 g 和 n/g。
求计算最大公约数次数的期望，误差不超过 10⁻⁶。

## 输入

n（2 ≤ n ≤ 10⁹）。

## 输出

计算最大公约数的期望次数。

## 样例

### 样例 1

输入：

```
12
```

输出：

```
4.8571428571
```

### 样例 2

输入：

```
8
```

输出：

```
6.6666666667
```

## 解法

由于 10¹⁸ 远大于 n，r mod n 在可忽略的误差下是均匀的，最大公约数按 n 的素数幂分解。若 p 在 m 中的指数为 e，则 p 在 gcd(m, r) 中的指数为 c < e 的概率是 (1 − 1/p)/pᶜ，
为 e 的概率是 1/pᵉ，各素数相互独立。对合数 m，这一步重复到最大公约数是真因子为止，所以 E(m) = (1 + Σ P(g)·(E(g) + E(m/g))) / (1 − P(1) − P(m))，
求和遍历真因子 g，且素数处 E 为 0。

遇到的数都是 n 的因子，10⁹ 以内最多 1344 个。把因子用混合进制下的指数向量编号后，因子的每个真因子编号都更小，所以 E 可以按编号递增填写。
g 和 m/g 这一对的编号就是 d 和 index − d。求和遍历 n 所有因子的所有因子，最坏约 1.4·10⁵ 项。对 n 的因子 m 为 `O(Σ d(m))`。

第二个样例中 8 = 2³：最大公约数为 1、2、4、8 的概率分别为 1/2、1/4、1/8、1/8。E(4) = 4，E(8) = (1 + 1/4·4 + 1/8·4) / (3/8) = 20/3。

注意事项：

- E(m) 出现在等式两边，因为无用的最大公约数会使这一步重复；
- 概率与素数本身有关，而不仅仅取决于指数的形状；
- 素数根本不需要计算最大公约数，所以 E(p) = 0。

在样例、素数、素数幂、因子最多的数以及随机值上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1816_number_theory.cpp](1816_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sum of d(m) over divisors m of n) | AC | 0.015 s | 248 KB |
| [1816_number_theory.go](1816_number_theory.go) | Go 1.14 x64 | number_theory | O(sum of d(m) over divisors m of n) | AC | 0.015 s | 2372 KB |
| [1816_number_theory.java](1816_number_theory.java) | Java 1.8 | number_theory | O(sum of d(m) over divisors m of n) | AC | 0.125 s | 2280 KB |
| [1816_number_theory.py](1816_number_theory.py) | Python 3.12 x64 | number_theory | O(sum of d(m) over divisors m of n) | AC | 0.093 s | 708 KB |
| [1816_number_theory.rs](1816_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sum of d(m) over divisors m of n) | AC | 0.031 s | 324 KB |
