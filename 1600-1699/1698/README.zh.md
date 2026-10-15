# 1698. 方形国 5

[Timus 1698](https://acm.timus.ru/problem.aspx?space=1&num=1698) · 难度 640 · number_theory

原题作者 Alex Samsonov，出自 2009 年 2 月彼得罗扎沃茨克冬季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计不超过 n 位、没有前导零、平方以自身结尾的正整数个数，例如 76² = 5776。

## 输入

n（1 ≤ n ≤ 2000）。

## 输出

个数。

## 样例

### 样例 1

输入：

```
1
```

输出：

```
3
```

## 解法

d 位数 x 符合条件当且仅当 x² ≡ x (mod 10ᵈ)，即 x(x − 1) 同时被 2ᵈ 和 5ᵈ 整除。
x 与 x − 1 互素，所以每个素数幂只整除其中之一，于是模 10ᵈ 有四个余数：0、1 和两个混合的。
混合余数就是两个无限长的 10 进数 …890625 和 …109376 的末 d 位。
除最后一位外，它们每一位上的数字之和都是 9，因为这两个数之和是 1 (mod 10ᵈ)。

所以对每个长度 d，候选是 1（仅当 d = 1）以及两个长为 d 的结尾，结尾的最高位（即无限数的第 d 位）不为 0 时才算。
把以 5 结尾的数写成 x = Σ xᵢ 10ⁱ，x² 的第 d 位是 i + j = d 的所有 xᵢ·xⱼ 之和加上低位的进位。
新数字 c 在这个和中以 2·5·c 的形式出现，是 10 的倍数，所以 c 必须等于（其余乘积 + 进位）mod 10，下一个进位随之确定。
以 6 结尾的数在该位上是 9 − c，c ≠ 9 时才算。共 `O(n²)` 次数字乘法，不需要高精度。

注意事项：

- 1 算在内（1² = 1），但 0 不是正数；
- 有前导零的结尾，比如 d = 4 时的 0625，不算（测试 04）；
- 两个无限数是相关的：一个等于 1 减去另一个，所以同一位数字同时决定两者。

对所有检验过的 n（直到 2000），答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1698_number_theory.cpp](1698_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n²) | AC | 0.015 s | 204 KB |
| [1698_number_theory.go](1698_number_theory.go) | Go 1.14 x64 | number_theory | O(n²) | AC | 0.031 s | 1168 KB |
| [1698_number_theory.java](1698_number_theory.java) | Java 1.8 | number_theory | O(n²) | AC | 0.125 s | 1600 KB |
| [1698_number_theory.py](1698_number_theory.py) | Python 3.12 x64 | number_theory | O(n²) | AC | 0.296 s | 436 KB |
| [1698_number_theory.rs](1698_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n²) | AC | 0.015 s | 236 KB |
