# 1675. 月球码 2

[Timus 1675](https://acm.timus.ru/problem.aspx?space=1&num=1675) · 难度 1805 · combinatorics

原题作者 Igor Chevdar，出自 2008 年 8 月彼得罗扎沃茨克夏季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计 M × N 的 0/1 矩阵中，恰有 K 行和恰有 L 列全为 0 的矩阵个数，对 10⁹ + 7 取模。

## 输入

M、N、K、L（1 ≤ M, N ≤ 100000；0 ≤ K ≤ M；0 ≤ L ≤ N）。

## 输出

个数对 10⁹ + 7 取模。

## 样例

### 样例 1

输入：

```
2 2 0 0
```

输出：

```
7
```

### 样例 2

输入：

```
2 3 1 1
```

输出：

```
6
```

## 解法

先选出哪 K 行、哪 L 列全为 0，共 C(M, K) · C(N, L) 种。于是所有的 1 都在剩下的 a × b 块中（a = M − K，
b = N − L），并且这个块的每一行、每一列都必须含有 1。

没有全零行和全零列的 a × b 矩阵用对必须为零的列做容斥来计数：若指定的 j 列为零，a 行中每一行都是其余列上
2^(b − j) − 1 种非零模式之一，所以

f(a, b) = Σⱼ (−1)ʲ C(b, j) (2^(b − j) − 1)^a。

该式关于 a、b 对称，所以沿较短的一边求和。预处理到 max(M, N) 的阶乘及其逆元得到组合数。
`O(max(M, N) + min(a, b) log max(a, b))`。

易错点：

- 如果所有行都为零，那么所有列也为零：K = M 要求 L = N（测试 06 和 07）；公式自动处理这一点，因为 a = 0 时和式为
  Σ (−1)ʲ C(b, j)，b = 0 时为 1，否则为 0；
- 和式中 0⁰ 取 1。

在所有不超过 4 × 4 的矩阵及所有 K、L 上，答案与穷举计数一致，也与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1675_combinatorics.cpp](1675_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.015 s | 1760 KB |
| [1675_combinatorics.go](1675_combinatorics.go) | Go 1.14 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.031 s | 2696 KB |
| [1675_combinatorics.java](1675_combinatorics.java) | Java 1.8 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.218 s | 3132 KB |
| [1675_combinatorics.py](1675_combinatorics.py) | Python 3.12 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.500 s | 8372 KB |
| [1675_combinatorics.rs](1675_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.031 s | 1792 KB |
