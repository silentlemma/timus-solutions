# 1219. 一百万个字母，单字母、双字母、三字母都不过于频繁

[Timus 1219](https://acm.timus.ru/problem.aspx?space=1&num=1219) · 难度 121 · constructive

原题作者 Pavel Atnashev 和 Leonid Volkov，出自第七届乌拉尔国立大学大学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

输出 1,000,000 个小写拉丁字母，使每个字母最多出现 40,000 次，每两个相邻字母组成
的对最多出现 2,000 次，每三个相邻字母组成的组最多出现 100 次。

时间限制：1 秒。内存限制：64 MB。

## 输入

没有输入。

## 输出

一行字母。

## 评测方式

任何满足三个限制的序列都被接受。

## 样例

没有输入，题面也没有给出样例输出。

## 解法

把一百万个字母尽量均匀地分布。字母有 26 个，对有 `26² = 676` 种，三元组有
`26³ = 17,576` 种，所以完全均匀时分别出现约 38,462、1,479 和 57 次，都在限制以内。

26 个字母上的 3 阶 de Bruijn 序列是一个长 17,576 的环，绕环一周时每个三元组恰好
作为三个相邻字母出现一次。把它首尾相接地重复，每个三字母窗口仍是环上的窗口，所以
约 57 份之后，每个三元组出现 56 或 57 次，每个对出现的次数是其 26 倍，每个字母是其
676 倍：这里最多为 38,532、1,482 和 57。这个环由经典构造得到：按字典序拼接长度
整除 3 的 Lyndon 词。`L = 10⁶` 时为 `O(L)`。

注意事项：

- 跨越两份之间的窗口是序列的环形窗口，因此不会破坏均衡；
- 随机序列大概也能通过，但其最频繁的三元组约出现 90 次，接近上限。

输出已按三个限制检查过，上面的数字就是它实际的最大值。

## 优化解法

优化的 C++ 解法直接把环构造成 17,576 个字母字节，用 `fwrite` 输出 56 遍，再输出
它的前 15,744 个字母，而不是填充一个一百万字母的字符串；输出完全相同：
{1219_constructive_optimized.cpp}。

优化的 Go 解法把环转换成 17,576 个字母字节的块，通过 `bufio` 输出 56 遍，再输出
它的前 15,744 个字母，而不是填充一个一百万字节的切片；输出完全相同：
{1219_constructive_optimized.go}。

优化的 Java 解法直接把环构造成 17,576 个字母字节，输出 56 遍，再输出它的前
15,744 个字母，而不是使用各有一百万个元素的 `int` 数组和字节数组；输出完全相同：
{1219_constructive_optimized.java}。

优化的 Python 解法直接在 17,576 个字母的 `bytearray` 中构造环，输出 56 遍，再输
出它的前 15,744 个字母，而不是创建数字列表和一百万字母的字符串；输出完全相同：
{1219_constructive_optimized.py}。

优化的 Rust 解法把环转换成 17,576 个字母字节的块，通过 `BufWriter` 输出 56 遍，
再输出它的前 15,744 个字母，而不是收集一个一百万字节的向量；输出完全相同：
{1219_constructive_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1219_constructive_optimized.cpp`: 时间降低 +0.00%; 内存降低 +91.89%; 基础版本: `1219_constructive.cpp`.

- `1219_constructive_optimized.go`: 时间降低 +0.00%; 内存降低 +38.11%; 基础版本: `1219_constructive.go`.

- `1219_constructive_optimized.java`: 时间降低 +75.81%; 内存降低 +95.58%; 基础版本: `1219_constructive.java`.

- `1219_constructive_optimized.py`: 时间降低 +60.26%; 内存降低 +86.97%; 基础版本: `1219_constructive.py`.

- `1219_constructive_optimized.rs`: 时间降低 +0.00%; 内存降低 +80.53%; 基础版本: `1219_constructive.rs`.

## 各语言说明

- 所有语言都用同样的递归构造生成这个环，并一次性写出整行。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1219_constructive.cpp](1219_constructive.cpp) | G++ 13.2 x64 | constructive | O(L) | AC | 0.001 s | 1184 KB | 11283683 |
| [1219_constructive.go](1219_constructive.go) | Go 1.14 x64 | constructive | O(L) | AC | 0.015 s | 2624 KB | 11283684 |
| [1219_constructive.java](1219_constructive.java) | Java 1.8 | constructive | O(L) | AC | 0.062 s | 8868 KB | 11283687 |
| [1219_constructive.py](1219_constructive.py) | Python 3.12 x64 | constructive | O(L) | AC | 0.078 s | 3224 KB | 11283686 |
| [1219_constructive.rs](1219_constructive.rs) | Rust 1.75 x64 | constructive | O(L) | AC | 0.001 s | 2404 KB | 11283688 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1219_constructive_optimized.cpp](1219_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(L) | AC | 0.001 s | 96 KB | 11304363 |
| [1219_constructive_optimized.go](1219_constructive_optimized.go) | Go 1.14 x64 | constructive | O(L) | AC | 0.001 s | 1624 KB | 11304367 |
| [1219_constructive_optimized.java](1219_constructive_optimized.java) | Java 1.8 | constructive | O(L) | AC | 0.001 s | 392 KB | 11304365 |
| [1219_constructive_optimized.py](1219_constructive_optimized.py) \* | Python 3.12 x64 | constructive | O(L) | AC | 0.031 s | 420 KB | 11304366 |
| [1219_constructive_optimized.rs](1219_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(L) | AC | 0.015 s | 468 KB | 11304368 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
