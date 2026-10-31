# 1402. 鸡尾酒

[Timus 1402](https://acm.timus.ru/problem.aspx?space=1&num=1402) · 难度 130 · combinatorics

原题作者 Sergey Pupyrev，出自 2005 年 10 月 15 日第十二届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

鸡尾酒由 N ≤ 21 种饮料中的两种或更多种调成，每种至多用一次，且饮料的顺序不
同算不同的鸡尾酒。求不同鸡尾酒的数目。

时间限制：1 秒。内存限制：64 MB。

## 输入

数 N（1 ≤ N ≤ 21）。

## 输出

鸡尾酒的数目。

## 样例

### 样例 1

输入:

```
3
```

输出:

```
12
```

## 解法

k 种饮料的鸡尾酒就是从中有序地选出 k 种不同的饮料，共有
N·(N − 1)·…·(N − k + 1) 种。对 k 从 2 到 N 求和，每个乘积由上一个得到。
`O(N)`。

注意事项：

- 只有一种饮料时没有鸡尾酒（测试 02）；
- N = 21 时答案约为 1.4·10²⁰，超过 64 位，所以解答使用 128 位整数或大整数
  （测试 07）。

测试按精确比较判定。

## 优化解法

优化的 C++ 解法仍用 128 位整数求和，但把各位数字从后往前写进一个 23 个字符的固定
数组，而不是逐个插到 `std::string` 的开头：因为 `N ≤ 21`，答案小于
21·21! < 10²²，22 位数字加上结尾的零总能放下。不用 `<string>`，程序本身就不在堆
上分配内存：{1402_combinatorics_optimized.cpp}。

优化的 Java 解法直接从 `System.in` 逐字节读入 N，而不是创建 `Scanner`，后者的正
则表达式和区域设置数据比至多二十次乘法本身还费资源；求和仍用 `BigInteger`：
{1402_combinatorics_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1402_combinatorics_optimized.cpp`: 时间降低 +0.00%; 内存降低 +48.94%; 基础版本: `1402_combinatorics.cpp`.

- `1402_combinatorics_optimized.java`: 时间降低 +0.00%; 内存降低 +73.70%; 基础版本: `1402_combinatorics.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1402_combinatorics.go](1402_combinatorics.go).
- [1402_combinatorics.rs](1402_combinatorics.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1402_combinatorics.cpp](1402_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N) | AC | 0.015 s | 188 KB | 11286026 |
| [1402_combinatorics.go](1402_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N) | AC | 0.031 s | 1176 KB | 11286027 |
| [1402_combinatorics.java](1402_combinatorics.java) | Java 1.8 | combinatorics | O(N) | AC | 0.109 s | 1688 KB | 11286031 |
| [1402_combinatorics.py](1402_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N) | AC | 0.078 s | 388 KB | 11286029 |
| [1402_combinatorics.rs](1402_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N) | AC | 0.031 s | 232 KB | 11286032 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1402_combinatorics_optimized.cpp](1402_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(N) | AC | 0.001 s | 96 KB | 11304432 |
| [1402_combinatorics_optimized.java](1402_combinatorics_optimized.java) | Java 1.8 | combinatorics | O(N) | AC | 0.109 s | 444 KB | 11304433 |
