# 2135. 乘积落在区间内的最少分段数

[Timus 2135](https://acm.timus.ru/problem.aspx?space=1&num=2135) · 难度 991 · dp, two_pointers

原题作者 Anna Khanova，出自 “迟到总比不到好”专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把 n 个正整数组成的序列切成尽可能少的连续段，使每段的乘积都在 [l, r] 中，或者报告无法做到。时间限制 2 秒，内存限制 256 MB。

## 输入

n、l 和 r（1 ≤ n ≤ 50 000，1 ≤ l ≤ r ≤ 10¹⁸），然后是这些数，每个在 1 到 10⁹ 之间。

## 输出

最少段数，或者 −1。

## 样例

### 样例 1

输入：

```
7 8 20
2 4 8 16 1 3 5
```

输出：

```
4
```

### 样例 2

输入：

```
7 10 20
2 4 8 16 1 3 5
```

输出：

```
-1
```

## 解法

设 best(i) 为覆盖前 i 个数所需的最少段数。前 i 个数的划分中最后一段从某个 j 开始，j 向左移动时它的乘积增大，因为所有数都至少为 1。所以乘积不超过 r 的起点构成从 U 开始的后缀，乘积至少为 l 的起点构成 L 之前的前缀；允许的起点是区间 [U, L)。

随着 i 增大两个端点都只向右移动，所以用两个指针维护，各自带着窗口的乘积：当下一个数会使乘积超出界限时，先从左边除掉若干个数，这样每个乘积都保持在 64 位之内。大于 r 的数重置上窗口，不小于 l 的数重置下窗口。j ∈ [U, L) 的 best(j) 值进出一个单调双端队列，O(1) 给出最小值，于是 best(i) = 1 + 这个最小值。整个过程 O(n)。

第一个样例中 2 · 4 | 8 | 16 · 1 | 3 · 5 用了四段，乘积分别为 8、8、16 和 15。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2135_dp_two_pointers.cpp](2135_dp_two_pointers.cpp) | G++ 13.2 x64 | dp, two_pointers | O(n) | AC | 0.015 s | 836 KB |
| [2135_dp_two_pointers.go](2135_dp_two_pointers.go) | Go 1.14 x64 | dp, two_pointers | O(n) | AC | 0.046 s | 3016 KB |
| [2135_dp_two_pointers.java](2135_dp_two_pointers.java) | Java 1.8 | dp, two_pointers | O(n) | AC | 0.093 s | 1344 KB |
| [2135_dp_two_pointers.py](2135_dp_two_pointers.py) | Python 3.12 x64 | dp, two_pointers | O(n) | AC | 0.156 s | 5472 KB |
| [2135_dp_two_pointers.rs](2135_dp_two_pointers.rs) | Rust 1.75 x64 | dp, two_pointers | O(n) | AC | 0.031 s | 1940 KB |
