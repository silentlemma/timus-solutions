# 1857. 爱丽丝与潘达斯奈基

[Timus 1857](https://acm.timus.ru/problem.aspx?space=1&num=1857) · 难度 1350 · combinatorics

原题作者 Pavel Klimov，出自 2011 年 8 月彼得罗扎沃茨克夏季集训的 Ural SU Team.GOV Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

爱丽丝的密钥是一个由 0 到 a − 1 的数组成的序列 x₁, …, xₙ，其中 a 是字母表的大小；密钥被反复作用在消息的字母上。只差一个循环移位的密钥算作同一个，而重复某个更短块（周期小于 n）的密钥不使用。求不同密钥的数目。

## 输入

a 和 n（1 ≤ a ≤ 26，1 ≤ n ≤ 10 000）。

## 输出

密钥的确切数目。

## 样例

### 样例 1

输入：

```
3 4
```

输出：

```
18
```

### 样例 2

输入：

```
10 2
```

输出：

```
45
```

## 解法

这些密钥就是 a 个字母上周期恰为 n 的长度为 n 的项链，即 Lyndon 词。每个长度为 n 的词都在重复一个长度 d 整除 n 的本原块，所以 aⁿ = Σ_{d | n} d·L(d)，其中 L(d) 是长度为 d 的 Lyndon 词的个数（每个给出 d 个不同的旋转）。
Möbius 反演把它变为 n·L(n) = Σ_{d | n} μ(d)·a^(n/d)，其中只有无平方因子的 d 才计入，符号为 (−1) 的质因子个数次方。

不超过 10 000 的数最多有五个不同的质因子，所以最多 32 项，但 a^(n/d) 最多有 14 150 位。Python、Go 和 Java 使用自带的大整数；C++ 和 Rust 版本用 10⁹ 进制保存数字，只需要乘以 a、加法、减法以及除以 n：正项与负项分别求和，最后相减一次。
每一项通过逐次乘以 a 构造，总共约 2n 次乘法，每个数最多 1600 个基数位。

在第一个样例中，长度为 4 的 81 个密钥里有 9 个周期为 2 或 1，其余 72 个按旋转每 4 个一类：共 18 类。

注意事项：

- 只有一个字母时，任何长度大于 1 的密钥都在重复自身：答案为 0，而 n = 1 时为 1；
- 答案是精确的长整数；Python 3.12 需要解除打印长整数的默认限制。

对较小的 a 和 n，答案与枚举所有密钥的计数一致；在长度不超过 10 000 的数据上，与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1857_combinatorics.cpp](1857_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n^2) | AC | 0.031 s | 228 KB |
| [1857_combinatorics.go](1857_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n^2) | AC | 0.031 s | 1464 KB |
| [1857_combinatorics.java](1857_combinatorics.java) | Java 1.8 | combinatorics | O(n^2) | AC | 0.140 s | 3932 KB |
| [1857_combinatorics.py](1857_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n^2) | AC | 0.093 s | 840 KB |
| [1857_combinatorics.rs](1857_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n^2) | AC | 0.062 s | 260 KB |
