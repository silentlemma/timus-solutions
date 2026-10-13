# 1428. 绝地之谜

[Timus 1428](https://acm.timus.ru/problem.aspx?space=1&num=1428) · 难度 499 · math

原题作者 Ilya Grebnov、Dmitry Kovalioff 与 Nikita Rybak，出自 Timus Top Coders: First Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给出 A、B、C（1 ≤ A, B, C ≤ 32），且 C − 1 能被 A 和 B 整除。求 1 到 10⁵⁰ 之间的
整数 X、Y、Z，使 X^A + Y^B = Z^C。任何这样的三元组都可以。

时间限制：1 秒。内存限制：64 MB。

## 输入

A、B 和 C。

## 输出

X、Y 和 Z，每行一个。

## 样例

### 样例 1

输入:

```
2 2 3
```

输出:

```
10
5
5
```

## 解法

两个相等的一半合成一个整体：2^(C−1) + 2^(C−1) = 2^C。因为 A 和 B 整除 C − 1，取
X = 2^((C−1)/A)、Y = 2^((C−1)/B)，于是 X^A = Y^B = 2^(C−1)，再取 Z = 2。这些数不
超过 2³¹，远小于 10⁵⁰，放得进 64 位整数。`O(1)`。

注意事项：

- C = 1 时 X = Y = 1，且 1 + 1 = 2¹（测试 03、08）；
- 样例输出的是另一组三元组，所以测试使用带大整数的检查器（测试 01）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1428_math.cpp](1428_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1428_math.go](1428_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1064 KB |
| [1428_math.java](1428_math.java) | Java 1.8 | math | O(1) | AC | 0.156 s | 1600 KB |
| [1428_math.py](1428_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 408 KB |
| [1428_math.rs](1428_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 208 KB |
