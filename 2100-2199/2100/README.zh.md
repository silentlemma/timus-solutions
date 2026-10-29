# 2100. 统计宾客并避开十三

[Timus 2100](https://acm.timus.ru/problem.aspx?space=1&num=2100) · 难度 29 · implementation

原题作者 Alexey Danilyuk，出自 2016 年乌拉尔联邦大学青少年锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一对新人邀请了 n 位朋友；回复 `name+one` 表示这位朋友带一位伴侣来。所有人与新人坐在同一张桌子旁，如果恰好有 13 人，就加一个假人。每个座位 100 美元。输出晚宴的花费。时间限制 1 秒，内存限制 64 MB。

## 输入

1 ≤ n ≤ 20，然后是 n 条回复，每条是由不超过 20 个拉丁字母组成的名字，可能带有 `+one`。

## 输出

以美元计的花费。

## 样例

### 样例 1

输入：

```
3
Ted+one
Robin
Barney
```

输出：

```
600
```

### 样例 2

输入：

```
6
Alice+one
Bob+one
carl
Debora+one
Enrique+one
FRED+one
```

输出：

```
1400
```

## 解法

从两位主人开始，以 `+one` 结尾的回复加 2，否则加 1，把 13 变成 14，再乘以 100。

第二个样例中会有 2 + 5 · 2 + 1 = 13 人入座，所以加一个假人：1400。

## 优化解法

优化的 C++ 解法用 `scanf` 代替 `iostream`，把回复读入 25 字节的缓冲区，并统计含
有 `+` 的回复，因为只有以 `+one` 结尾的回复才含有它：128 KB，而不是 396 KB，时间
不变。

优化的 Java 解法按 1 KB 分块读入，并和 C++ 解法一样逐字节统计回复中的 `+`，而不
是使用 `Scanner` 和字符串：0.093 s，而不是 0.140 s；364 KB，而不是 1572 KB。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2100_implementation.cpp](2100_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 396 KB | 11303533 |
| [2100_implementation.go](2100_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1076 KB | 11294707 |
| [2100_implementation.java](2100_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1572 KB | 11303534 |
| [2100_implementation.py](2100_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 420 KB | 11294708 |
| [2100_implementation.rs](2100_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 236 KB | 11294714 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2100_implementation_optimized.cpp](2100_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303968 |
| [2100_implementation_optimized.java](2100_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 364 KB | 11303969 |
