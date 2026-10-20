# 2145. 统计每个学生都能解出所分题目的分配方式

[Timus 2145](https://acm.timus.ru/problem.aspx?space=1&num=2145) · 难度 375 · combinatorics, sorting

原题作者 Valentin Zuev，出自 2019 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 名学生的知识水平为 aᵢ，n 道题的难度为 bⱼ；当 aᵢ ≥ bⱼ 时学生能解出该题。求给每名学生恰好分一道互不相同的题、使每人都能解出自己那道题的方式数，对 p 取模。时间限制 3 秒，内存限制 256 MB。

## 输入

n（1 ≤ n ≤ 10⁵），数值 aᵢ，数值 bⱼ，都在 0 到 10⁹ 之间，以及 p（1 ≤ p ≤ 10⁹）。

## 输出

方式数对 p 取模。

## 样例

### 样例 1

输入：

```
3
1 2 3
1 2 3
100
```

输出：

```
1
```

### 样例 2

输入：

```
3
3 3 3
1 1 1
100
```

输出：

```
6
```

## 解法

把学生按知识水平排序，从最弱的学生开始分题。设 cᵢ 为第 i 名学生（从 0 开始计数）能解的题数。更弱的学生能解的题，第 i 名学生也都能解，而 i 名更弱的学生已经从第 i 名学生的 cᵢ 道题中拿走了 i 道不同的题。不论他们拿走了哪些，第 i 名学生恰好有 cᵢ − i 种选择，所以答案是各个 cᵢ − i 的乘积。一旦某个因子为 0，乘积就一直是 0。

两个数组都排序后，cᵢ 随 i 增大，用一个指针扫描题目即可得到全部 cᵢ。每一步都对 p 取模，1 % p 处理了 p = 1 的情况。工作量 O(n log n)。

第二个样例中每名学生都能解每道题，乘积为 3 · 2 · 1 = 6。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2145_combinatorics_sorting.cpp](2145_combinatorics_sorting.cpp) | G++ 13.2 x64 | combinatorics, sorting | O(n log n) | AC | 0.171 s | 1768 KB |
| [2145_combinatorics_sorting.go](2145_combinatorics_sorting.go) | Go 1.14 x64 | combinatorics, sorting | O(n log n) | AC | 0.203 s | 5672 KB |
| [2145_combinatorics_sorting.java](2145_combinatorics_sorting.java) | Java 1.8 | combinatorics, sorting | O(n log n) | AC | 0.156 s | 2156 KB |
| [2145_combinatorics_sorting.py](2145_combinatorics_sorting.py) | Python 3.12 x64 | combinatorics, sorting | O(n log n) | AC | 0.187 s | 21384 KB |
| [2145_combinatorics_sorting.rs](2145_combinatorics_sorting.rs) | Rust 1.75 x64 | combinatorics, sorting | O(n log n) | AC | 0.031 s | 6320 KB |
