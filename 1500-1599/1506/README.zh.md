# 1506. 数字列

[Timus 1506](https://acm.timus.ru/problem.aspx?space=1&num=1506) · 难度 134 · implementation

原题作者 Stanislav Vasiliev，出自 2006 年第 31 届 ACM ICPC 叶卡捷琳堡四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把 N 个 0 到 999 之间的数（1 ≤ N ≤ 100）排成 K 列（1 ≤ K ≤ N），行数尽可能少。除最
后一列可以较短外，各列高度相同。数先从上到下填满第一列，再填第二列，依此类推。每个
数在 4 个字符宽的字段中右对齐，行末没有多余空格。
保证存在恰好有 K 个非空列的合法表格。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 K，然后是 N 个数。

## 输出

排好的表格。

## 样例

### 样例 1

输入:

```
7 3
1 2 30 40 50 600 700
```

输出:

```
   1  40 700
   2  50
  30 600
```

## 解法

最少的行数是 H = ⌈N / K⌉。任何合法高度 h 都满足 h ≥ H 且 (K − 1)·h < N。
由有解的保证可得 (K − 1)·H < N，因此高度 H 下最后一列非空。
第 c 列放下标从 c·H 到 c·H + H − 1 的数，所以第 r 行由
c = 0, 1, … 时存在的数 c·H + r 组成；它们在第一个用完的列处停止，而这只可能是最后
一列。每个数占 4 个字符输出，然后结束这一行。`O(N)`。

注意事项：

- 数是沿列往下排的，而不是沿行（测试 01）；
- 每个数都占 4 个字符，第一个也是，所以每行都以空格开头（测试 01）；
- 最后一列较短时，下面的行少一个数提前结束，且没有行末空格（测试 06）；
- 有解的保证不可忽略：最后一列至少有一个数（测试 06）；并非所有满足 1 ≤ K ≤ N 的组合都有解；
- K = N 时只有一行，K = 1 时只有一列（测试 03、04）。

## 优化解法

优化的 C++ 解法把数放在栈上 100 个 `int` 的固定数组里，而不是 `std::vector`，因
为 N ≤ 100，所以程序完全不在堆上分配内存：{1506_implementation_optimized.cpp}。

优化的 Java 解法自己补齐每个格子：用 `Integer.toString` 转换数字，并在前面补空格
到 4 个字符，而不是调用 `String.format`，后者每个格子都要新建一个格式化器并解析
格式串。不超过 999 的数最多三位，所以每个格子前面至少有一个空格：
{1506_implementation_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1506_implementation_optimized.cpp`: 时间降低 +0.00%; 内存降低 +48.98%; 基础版本: `1506_implementation.cpp`.

- `1506_implementation_optimized.java`: 时间降低 +14.68%; 内存降低 +56.56%; 基础版本: `1506_implementation.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1506_implementation.go](1506_implementation.go).
- [1506_implementation.rs](1506_implementation.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1506_implementation.cpp](1506_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11287283 |
| [1506_implementation.go](1506_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1108 KB | 11287284 |
| [1506_implementation.java](1506_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 976 KB | 11287286 |
| [1506_implementation.py](1506_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.093 s | 460 KB | 11287285 |
| [1506_implementation.rs](1506_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 252 KB | 11287287 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1506_implementation_optimized.cpp](1506_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 100 KB | 11304437 |
| [1506_implementation_optimized.java](1506_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 424 KB | 11304438 |
