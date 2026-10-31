# 1796. 游乐园

[Timus 1796](https://acm.timus.ru/problem.aspx?space=1&num=1796) · 难度 111 · math

原题作者 Eugene Kurpilyansky（由 Egor Shchelkonogov 准备），出自 2010 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

老师用面额 10、50、100、500、1000 和 5000 卢布的纸币买票。钱够买这些票，但拿走任何一张纸币就不够了。给定每种面额的张数和票价，列出所有可能的票数。

## 输入

六个非负的纸币张数（面额从小到大），然后是票价。所有数都是不超过 1000 的整数，票
价为正。至少存在一个答案。

## 输出

可能答案的个数，然后按升序输出这些答案。

## 样例

### 样例 1

输入：

```
0 2 0 0 0 0
10
```

输出：

```
5
6 7 8 9 10
```

### 样例 2

输入：

```
1 2 0 0 0 0
10
```

输出：

```
1
11
```

## 解法

设总额为 T，给出的纸币中最小面额为 s。买 k 张票钱必须够：k·price ≤ T。少任何一张纸币就必须不够，而最小的纸币是最难满足的情形：
若 T − s 不够，那么少任何更大面额的纸币也不够。所以 T − s < k·price，答案是从 ⌊(T − s)/price⌋ + 1 到 ⌊T/price⌋ 的所有 k。
`O(answers)`，答案最多 5000 个。

第一个样例中 T = 100，s = 50：少一张纸币后 50 卢布必须不够，所以票数大于 5，且最多为 10。

注意事项：

- 要拿走的是现有纸币中最小的那张，而不一定是 10 卢布纸币；
- 有一张 5000 卢布纸币且票价为 1 时，有 5000 个答案，全在一行。

在 300 个随机情形上（纸币少和纸币多），答案与一个独立的已通过实现一致。

## 优化解法

优化的 C++ 解法用 `scanf` 代替 `std::cin` 读入，并用 `printf` 立即输出每个答案，
而不是先把最多 5000 个答案收集到 `std::string` 中，因此程序完全不需要
`iostream`：{1796_math_optimized.cpp}。

优化的 Java 解法直接从 `System.in` 逐位读取这七个数，而不是创建 `Scanner`；答案
仍收集在 `StringBuilder` 中：{1796_math_optimized.java}。

优化的 Rust 解法从按空白切分得到的迭代器中逐个取出这七个数，而不是先收集到向量
中；答案通过 `BufWriter` 写出，而不是为最多 5000 个答案各建一个 `String` 再拼
接：{1796_math_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1796_math_optimized.cpp`: 时间降低 +0.00%; 内存降低 +71.68%; 基础版本: `1796_math.cpp`.

- `1796_math_optimized.java`: 时间降低 +28.44%; 内存降低 +63.03%; 基础版本: `1796_math.java`.

- `1796_math_optimized.rs`: 时间降低 -106.67%; 内存降低 +47.90%; 基础版本: `1796_math.rs`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1796_math.go](1796_math.go).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1796_math.cpp](1796_math.cpp) | G++ 13.2 x64 | math | O(answers) | AC | 0.015 s | 452 KB | 11304050 |
| [1796_math.go](1796_math.go) | Go 1.14 x64 | math | O(answers) | AC | 0.031 s | 1288 KB | 11289894 |
| [1796_math.java](1796_math.java) | Java 1.8 | math | O(answers) | AC | 0.109 s | 1980 KB | 11304051 |
| [1796_math.py](1796_math.py) | Python 3.12 x64 | math | O(answers) | AC | 0.078 s | 720 KB | 11304052 |
| [1796_math.rs](1796_math.rs) | Rust 1.75 x64 | math | O(answers) | AC | 0.015 s | 476 KB | 11304053 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1796_math_optimized.cpp](1796_math_optimized.cpp) | G++ 13.2 x64 | math | O(answers) | AC | 0.015 s | 128 KB | 11304279 |
| [1796_math_optimized.java](1796_math_optimized.java) | Java 1.8 | math | O(answers) | AC | 0.078 s | 732 KB | 11304331 |
| [1796_math_optimized.rs](1796_math_optimized.rs) | Rust 1.75 x64 | math | O(answers) | AC | 0.031 s | 248 KB | 11304332 |
