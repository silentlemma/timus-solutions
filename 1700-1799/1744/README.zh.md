# 1744. 上尉的连队

[Timus 1744](https://acm.timus.ru/problem.aspx?space=1&num=1744) · 难度 1983 · constructive

原题作者 Artyom Ripatti，出自 2009 年 8 月彼得罗扎沃茨克夏季集训的乌法国立航空技术大学专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每天 n 名士兵中有三人值夜班，任何两人一起值班不得超过三次。为尽可能多的天数排出值班表。

## 输入

奇数 n（3 ≤ n ≤ 99）。

## 输出

最大天数 k 以及每天的三名士兵。任何 k 天的值班表都可以。

## 样例

### 样例 1

输入：

```
3
```

输出：

```
3
1 2 3
2 3 1
3 1 2
```

### 样例 2

输入：

```
5
```

输出：

```
10
1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5
2 3 4
2 3 5
2 4 5
3 4 5
```

## 解法

每天让三对士兵在一起，而 n(n − 1)/2 对中的每一对最多可以一起三次，所以天数至多为 n(n − 1)/2。
这个上界可以达到：把士兵编号为 0 … n − 1，对每个 i 和每个 1 到 (n − 1)/2 的 d，取三元组 i, i + d, i + 2d（模 n）。

编号相差 δ 的两名士兵，作为三元组中相邻的两人相遇两次——在 δ = ±d 的那个 d 对应的三元组的前两个或后两个位置上——
并作为三元组的两端相遇一次——在 δ = ±2d 的那个 d 里。由于 n 是奇数，每个 δ 恰好对应一个第一类的 d，
又因为模 n 可以除以 2，也恰好对应一个第二类的 d，所以每对恰好相遇三次。三元组中的三人互不相同，因为 d 和 2d 都不是 n 的倍数。`O(n²)`。

当 n = 3 时得到样例 1：d = 1 以及 1, 2, 3 的三个轮换。

注意事项：

- 同样的三人可以在多天值班；
- 一天内士兵的顺序无关紧要。

检查程序验证天数、士兵编号和每对相遇的次数；对 3 到 99 的所有奇数 n 都检查过值班表。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1744_constructive.cpp](1744_constructive.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 380 KB |
| [1744_constructive.go](1744_constructive.go) | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1228 KB |
| [1744_constructive.java](1744_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.125 s | 2028 KB |
| [1744_constructive.py](1744_constructive.py) | Python 3.12 x64 | constructive | O(n²) | AC | 0.078 s | 836 KB |
| [1744_constructive.rs](1744_constructive.rs) | Rust 1.75 x64 | constructive | O(n²) | AC | 0.015 s | 320 KB |
