# 1295. 胡思乱想

[Timus 1295](https://acm.timus.ru/problem.aspx?space=1&num=1295) · 难度 151 · number_theory

原题作者 Den Raskovalov，出自 2004 年 3 月 13 日第九届中学生公开团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

当 1 ≤ n ≤ 300 000 时，十进制数 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ 末尾有几个零？

时间限制：1 秒。内存限制：64 MB。

## 输入

数 n。

## 输出

末尾零的个数。

## 样例

### 样例 1

输入：

```
1
```

输出：

```
1
```

### 样例 2

输入：

```
3
```

输出：

```
2
```

## 解法

n 最大时这个和超过 180 000 位，但末尾零的个数受其中 2 的幂次限制。设 S = 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ。

- n = 1：S = 10，一个零。
- n 为偶数：1ⁿ + 3ⁿ ≡ 1 + 1 = 2 (mod 4)，而 2ⁿ、4ⁿ 是 4 的倍数，所以 S 能被 2 整除但不能被 4
  整除。
- n 为奇数且 n ≥ 3：3ⁿ ≡ 3 (mod 8)，所以 1ⁿ + 3ⁿ ≡ 4 (mod 8)，而 2ⁿ 和 4ⁿ 是 8 的倍数；S 能被
  4 整除但不能被 8 整除。

因此 S 末尾不会有三个零，一切由 S mod 100 决定：为 0 时两个零，末位为 0 时一个零，否则没有。
四个幂模 100 的值用快速幂求出。`O(log n)`。

实际上答案只取决于 n mod 20：n 被 4 整除时为 0，n 模 4 余 3 或模 20 余 5 时为 2，其余为 1。
解法直接计算，而不依赖这张表。

注意事项：

- n 模 4 余 1 时通常只有一个零，但 n = 5、25、… 有两个（测试 05 和 06）；
- 完整的和可以用高精度构造，但完全没有必要：只有最后两位重要。

对 3000 以内的每个 n，结果都与高精度精确和比较过。

## 各语言说明

- Python 使用内置的三参数 `pow`；其他语言手工做模 100 的快速幂。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1295_number_theory.cpp](1295_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log n) | AC | 0.015 s | 128 KB |
| [1295_number_theory.go](1295_number_theory.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 1080 KB |
| [1295_number_theory.java](1295_number_theory.java) | Java 1.8 | number_theory | O(log n) | AC | 0.125 s | 1600 KB |
| [1295_number_theory.py](1295_number_theory.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.093 s | 464 KB |
| [1295_number_theory.rs](1295_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log n) | AC | 0.046 s | 240 KB |
