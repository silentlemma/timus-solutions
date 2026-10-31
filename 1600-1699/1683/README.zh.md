# 1683. 冰箱

[Timus 1683](https://acm.timus.ru/problem.aspx?space=1&num=1683) · 难度 137 · greedy

原题作者 Stanislav Vasilyev，出自 2009 年 2 月 28 日第十届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把宽 1 厘米、长 n 厘米的纸条折成 1 × 1 厘米、共 n 层的方块。每次折叠都从左端量出整数厘米，
把这一段向右翻折，于是左端移动了这个长度。求最少的折叠次数以及每次量出的长度。

## 输入

n（1 ≤ n ≤ 10⁹）。

## 输出

折叠次数，然后按顺序给出量出的长度。任何最短的序列都可以。

## 样例

### 样例 1

输入：

```
12
```

输出：

```
4
5 3 2 1
```

## 解法

长为 L 的纸条只有在翻过去的部分能放在剩余部分上时，即 x ≤ L − x，才能折 x 厘米，
此后剩下长度 L − x ≥ ⌈L / 2⌉。所以每次折叠至多把纸条减半（向上取整），
而每次折 ⌊L / 2⌋ 恰好做到这一点：折叠次数是满足 2ᵐ ≥ n 的最小 m。`O(log n)`。

注意事项：

- n = 1 不需要折叠：输出 0 和一个空列表；
- 样例中的 5 3 2 1 只是众多答案之一，所以检查器比较次数并重放每次折叠。

检查器重放每次折叠，并把次数与贪心的结果比较。

## 优化解法

优化的 C++ 解法把各次折叠放在栈上 30 个数的固定数组里，而不是不断增长的
`std::vector`。因为 n ≤ 10⁹ < 2³⁰，最多对半折 30 次纸条就只剩 1 厘米，所以数组总
够用，程序本身也不在堆上分配内存：{1683_greedy_optimized.cpp}。

优化的 Java 解法用 `BufferedReader` 读入唯一的一行，再用 `Long.parseLong` 转成
数，而不是创建 `Scanner`，后者的正则表达式和区域设置数据比 30 次对半折叠贵得多：
{1683_greedy_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1683_greedy_optimized.cpp`: 时间降低 +0.00%; 内存降低 +47.92%; 基础版本: `1683_greedy.cpp`.

- `1683_greedy_optimized.java`: 时间降低 +25.60%; 内存降低 +72.84%; 基础版本: `1683_greedy.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1683_greedy.go](1683_greedy.go).
- [1683_greedy.rs](1683_greedy.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy.cpp](1683_greedy.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 192 KB | 11288846 |
| [1683_greedy.go](1683_greedy.go) | Go 1.14 x64 | greedy | O(log n) | AC | 0.031 s | 1096 KB | 11288848 |
| [1683_greedy.java](1683_greedy.java) | Java 1.8 | greedy | O(log n) | AC | 0.125 s | 1664 KB | 11288850 |
| [1683_greedy.py](1683_greedy.py) | Python 3.12 x64 | greedy | O(log n) | AC | 0.125 s | 372 KB | 11288849 |
| [1683_greedy.rs](1683_greedy.rs) | Rust 1.75 x64 | greedy | O(log n) | AC | 0.015 s | 244 KB | 11288851 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy_optimized.cpp](1683_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 100 KB | 11304447 |
| [1683_greedy_optimized.java](1683_greedy_optimized.java) | Java 1.8 | greedy | O(log n) | AC | 0.093 s | 452 KB | 11304448 |
