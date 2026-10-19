# 1860. 斐波阶乘

[Timus 1860](https://acm.timus.ru/problem.aspx?space=1&num=1860) · 难度 469 · number_theory

原题作者 Denis Dublennykh（创意来自 Grigoriy Nazarov），出自 2011 年 8 月彼得罗扎沃茨克夏季集训的 Ural SU Team.GOV Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

设 F₀ = F₁ = 1，Fᵢ = i·Fᵢ₋₁·Fᵢ₋₂。求 Fₙ 的约数个数模 10⁹ + 7。

## 输入

n（1 ≤ n ≤ 10⁶）。

## 输出

Fₙ 的约数个数模 10⁹ + 7。

## 样例

### 样例 1

输入：

```
3
```

输出：

```
4
```

## 解法

每一步乘上一次 i，并重复前两个乘积，所以因子 k 在 Fₙ 中恰好出现 fib(n − k + 1) 次，其中 fib(1) = fib(2) = 1：它在 F_k 中出现一次，在 F_{k+1} 中一次，在 F_{k+2} 中两次，依此按斐波那契规律。因此 Fₙ = Π k^fib(n−k+1)，k = 1 … n。

约数个数等于对所有质数 p 的 Π (e_p + 1)，其中 e_p 是 p 在 Fₙ 中的指数。数 k 贡献 v_p(k) 乘以它的权重 fib(n − k + 1)，而 v_p(k) 数的是 p、p²、p³ … 中有多少个整除 k，所以 e_p 就是 p、p² 等的所有倍数的权重之和。
只需要 e_p 模 10⁹ + 7 的值，所以权重也保持取模。遍历每个质数幂的倍数共约 n·ln ln n 步；Python 版本用一次切片对每个等差数列求和。`O(n log log n)`。

在样例中 F₃ = 3·F₂·F₁ = 3·2·1 = 6，它的约数是 1、2、3 和 6。

注意事项：

- 指数非常大，但答案只需要它们模 10⁹ + 7；
- 质数幂超过 n 时必须在溢出之前停止循环；
- Python 版本在 PyPy 上运行。

对 n 不超过 14，答案与 Fₙ 的直接分解一致；直到 10⁶，与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1860_number_theory.cpp](1860_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log log n) | AC | 0.031 s | 15508 KB |
| [1860_number_theory.go](1860_number_theory.go) | Go 1.14 x64 | number_theory | O(n log log n) | AC | 0.046 s | 18860 KB |
| [1860_number_theory.java](1860_number_theory.java) | Java 1.8 | number_theory | O(n log log n) | AC | 0.140 s | 18448 KB |
| [1860_number_theory.py](1860_number_theory.py) | PyPy 3.10 x64 | number_theory | O(n log log n) | AC | 0.187 s | 34144 KB |
| [1860_number_theory.rs](1860_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log log n) | AC | 0.062 s | 16688 KB |
