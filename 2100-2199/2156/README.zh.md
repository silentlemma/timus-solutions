# 2156. 把圆周上的差值分成相等的两半

[Timus 2156](https://acm.timus.ru/problem.aspx?space=1&num=2156) · 难度 656 · math, constructive

原题作者 Semyon Trifochkin，出自 2020 年乌拉尔团队程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 位有趣度为 a₁ … aₙ 的朋友围坐在圆桌旁，邻座 i 与 i + 1（最后一对为 n 与 1）之间谈话的有趣度为 |aᵢ − aᵢ₊₁|。把 n 段谈话分成两个非空集合，使总有趣度相等，或者输出 NO。任何合法划分都可接受。时间限制 1 秒，内存限制 256 MB。

## 输入

n（3 ≤ n ≤ 10⁵），然后是 a₁ … aₙ（1 ≤ aᵢ ≤ 10⁹）。

## 输出

YES，然后依次是第一个集合和第二个集合的大小及编号，或者 NO。

## 评测方式

检查器验证两个集合非空、划分了所有谈话且和相等。

## 样例

### 样例 1

输入：

```
3
1 2 3
```

输出：

```
YES
2
1 2
1
3
```

## 解法

答案总是 YES。沿圆桌绕一圈，有符号差值 aᵢ − aᵢ₊₁ 之和为 0。所以数值下降（aᵢ > aᵢ₊₁）的谈话与数值上升的谈话总有趣度相同，而相等邻座之间的谈话有趣度为 0，可以放到任一边。

若数值不全相等，则至少有一次下降和一次上升，两个集合都非空。若全部相等，每段谈话的有趣度都是 0，一段对其余 n − 1 段即可。工作量 O(n)。

样例中数值只在从 3 回到 1 时下降，所以谈话 3（有趣度 2）与谈话 1 和 2（各为 1）平衡。

## 优化解法

`2156_math_constructive_optimized.cpp`. 保留按环上下降边划分的精确构造。用 4 KiB fread 缓冲读取高度，只保留首个和前一个高度，并在 bitset 中标记下降边。若高度全相等，将首条边分给一组。两次扫描 bitset，经 4 KiB fwrite 缓冲输出两组，无需高度数组或索引向量。时间 O(n)，n 位加固定缓冲；划分性质和边编号不变。

精确源代码 Accepted #11326979：0.015 s / 136 KB。2026-11-20 保存的 G++ 13.2 样本：时间排名 1/33，内存排名 1/33。教学源代码保留。

按顺序读取数值，只保留首项和上一项。用位集记录下降的边，再扫描位集两次，分别输出两组边，无需保存输入数组或下标列表。

Go 为每条边保存一个布尔标记，使用固定大小的缓冲区输出下标。

Python 分块读写数据，每条边只占一个字节。

Rust 为每条边保存一个布尔标记，使用固定大小的缓冲区输出下标。

Java 使用缓冲输入输出，每条边保留一个布尔标记。内存从 9008 KB 降至 656 KB，耗时从 0.140 s 增至 0.156 s。

**优化版本的 Timus 提交记录**

`2156_math_constructive_optimized.cpp` (G++ 13.2 x64) №11326979 · `2156_math_constructive_optimized.go` (Go 1.14 x64) №11317380 · `2156_math_constructive_optimized.java` (Java 1.8) №11317394 · `2156_math_constructive_optimized.py` (Python 3.12 x64) №11317384 · `2156_math_constructive_optimized.rs` (Rust 1.75 x64) №11317388.

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11321927 · Java 1.8 №11321928 · Python 3.12 x64 №11321930 · Rust 1.75 x64 №11321931.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [2156_math_constructive.cpp](2156_math_constructive.cpp) | G++ 13.2 x64 | math, constructive | O(n) | AC | 0.093 s | 2652 KB | 11321927 |
| [2156_math_constructive.go](2156_math_constructive.go) | Go 1.14 x64 | math, constructive | O(n) | AC | 0.109 s | 8676 KB | 11322054 |
| [2156_math_constructive.java](2156_math_constructive.java) | Java 1.8 | math, constructive | O(n) | AC | 0.171 s | 8996 KB | 11321928 |
| [2156_math_constructive.py](2156_math_constructive.py) | Python 3.12 x64 | math, constructive | O(n) | AC | 0.156 s | 21304 KB | 11321930 |
| [2156_math_constructive.rs](2156_math_constructive.rs) | Rust 1.75 x64 | math, constructive | O(n) | AC | 0.078 s | 8860 KB | 11321931 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [2156_math_constructive_optimized.cpp](2156_math_constructive_optimized.cpp) | G++ 13.2 x64 | math, constructive | O(n) | AC | 0.015 s | 136 KB | 11326979 |
| [2156_math_constructive_optimized.go](2156_math_constructive_optimized.go) | Go 1.14 x64 | math, constructive | O(n) | AC | 0.031 s | 1068 KB | 11317380 |
| [2156_math_constructive_optimized.py](2156_math_constructive_optimized.py) | Python 3.12 x64 | math, constructive | O(n) | AC | 0.125 s | 1164 KB | 11317384 |
| [2156_math_constructive_optimized.rs](2156_math_constructive_optimized.rs) | Rust 1.75 x64 | math, constructive | O(n) | AC | 0.046 s | 304 KB | 11317388 |
| [2156_math_constructive_optimized.java](2156_math_constructive_optimized.java) | Java 1.8 | math, constructive | O(n) | AC | 0.156 s | 656 KB | 11317394 |
