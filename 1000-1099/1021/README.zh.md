# 1021. 从两个有序列表中找出和为给定值的一对数

[Timus 1021](https://acm.timus.ru/problem.aspx?space=1&num=1021) · 难度 148 · two_pointers, hashing

原题出自 2000 年 10 月 7 日斯维尔德洛夫斯克州第二届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定两个整数列表：第一个按递增排序，第二个按递减排序（各有 `1 ≤ N_i ≤ 50 000` 个数，每个数在 -32768 到
32767 之间）。判断能否从每个列表中各选一个数，使它们之和恰好为 10000。

时间限制：1 秒。内存限制：64 MB。

## 输入

第一个列表：先是其大小，然后每行一个数。接着是同样格式的第二个列表。

## 输出

若存在这样的一对数输出 `YES`，否则输出 `NO`。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
3
-5
3
9998
3
10
7
2
```

输出：

```
YES
```

### 样例 2

输入：

```
3
1
2
3
3
9000
50
0
```

输出：

```
NO
```

## 题解

**双指针。** 指针 `i` 放在递增列表开头，`j` 放在递减列表开头，于是 `up[i]` 是第一个列表剩余的最小数，
`down[j]` 是第二个列表剩余的最大数。比较 `up[i] + down[j]` 与 10000：

- 相等——找到了；
- 较小——`up[i]` 不可能属于任何一对，因为连剩余最大的 `down[j]` 都不够：右移 `i`；
- 较大——`down[j]` 不可能属于任何一对，因为连剩余最小的 `up[i]` 都太大：右移 `j`。

当某个指针越过列表末尾时，不存在这样的一对。每一步排除一个数：`O(N_1 + N_2)`。

**哈希。** 把第二个列表中每个 `b` 对应的 `10000 - b` 放入集合，检查第一个列表中是否有数在其中——平均
同样是线性的，也不需要有序。

注意事项：

- 第二个列表按相反顺序排序：两个列表都从开头开始走；
- 和为 10000 可能需要极端值，例如 `32767 + (-22767)`。

## 优化解法

优化的 C++ 解法从用 `fread` 反复填充的 4 KB 缓冲区中手工解析数字，而不是用
`scanf`。它只保存递增列表，类型为 `int16_t`，足以容纳 -32768 到 32767 之间的任何
数；并且在读入递减列表的同时移动指针，所以第二个列表根本不用保存：
{1021_two_pointers_optimized.cpp}。

优化的 Go 解法从 `bufio.Reader` 中逐字节解析数字，而不是用 `fmt.Fscan`。它只保存
递增列表，类型为 `int16`，足以容纳 -32768 到 32767 之间的任何数；并且在读入递减
列表的同时移动指针，所以第二个列表根本不用保存：
{1021_two_pointers_optimized.go}。

优化的 Java 解法从由 `System.in` 反复填充的 4 KB 缓冲区中手工解析数字，而不是用
`StreamTokenizer`。它只保存递增列表，类型为 `short`，足以容纳 -32768 到 32767 之
间的任何数；并且在读入递减列表的同时移动指针，所以第二个列表根本不用保存：
{1021_two_pointers_optimized.java}。

优化的 Python 解法利用每行恰好一个数这一点，边读边转换每一行，而不是把整个输入切
分成列表。它不用集合，而是在一个有 65536 个单元的 `bytearray` 中标记第一个列表的
数，-32768 到 32767 的每个可能值各占一个单元。对第二个列表的每个 `b`，先检查
`10000 - b` 是否在此范围内，在范围内才在其中查找：{1021_hashing_optimized.py}。

优化的 Rust 解法从由标准输入反复填充的 4 KB 缓冲区中手工解析数字，而不是把整个输
入读进 `String`。它只保存递增列表，类型为 `i16`，足以容纳 -32768 到 32767 之间的
任何数；并且在读入递减列表的同时移动指针，所以第二个列表根本不用保存：
{1021_two_pointers_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1021_two_pointers_optimized.cpp`: 时间降低 +80.77%; 内存降低 +63.89%; 基础版本: `1021_two_pointers.cpp`.

- `1021_two_pointers_optimized.go`: 时间降低 +50.00%; 内存降低 +57.25%; 基础版本: `1021_two_pointers.go`.

- `1021_two_pointers_optimized.java`: 时间降低 +37.60%; 内存降低 +45.58%; 基础版本: `1021_two_pointers.java`.

- `1021_hashing_optimized.py`: 时间降低 -39.74%; 内存降低 +95.36%; 基础版本: `1021_hashing.py`.

- `1021_two_pointers_optimized.rs`: 时间降低 +67.39%; 内存降低 +86.55%; 基础版本: `1021_two_pointers.rs`.

## 各语言说明

- **C++**、**Go**、**Java**、**Rust**：双指针。
- **Python**：集合求交，以 C 的速度运行。

## 题解代码

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1021_two_pointers.cpp](1021_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.078 s | 576 KB | 11278250 |
| [1021_two_pointers.go](1021_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 2620 KB | 11278252 |
| [1021_two_pointers.java](1021_two_pointers.java) | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.125 s | 904 KB | 11278257 |
| [1021_hashing.py](1021_hashing.py) | Python 3.12 x64 | hashing | O(N1 + N2) on average | AC | 0.078 s | 10700 KB | 11278255 |
| [1021_two_pointers.rs](1021_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.046 s | 2112 KB | 11278259 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1021_two_pointers_optimized.cpp](1021_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 208 KB | 11304533 |
| [1021_two_pointers_optimized.go](1021_two_pointers_optimized.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.031 s | 1120 KB | 11304534 |
| [1021_two_pointers_optimized.java](1021_two_pointers_optimized.java) | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.078 s | 492 KB | 11304535 |
| [1021_hashing_optimized.py](1021_hashing_optimized.py) \* | Python 3.12 x64 | hashing | O(N1 + N2) on average | AC | 0.109 s | 496 KB | 11304537 |
| [1021_two_pointers_optimized.rs](1021_two_pointers_optimized.rs) | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 284 KB | 11304536 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
