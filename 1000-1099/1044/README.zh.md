# 1044. 统计 N 位平衡票号

[Timus 1044](https://acm.timus.ru/problem.aspx?space=1&num=1044) · 难度 123 · bruteforce

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

`N = 8` 时答案是 4816030，32 位就放得下，但除 Python 外，平方和仍用 64 位整数累加。

注意事项：

- 前导零也算：`0000` 也是一个票号；
- 每一半有 `N / 2` 位，而不是 `N` 位。

[题目 1036](../1036/README.zh.md) 问的是最多 100 位、给定数字总和时的同样问题；那里的计数用动态规划求出，并且
需要高精度整数。

## 优化解法

优化的 C++ 解法把计数放在栈上一个 37 个元素的固定数组里，而不是 `std::vector`：
因为 `N ≤ 8`，每一半最多四位，数字和最多 36。这样程序完全不需要容器库：
{1044_bruteforce_optimized.cpp}。

优化的 Java 解法直接从 `System.in` 逐字节读入 `N`，而不是创建 `Scanner`，后者的
正则表达式和区域设置数据比计数本身还费资源；计数方法不变：
{1044_bruteforce_optimized.java}。

较快的 Go 版本使用数位和动态规划，代替枚举所有半张票号。追加一位相当于将计数与十个 1 卷积；滑动和使每个新计数只需常数时间。经过 `N/2` 步后，将计数的平方相加即得答案。时间为 `O(N²)`，额外空间为 `O(N)`。枚举版本保留为基础实现。

{1044_dp.go}.

与源代码对应的 Accepted 记录：基础版本 0.046 秒 / 1080 KB；本版本 0.015 秒 / 804 KB（提交 11307438）。在 2026-10-31 的快照中达到排名目标。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1044_bruteforce_optimized.cpp`: 时间降低 +0.00%; 内存降低 +36.73%; 基础版本: `1044_bruteforce.cpp`.

- `1044_dp.go`: 时间降低 +67.39%; 内存降低 +25.56%; 基础版本: `1044_bruteforce.go`.

- `1044_bruteforce_optimized.java`: 时间降低 +16.13%; 内存降低 +79.64%; 基础版本: `1044_bruteforce.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1044_bruteforce.rs](1044_bruteforce.rs).

- 各语言做同样的计数；Python 对 `str(x)` 求数字和。

## 题解代码

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1044_bruteforce.cpp](1044_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 196 KB | 11278614 |
| [1044_bruteforce.go](1044_bruteforce.go) | Go 1.14 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.046 s | 1080 KB | 11278618 |
| [1044_bruteforce.java](1044_bruteforce.java) | Java 1.8 | bruteforce | O(10^(N/2) · N) | AC | 0.093 s | 1552 KB | 11278622 |
| [1044_bruteforce.py](1044_bruteforce.py) | Python 3.12 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.078 s | 288 KB | 11278621 |
| [1044_bruteforce.rs](1044_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 216 KB | 11278623 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1044_bruteforce_optimized.cpp](1044_bruteforce_optimized.cpp) | G++ 13.2 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.001 s | 124 KB | 11304375 |
| [1044_dp.go](1044_dp.go) | Go 1.14 x64 | dp | O(N²) | AC | 0.015 s | 804 KB | 11307438 |
| [1044_bruteforce_optimized.java](1044_bruteforce_optimized.java) \* | Java 1.8 | bruteforce | O(10^(N/2) · N) | AC | 0.078 s | 316 KB | 11304376 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
