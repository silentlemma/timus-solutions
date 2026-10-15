# 1690. 法师军团

[Timus 1690](https://acm.timus.ru/problem.aspx?space=1&num=1690) · 难度 637 · constructive

原题作者 Eugene Kurpilyanskiy，出自 2009 年 2 月彼得罗扎沃茨克冬季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 5n 名候选人住在互不相同的整点上。若两人住所之间的线段经过另一个整点，两位法师就互相尊重。
选出 n 名两两互相尊重的候选人，或报告无法做到。

## 输入

n（1 ≤ n ≤ 5000），然后是 5n 个住所，坐标为绝对值不超过 10000 的整数。

## 输出

OK 和所选候选人的编号，或 IMPOSSIBLE。任何合法的军团都可以。

## 样例

### 样例 1

输入：

```
2
1 1
5 5
0 0
2 2
0 10
6 6
7 7
8 8
9 9
10 10
```

输出：

```
OK
2 1
```

## 解法

从 (x1, y1) 到 (x2, y2) 的线段内部有整点，当且仅当 gcd(|x1 − x2|, |y1 − y2|) ≥ 2。
特别地，x 与 y 奇偶性都相同的两个住所坐标差都是偶数，所以线段中点是整点。

奇偶类只有四个，5n 个住所分到四类中，必有一类至少有 ⌈5n / 4⌉ ≥ n 个。
所以答案总是 OK：从最大的类中任取 n 个即可。`O(n)`。

注意事项：

- 永远不会出现 IMPOSSIBLE；
- 负坐标的奇偶性必须得到 0 或 1：−3 是奇数，补码下 `x & 1` 能正确处理，而在类 C 语言中 `x % 2` 会得到 −1（测试 03）。

检查器接受任意 n 名互不相同、两两尊重的候选人：若不在同一奇偶类则逐对检查。一个独立的已通过实现给出的答案也能通过。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1690_constructive.cpp](1690_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.046 s | 304 KB |
| [1690_constructive.go](1690_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.062 s | 4412 KB |
| [1690_constructive.java](1690_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.140 s | 1840 KB |
| [1690_constructive.py](1690_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.093 s | 6088 KB |
| [1690_constructive.rs](1690_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 2120 KB |
