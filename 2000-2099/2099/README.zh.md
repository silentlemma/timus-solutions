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

所有判断都用整数精确进行。混合积可达约 5·10¹⁹，超出 64 位，所以 C++ 和 Rust 用 128 位整数，Go 和 Java 用大整数计算它。

样例中第一条直线是 x 轴，第二条是 y 轴，在 B = (−1, 0, 0) 之后于原点转弯，C = (0, 1, 0) 在其后：Valid。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2099_geometry.cpp](2099_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 128 KB |
| [2099_geometry.go](2099_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1160 KB |
| [2099_geometry.java](2099_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1720 KB |
| [2099_geometry.py](2099_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 548 KB |
| [2099_geometry.rs](2099_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 240 KB |
