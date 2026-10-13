# 1476. 月球码

[Timus 1476](https://acm.timus.ru/problem.aspx?space=1&num=1476) · 难度 1263 · dp

原题作者 Alexander Ipatov（创意来自 Alexander Toropov），出自 2006 年 8 月彼得罗扎沃茨克夏季集训的乌拉尔国立大学与奥廖尔国立技术大学比赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计由 0 和 1 组成的 M × N 矩阵（1 ≤ M, N ≤ 40）的个数，要求对每一对相邻的列 i
与 i + 1，至多 K 行（0 ≤ K ≤ M）在第 i 列为 0 而在第 i + 1 列为 1。

时间限制：1 秒。内存限制：64 MB。

## 输入

M、N 和 K。

## 输出

满足条件的矩阵个数。

## 样例

### 样例 1

输入:

```
2 1 0
```

输出:

```
4
```

### 样例 2

输入:

```
2 2 1
```

输出:

```
15
```

## 解法

逐列填写矩阵。下一列是否允许取决于当前列哪些行是 0，但继续填写的方法数只取决于
该列有多少个 1。从有 c 个 1 的列出发，把 M − c 个 0 中的 t ≤ K 个变成 1、保留 c
个 1 中的 s = d − t 个，就得到有 d 个 1 的下一列：
step(c, d) = Σ C(M − c, t)·C(c, d − t)，对 t ≤ K 求和。这些数不超过 2⁴⁰。有 c
个 1 的第一列有 C(M, c) 种选法；之后每一列都把计数向量乘以 step 表，N 列之后求
和即为答案。对至多 M·N 位的数做 `O(N·M²)` 次运算。

注意事项：

- K = M 时所有矩阵都符合，2¹⁶⁰⁰ 需要大整数（测试 03）；
- 只有一行且 K = 0 时，这一行永远不能从 0 变成 1：共 N + 1 个矩阵（测试 05）；
- 只有一列时没有需要检查的列对：共 2^M 个矩阵（测试 01、06）。

## 语言说明

- C++ 和 Rust 以 10⁹ 为基数分段存储计数，并用 128 位运算把它们乘以 64 位的 step
  值，这里需要的大数运算仅此而已。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1476_dp.cpp](1476_dp.cpp) | G++ 13.2 x64 | dp | O(N M^2) big-number operations | AC | 0.031 s | 492 KB |
| [1476_dp.go](1476_dp.go) | Go 1.14 x64 | dp | O(N M^2) big-number operations | AC | 0.046 s | 2104 KB |
| [1476_dp.java](1476_dp.java) | Java 1.8 | dp | O(N M^2) big-number operations | AC | 0.125 s | 6228 KB |
| [1476_dp.py](1476_dp.py) | Python 3.12 x64 | dp | O(N M^2) big-number operations | AC | 0.093 s | 540 KB |
| [1476_dp.rs](1476_dp.rs) | Rust 1.75 x64 | dp | O(N M^2) big-number operations | AC | 0.031 s | 516 KB |
