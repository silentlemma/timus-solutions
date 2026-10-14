# 1581. 团队合作

[Timus 1581](https://acm.timus.ru/problem.aspx?space=1&num=1581) · 难度 41 · implementation

原题作者 Alex Samsonov，出自 2007 年 10 月第十四届斯维尔德洛夫斯克州中学生团体程序设计公开赛（USU Junior Contest）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个由 N ≤ 1000 个 1 到 10 之间的数组成的序列按“段”口述：对每一段相等的数，先说有几个，再说是哪个数。输出口述
出来的数。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是 N 个数。

## 输出

各段的长度和值，按顺序在一行中输出。

## 样例

### 样例 1

输入:

```
8
1 1 2 3 3 3 10 10
```

输出:

```
2 1 1 2 3 3 2 10
```

## 解法

遍历这些数，把它们切成相等值的极大段；对每一段输出其长度，再输出其值。`O(N)`。

注意事项：

- 一段可能就是整个序列，长达 1000（测试 05）；
- 不相邻的相等数属于不同的段（测试 04）；
- 10 是一个数，所以要按数读入，而不是按字符。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1581_implementation.cpp](1581_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB |
| [1581_implementation.go](1581_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.031 s | 1268 KB |
| [1581_implementation.java](1581_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.125 s | 2404 KB |
| [1581_implementation.py](1581_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.078 s | 404 KB |
| [1581_implementation.rs](1581_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 328 KB |
