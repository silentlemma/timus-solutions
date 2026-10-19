# 1910. 和最大的连续三项

[Timus 1910](https://acm.timus.ru/problem.aspx?space=1&num=1910) · difficulty 34 · two_pointers

原题作者 Denis Dublennykh，比赛 NEERC 2012, Eastern subregional contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定正数序列，找出和最大的连续三个元素。输出该和以及中间元素从一开始
的下标。保证取得最大和的三元组唯一。时间限制 1 秒，内存限制 64 MB。

## 输入

先给 n，3≤n≤1000，再给 n 个整数 aᵢ，1≤aᵢ≤10⁶。
空格或换行均可作为分隔符。

## 输出

最大和，以及中间元素从一开始的下标。

## 评测方式

两个精确整数，按标记比较。

## 样例

```
6
1 4 4 4 1 1
```

```
12 3
```

## 解法

维护长度为三的滑动窗口。初始和为前三项之和，中间下标为 2。将从零开始
的窗口起点从 s−1 移到 s 时，减去 a[s−1]，加上 a[s+2]。若新和大于
当前最优值，就保存该和及新的中间位置 s+2。

每次更新都保持当前和恰好等于当前三元组之和。最优值初始对应第一个窗口，
每次比较后都等于已检查窗口中的最大和。所有起点 0,…,n−3 都恰好检查一次，
所以最终和最优，保存的位置属于唯一最优三元组。

n=3 时只有初始窗口，更新循环为空。必须输出中间位置，不能输出窗口的
开头或结尾。示例中第 2、3、4 项之和为 12，中间元素位置为 3。

时间复杂度 O(n)，输入数组占 O(n) 空间，额外状态为 O(1)。三项和至多
3·10⁶，适合有符号 32 位整数。

## 各语言说明

C++、Go 1.14、Java 8、Rust 1.75 使用整数数组或向量。Python 3.12 读取
整数标记并执行相同滚动更新。无需浮点数或大整数。只有更大的和才更新答案；
输入保证不存在并列最大值。

在全部 14 157 个长度为 3 到 7、取值 1 到 4 且最优三元组唯一的序列上，答案与直接对所有三元组求和的结果一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1910_two_pointers.cpp](1910_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n) | AC | 0.015 s | 432 KB |
| [1910_two_pointers.go](1910_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n) | AC | 0.015 s | 1096 KB |
| [1910_two_pointers.java](1910_two_pointers.java) | Java 1.8 | two_pointers | O(n) | AC | 0.125 s | 2376 KB |
| [1910_two_pointers.py](1910_two_pointers.py) | Python 3.12 x64 | two_pointers | O(n) | AC | 0.078 s | 496 KB |
| [1910_two_pointers.rs](1910_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n) | AC | 0.015 s | 240 KB |
