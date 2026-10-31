# 2149. 把 ASCII 鸽子转成整齐的图案

[Timus 2149](https://acm.timus.ru/problem.aspx?space=1&num=2149) · 难度 148 · implementation

原题作者 Kirill Borozdin，出自 2019 年乌拉尔程序设计团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 只鸽子排成一排（n 为偶数），每只朝左或朝右，用 ASCII 字符画出。当左半边朝一个方向、右半边朝另一个方向，或者偶数位置的鸽子朝一个方向、奇数位置的朝另一个方向时，这一排就是整齐的。求最少需要转身的鸽子数。时间限制 0.5 秒，内存限制 256 MB。

## 输入

n（2 ≤ n ≤ 100），然后是三行、每行 5n − 1 个字符的鸽子图：朝左的鸽子为 `<@..`、`.OO=`、`./\.`，朝右的为 `..@>`、`=OO.`、`./\.`，相邻鸽子之间用一列点隔开。

## 输出

最少的转身次数。

## 样例

### 样例 1

输入：

```
8
..@>.<@...<@.....@>...@>...@>.<@...<@..
=OO...OO=..OO=.=OO..=OO..=OO...OO=..OO=
./\.../\.../\.../\.../\.../\.../\.../\.
```

输出：

```
4
```

### 样例 2

输入：

```
4
..@>...@>.<@.....@>
=OO..=OO...OO=.=OO.
./\.../\.../\.../\.
```

输出：

```
1
```

## 解法

只需要第一行：鸽子和字符均从 0 编号，鸽子 i 朝左当且仅当位置 5i 上的字符是 `<`。检查四个候选整齐图案，分成两对互为相反的图案。统计与"左半边朝左、右半边朝右"不同的鸽子数；与之相反的图案恰好在其余鸽子上不同，所以需要 n 减去这个数。"偶数位置朝左、奇数位置朝右"同理。答案是这四个数中的最小值，用时 O(n)。

第二个样例中只有第一只鸽子破坏了交替，所以转一只就够了。

## 优化解法

优化的 C++ 解法用 `scanf` 读入一个固定的 500 字节 `char` 缓冲区，而不是用
`std::cin` 读进 `std::string`，这样程序不需要 `iostream` 库；由于 `n ≤ 100`，一
行至多 5 · 100 − 1 = 499 个字符：{2149_implementation_optimized.cpp}。

优化的 Java 解法从 4 KB 缓冲区中读取字节，而不是用 `Scanner`，并直接按第一行的字
节、每隔五列数鸽子，不为它创建 `String`；另外两行读入后直接丢弃：
{2149_implementation_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `2149_implementation_optimized.cpp`: 时间降低 +0.00%; 内存降低 +73.47%; 基础版本: `2149_implementation.cpp`.

- `2149_implementation_optimized.java`: 时间降低 -12.00%; 内存降低 +75.13%; 基础版本: `2149_implementation.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [2149_implementation.rs](2149_implementation.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2149_implementation.cpp](2149_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 392 KB | 11304075 |
| [2149_implementation.go](2149_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1100 KB | 11295005 |
| [2149_implementation.java](2149_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1576 KB | 11304076 |
| [2149_implementation.py](2149_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 412 KB | 11295006 |
| [2149_implementation.rs](2149_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 240 KB | 11295008 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2149_implementation_optimized.cpp](2149_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 104 KB | 11304538 |
| [2149_implementation_optimized.java](2149_implementation_optimized.java) \* | Java 1.8 | implementation | O(n) | AC | 0.140 s | 392 KB | 11304539 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
