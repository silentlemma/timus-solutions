# 1870. Zinium 2

[Timus 1870](https://acm.timus.ru/problem.aspx?space=1&num=1870) · 难度 716 · constructive

原题作者 Igor Chevdar（由 Eugene Kurpilyanskiy 准备），出自 2011 年乌拉尔联邦大学开放团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

在 n × n 的环面棋盘上（最上一行与最下一行粘合，最左一列与最右一列粘合，所以对角线会绕回来）放置 n 个皇后，使任意两个皇后互不攻击，或者说明这不可能。

## 输入

n（4 ≤ n ≤ 10⁵）。

## 输出

"Yes"，以及 x = 1, …, n 时第 x 列皇后所在的行；或者 "No"。任何合法放置均可。

## 样例

### 样例 1

输入：

```
5
```

输出：

```
Yes
2 4 1 3 5
```

### 样例 2

输入：

```
8
```

输出：

```
No
```

## 解法

行和列从 0 开始编号。在环面上，两个皇后的 x、y、x + y mod n 或 x − y mod n 之一相同时就互相攻击，所以这几个量都必须恰好取遍每个值一次。

若 n 与 6 互素，把第 i 列的皇后放在第 2i mod n 行。行 2i、和 3i 与差 −i 都两两不同，因为 2 和 3 在模 n 下可逆。

否则不存在放置。若 n 为偶数，把所有皇后的 x + y 相加。由于这些和取遍每个余数一次，总和为 n(n − 1)/2 ≡ n/2 (mod n)。但它又等于 Σx + Σy = n(n − 1) ≡ 0，矛盾。若 3 整除 n（且 n 为奇数），改为把平方相加。由于 (x + y)² + (x − y)² = 2x² + 2y²，所有余数的平方和 S 满足 S + S ≡ 2S + 2S，即 2S ≡ 0 (mod n)。而 S = (n − 1)n(2n − 1)/6，这要求 3 整除 (n − 1)(2n − 1)，但两个因子模 3 都余 2。`O(n)`。

对第一个样例，从 1 开始数的行是 1、3、5、2、4，这是另一个合法答案。

注意事项：

- 答案取决于 n 模 6，而不是 n 是否为素数：35 有放置，9 和 8 没有；
- 步长 2 是最小可行的；步长 1 会把所有皇后放在同一条对角线上；
- 输出多达 10⁵ 个数，最好一次性拼好再输出。

对 4 到 400 的每个 n 以及最大的 n，放置都通过了检查器，"No" 的判断与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1870_constructive.cpp](1870_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 1520 KB |
| [1870_constructive.go](1870_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1656 KB |
| [1870_constructive.java](1870_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.109 s | 5372 KB |
| [1870_constructive.py](1870_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.125 s | 7276 KB |
| [1870_constructive.rs](1870_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 5832 KB |
