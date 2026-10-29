# 1880. Psych Up 的特征值

[Timus 1880](https://acm.timus.ru/problem.aspx?space=1&num=1880) · 难度 30 · two_pointers, hashing

原题作者 Denis Mukhametianov，出自 2011 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一支队伍的三名队员各有一份"自己的"数的列表。一个数如果出现在全部三份列表中，就是队伍自己的数。这样的数有多少个？

## 输入

三个块：列表长度 n（1 ≤ n ≤ 4000），然后是它的 n 个互不相同、不超过 10⁹ 的正整数，按递增顺序给出。

## 输出

出现在全部三份列表中的数的个数。

## 样例

### 样例 1

输入：

```
5
13 20 22 43 146
4
13 22 43 146
5
13 43 67 89 146
```

输出：

```
3
```

## 解法

列表已排好序，所以给每份列表一个指针，同时向前走。如果三个当前数相等，计数加一。然后移动所有指向其中最小数的指针；任何一份列表走完就停止。Python 解法改为求三个集合的交集。`O(n)`。

样例中 13、43 和 146 在三份列表中都有，而 20、22、67、89 至少在一份中缺失。

注意事项：

- 只在两份列表中出现的数不算；
- 匹配后三个指针都移动，否则只移动指向最小值的指针，不然可能跳过公共数；
- 只要有一份列表走完，遍历就停止。

在 50 支随机队伍上，计数与一个独立的已通过实现一致。

## 优化解法

优化解法（C++、Rust）只保存一个列表。它们先保存第一个列表，然后在读取后面每个列
表的同时与之求交，用一个指针在已保存的数中移动；公共的数写回同一个数组的开头，写
入位置永远不会超过指针。数字用手工解析：C++ 用 `getchar`，Rust 从 1 KB 的缓冲区
读取。时间不变，C++ 为 108 KB，而不是 240 KB；Rust 为 228 KB，而不是 500 KB。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1880_hashing.py](1880_hashing.py) | Python 3.12 x64 | hashing | O(n) | AC | 0.078 s | 1860 KB | 11291026 |
| [1880_two_pointers.cpp](1880_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n) | AC | 0.015 s | 240 KB | 11303522 |
| [1880_two_pointers.go](1880_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n) | AC | 0.046 s | 1364 KB | 11291024 |
| [1880_two_pointers.java](1880_two_pointers.java) | Java 1.8 | two_pointers | O(n) | AC | 0.093 s | 536 KB | 11303524 |
| [1880_two_pointers.rs](1880_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n) | AC | 0.046 s | 500 KB | 11303525 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1880_two_pointers_optimized.cpp](1880_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(n) | AC | 0.015 s | 108 KB | 11303644 |
| [1880_two_pointers_optimized.rs](1880_two_pointers_optimized.rs) | Rust 1.75 x64 | two_pointers | O(n) | AC | 0.031 s | 228 KB | 11303645 |
