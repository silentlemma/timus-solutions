# 2150. 把稠密的友谊图分成两人组和三人组

[Timus 2150](https://acm.timus.ru/problem.aspx?space=1&num=2150) · 难度 1139 · greedy, matching

原题作者 Semyon Trifochkin，出自 2020 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 个学生中每人至少与 ⌈n / 2⌉ 个其他人是朋友，要把他们分成两人或三人一组，组内人人互相认识。输出一种分法或 NO。任何合法的分法都可接受。时间限制 1 秒，内存限制 256 MB。

## 输入

n（2 ≤ n ≤ 1000），然后是对称的朋友关系矩阵。

## 输出

NO，或者 YES、组数以及每组的大小和成员。

## 评测方式

检查器验证各组恰好覆盖每个学生一次，并且组内成员都是朋友。

## 样例

### 样例 1

输入：

```
2
0 1
1 0
```

输出：

```
YES
1
2 1 2
```

### 样例 2

输入：

```
5
0 1 0 1 1
1 0 1 0 1
0 1 0 1 1
1 0 1 0 1
1 1 1 1 0
```

输出：

```
YES
2
3 1 2 5
2 3 4
```

## 解法

答案总是 YES：存在近似完美匹配，n 为奇数时多出的一个学生可以加入其中一对。

先贪心求一个极大匹配。未匹配的学生两两不是朋友，否则贪心就会把他们配上，所以他们的朋友都已被匹配。对两个未匹配的学生 u 和 v，一定存在一对 (a, b)，使 u 与 a、v 与 b 是朋友，或者反过来：否则每一对至多得到来自 u 和 v 的两条边，总共至多 n − 2 条，而 u 和 v 合起来至少有 n 个朋友。把 (a, b) 换成 (u, a) 和 (v, b) 就多出一对，所以未匹配的学生每次两个地解决。

若 n 为奇数，还剩一个学生 w。w 至少有 ⌈n / 2⌉ 个朋友，多于 (n − 1) / 2 对，所以某一对的两人都是 w 的朋友，这一对与 w 组成三人组。每解决一个学生就扫描一遍各对，总共 O(n²)。

第二个样例中学生 5 认识所有人，所以对 (1, 2) 把学生 5 作为第三人，(3, 4) 保持为一对。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2150_greedy_matching.cpp](2150_greedy_matching.cpp) | G++ 13.2 x64 | greedy, matching | O(n^2) | AC | 0.031 s | 540 KB |
| [2150_greedy_matching.go](2150_greedy_matching.go) | Go 1.14 x64 | greedy, matching | O(n^2) | AC | 0.031 s | 6248 KB |
| [2150_greedy_matching.java](2150_greedy_matching.java) | Java 1.8 | greedy, matching | O(n^2) | AC | 0.156 s | 1532 KB |
| [2150_greedy_matching.py](2150_greedy_matching.py) | Python 3.12 x64 | greedy, matching | O(n^2) | AC | 0.187 s | 19168 KB |
| [2150_greedy_matching.rs](2150_greedy_matching.rs) | Rust 1.75 x64 | greedy, matching | O(n^2) | AC | 0.031 s | 3292 KB |
