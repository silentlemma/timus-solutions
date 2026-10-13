# 1407. 一二，一二

[Timus 1407](https://acm.timus.ru/problem.aspx?space=1&num=1407) · 难度 388 · constructive

原题作者 Sergey Pupyrev，出自 2005 年 10 月 15 日第十二届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对 1 ≤ N ≤ 100，输出一个至多 10 000 位、只由数字 1 和 2 组成且能被 2ᴺ 整除的数，
若不存在则输出 "No solution"。

时间限制：1 秒。内存限制：64 MB。

## 输入

数 N。

## 输出

这样一个数；任何一个都被接受。

## 样例

### 样例 1

输入:

```
2
```

输出:

```
12
```

## 解法

总存在恰好 N 位的这样的数，从右往左构造。设 aₖ 由 k 位 1 和 2 组成且能被 2ᵏ
整除；在前面添上数字 d：d·10ᵏ + aₖ = 2ᵏ·(d·5ᵏ + aₖ / 2ᵏ)。由于 5ᵏ 是奇数，
d = 1 和 d = 2 中恰有一个使括号内为偶数，于是 aₖ₊₁ 能被 2ᵏ⁺¹ 整除。从空数开
始重复 N 次。Go/Java 为 `O(N²)`，Python 为 `O(N³)`。

选择只取决于最低的 N + 1 位，所以 C++ 和 Rust 用 128 位保存这个数并允许求和
溢出回绕；Go 和 Java 用大整数并查看最低的置位。

注意事项：

- 答案永远不会是 "No solution"；
- 2¹⁰⁰ 远超 64 位（测试 07 到 09）。

检查了从 1 到 100 的每个 N：得到的数由 N 位 1 和 2 组成且能被 2ᴺ 整除。由于
N 位的答案唯一，测试按精确比较判定。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1407_constructive.cpp](1407_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 188 KB |
| [1407_constructive.go](1407_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.015 s | 1140 KB |
| [1407_constructive.java](1407_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.109 s | 1668 KB |
| [1407_constructive.py](1407_constructive.py) | Python 3.12 x64 | constructive | O(N^3) | AC | 0.078 s | 416 KB |
| [1407_constructive.rs](1407_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 216 KB |
