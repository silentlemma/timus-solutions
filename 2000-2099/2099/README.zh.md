# 2099. 经过四点的一次直角转弯

[Timus 2099](https://acm.timus.ru/problem.aspx?space=1&num=2099) · 难度 574 · geometry

原题作者 Denis Dublennykh，出自 2014 年乌拉尔联邦大学公开个人赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个沿直线飞行的点能否先后经过 A 和 B，转 90°，然后沿直线先后经过 C 和 D？转弯点可以是 B 或 C。时间限制 1 秒，内存限制 64 MB。

## 输入

空间中 A、B、C、D 的整数坐标，绝对值不超过 10⁶；各点两两不同。

## 输出

`Valid` 或 `Invalid`。

## 样例

### 样例 1

输入：

```
-2 0 0
-1 0 0
0 1 0
0 2 0
```

输出：

```
Valid
```

## 解法

第一条直线为 A + t·AB，第二条过 C、方向为 CD，两条都向前飞。飞行可行当且仅当：

- AB · CD = 0，转弯为直角；
- AC · (AB × CD) = 0，两条直线共面，又互相垂直，所以交于一点 P；
- P = A + t·AB，其中 t = (AC · AB) / |AB|²（因为 CD ⊥ AB，这是第二条直线在第一条上的垂足），不在 B 之前：AC · AB ≥ |AB|²；
- 在第二条直线上 C 不在 P 之前：(C − P) · CD = AC · CD ≥ 0，因为 C − P 中沿 AB 的部分与 CD 正交。

混合积等于 AB、AC 和 AD 构成的行列式，可能相差一个符号。行列式对每个点都是仿射的，因此绝对值最大值在立方体的顶点取得，为 1.6·10¹⁹。这个数超出有符号 64 位整数的范围。简单版 C++ 和 Rust 使用 128 位整数，Go 和 Java 使用大整数。

样例中第一条直线是 x 轴，第二条是 y 轴，在 B = (−1, 0, 0) 之后于原点转弯，C = (0, 1, 0) 在其后：Valid。

## 优化解法

Java 将 AC 的每个坐标除以 65 536，分别累加商与余数的贡献。AB × CD 的每个分量的绝对值不超过 8·10¹²，因此两个和 H、L 都能用 64 位有符号整数表示。当且仅当 L 能被 65 536 整除且 H + L / 65 536 为零时，混合积为零。

Python 直接用坐标差检验各个条件。

**Timus 提交记录**

- 简单版本 · G++ 13.2 x64, №11318402 · Java 1.8, №11318403 · Python 3.12 x64, №11318407 · Rust 1.75 x64, №11318409.
- 优化版本 · Java 1.8, №11318393 · Python 3.12 x64, №11318399.

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11318402 · Java 1.8 №11318403 · Python 3.12 x64 №11318407 · Rust 1.75 x64 №11318409 · Go 1.14 x64 №11322396.

Rust 用 64 位整数计算点积，并用 128 位整数计算标量三重积。 Rust 1.75 x64（提交 11323329）的运行时间从 0.015 秒变为 0.046 秒，内存从 232 KB 变为 48 KB。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [2099_geometry.cpp](2099_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 108 KB | 11318402 |
| [2099_geometry.go](2099_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1168 KB | 11322396 |
| [2099_geometry.java](2099_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.14 s | 1672 KB | 11318403 |
| [2099_geometry.py](2099_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 520 KB | 11318407 |
| [2099_geometry.rs](2099_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 232 KB | 11318409 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [2099_geometry_optimized.java](2099_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 360 KB | 11318393 |
| [2099_geometry_optimized.py](2099_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 472 KB | 11318399 |
| [2099_geometry_optimized.rs](2099_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 48 KB | 11323329 |

\* 带星号的解法仍有提升排名的空间。
