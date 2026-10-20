# 2174. 把纸币两两配对使每对之和为质数

[Timus 2174](https://acm.timus.ru/problem.aspx?space=1&num=2174) · 难度 885 · matching

原题作者 Ignat Nigmatullin，出自 2023 年乌拉尔程序设计团体竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把 N 张纸币（N 为偶数）分成若干对，使每对两张面值之和为质数，或者报告无法做到。任何合法的配对都可接受。时间限制 1 秒，内存限制 256 MB。

## 输入

N（2 ≤ N ≤ 500），然后是各面值（1 ≤ cᵢ ≤ 10⁶）。

## 输出

NO，或者 YES 以及 N / 2 对。

## 评测方式

检查器核对结论，并验证这些对恰好用上了给定的纸币且和均为质数。

## 样例

### 样例 1

输入：

```
8
6 2 4 5 2 3 1 5
```

输出：

```
YES
5 2
3 2
5 6
1 4
```

### 样例 2

输入：

```
2
1 3
```

输出：

```
NO
```

## 解法

唯一的偶质数是 2 = 1 + 1，所以其他每一对都必须由一张奇数面值和一张偶数面值组成。设 O 为奇数面值纸币数（包括 1），E 为偶数面值纸币数。两张 1 组成的对每次拿走两张奇数纸币，所以恰好需要 (O − E) / 2 对；如果这个数为负，或者需要的 1 比现有的多，答案为 NO。各张 1 都一样，所以哪些 1 配在一起无关紧要。

剩下数量相等的奇数和偶数纸币构成一个二分图，和为质数时连边，质数由筛到 2 · 10⁶ 的筛法得到。用 Kuhn 增广路算法在 O(N³) 内找到的完美匹配就是答案；若不存在则答案为 NO。

第二个样例中 1 + 3 = 4 不是质数，而两张奇数纸币没有别的配法。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2174_matching.cpp](2174_matching.cpp) | G++ 13.2 x64 | matching | O(N^3 + C log log C) | AC | 0.015 s | 1752 KB |
| [2174_matching.go](2174_matching.go) | Go 1.14 x64 | matching | O(N^3 + C log log C) | AC | 0.031 s | 3248 KB |
| [2174_matching.java](2174_matching.java) | Java 1.8 | matching | O(N^3 + C log log C) | AC | 0.109 s | 2904 KB |
| [2174_matching.py](2174_matching.py) | Python 3.12 x64 | matching | O(N^3 + C log log C) | AC | 0.109 s | 4620 KB |
| [2174_matching.rs](2174_matching.rs) | Rust 1.75 x64 | matching | O(N^3 + C log log C) | AC | 0.046 s | 2116 KB |
