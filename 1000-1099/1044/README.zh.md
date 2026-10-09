# 1044. 统计 N 位平衡票号

[Timus 1044](https://acm.timus.ru/problem.aspx?space=1&num=1044) · 难度 122 · bruteforce

原题作者 Stanislav Vasiliev，出自 2000 年 10 月第五届乌拉尔国立大学团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

票号有 `N` 位数字（`N` 为偶数，`2 ≤ N ≤ 8`；允许前导零）。若前一半数字之和等于后一半数字之和，则票号是平衡的。
统计平衡票号的个数。

时间限制：2 秒。内存限制：64 MB。

## 输入

`N`。

## 输出

平衡票号的个数。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
4
```

输出：

```
670
```

### 样例 2

输入：

```
2
```

输出：

```
10
```

## 题解

两半互相独立。对每个和 `s`，统计小于 `10^(N/2)` 的数中数字和为 `s` 的个数：最多只需检查 10000 个数。平衡票号
就是一对数字和相同的两半，所以答案是对所有 `s` 求 `ways[s]^2` 之和。`O(10^(N/2) · N)`。

`N = 8` 时答案是 4816030，32 位就放得下，但平方和仍用 64 位整数累加。

注意事项：

- 前导零也算：`0000` 也是一个票号；
- 每一半有 `N / 2` 位，而不是 `N` 位。

[题目 1036](../1036/README.zh.md) 问的是最多 100 位、给定数字总和时的同样问题；那里的计数用动态规划求出，并且
需要高精度整数。

## 各语言说明

- 各语言做同样的计数；Python 对 `str(x)` 求数字和。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1044_bruteforce.cpp](1044_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 196 KB |
| [1044_bruteforce.go](1044_bruteforce.go) | Go 1.14 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.046 s | 1080 KB |
| [1044_bruteforce.java](1044_bruteforce.java) | Java 1.8 | bruteforce | O(10^(N/2) · N) | AC | 0.093 s | 1552 KB |
| [1044_bruteforce.py](1044_bruteforce.py) | Python 3.12 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.078 s | 288 KB |
| [1044_bruteforce.rs](1044_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 216 KB |
