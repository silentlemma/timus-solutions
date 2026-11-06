# 2065. 不同区间和尽量少

[Timus 2065](https://acm.timus.ru/problem.aspx?space=1&num=2065) · 难度 318 · constructive

原题作者 Nikita Sivukhin（由 Alexey Danilyuk 和 Nikita Sivukhin 整理），出自 2015 年乌拉尔地区团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

构造一个含 n 个整数、至少有 k 个不同值的数组，使其所有连续区间的和中不同值的个数尽可能少。所有数的绝对值不超过 10⁶。时间限制 1 秒，内存限制 64 MB。

## 输入

两个整数 n 和 k，1 ≤ k ≤ n ≤ 500。

## 输出

在一行中输出 n 个整数。任何最优数组都被接受。

## 评测方式

检查器核对数值和不同值的个数，并统计不同的区间和，必须恰好为 k 个。

## 样例

### 样例 1

输入：

```
1 1
```

输出：

```
-987654
```

### 样例 2

输入：

```
3 2
```

输出：

```
0 7 0
```

## 解法

每个单独的元素都是一个区间，所以有 k 个不同值的数组至少有 k 个不同的区间和。这个下界总能达到：先放 n − k + 1 个零，再接 1, −1, 2, −2, 3, …，直到凑满 n 个数。零和其余 k − 1 个数恰好给出 k 个不同的值。

区间和是两个前缀和之差。这个数组的前缀和是 0, …, 0, 1, 0, 2, 0, 3, …：零与 1, 2, …, m 交替出现，m 是用到的最大数。若数组以 −m 结尾，较早与较晚前缀和之差恰好覆盖 −m, …, m，共 2m + 1 = k 个值。若以 m 结尾，前缀和 m 位于最后，所以得不到 −m，区间和为 −(m − 1), …, m，同样是 2m = k 个值。因此该数组最优，答案可在 O(n) 内构造。

第二个样例中数组 0 0 1 的值为 0 和 1，区间和也是 0 和 1，各两个，与样例答案 0 7 0 一样。

## 优化解法

Go 和 Rust 输出同一构造，先是 n−k+1 个零，再接 1、−1、2、−2 等直到共有 n 项。Go 在适用于 n ≤ 500 的固定缓冲区内格式化答案并直接访问标准输入和输出句柄，Rust 使用有界输出缓冲区。两个版本都不构造中间整数数组或格式化字符串列表。

已通过评测的基础实现 [2065_constructive.cpp](2065_constructive.cpp), [2065_constructive.java](2065_constructive.java), [2065_constructive.py](2065_constructive.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

以下说明针对基础实现。

没有特别需要注意的地方。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2065_constructive.cpp](2065_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 132 KB | 11294335 |
| [2065_constructive.go](2065_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1056 KB | 11294350 |
| [2065_constructive.java](2065_constructive.java) \* | Java 1.8 | constructive | O(n) | AC | 0.125 s | 1640 KB | 11294361 |
| [2065_constructive.py](2065_constructive.py) \* | Python 3.12 x64 | constructive | O(n) | AC | 0.078 s | 456 KB | 11294354 |
| [2065_constructive.rs](2065_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 276 KB | 11294366 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2065_constructive_optimized.go](2065_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 316 KB | 11311234 |
| [2065_constructive_optimized.rs](2065_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 176 KB | 11311148 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
