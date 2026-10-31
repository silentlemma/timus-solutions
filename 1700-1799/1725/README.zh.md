# 1725. 满座！

[Timus 1725](https://acm.timus.ru/problem.aspx?space=1&num=1725) · 难度 142 · math

原题作者 Denis Dublennykh（由 Oleg Dolgorukov 准备），出自 2009 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Vasya 第一个坐进有 n 个座位的一排，坐在第 k 个座位；其他人逐个到来，直到坐满。
每人从入口与其座位之间已坐人数较少的一端进入，人数相同时从较近的一端进入。求最多有多少人会被 Vasya 的腿绊到。

## 输入

n 和 k（1 ≤ k ≤ n ≤ 50，n 为偶数）。

## 输出

被 Vasya 绊到的最多人数。

## 样例

### 样例 1

输入：

```
4 1
```

输出：

```
1
```

## 解法

把 Vasya 之外较长的那部分称为远侧，它有 max(k − 1, n − k) 个座位。答案就是这个数减 2，但不小于 0。`O(1)`。

远端的两个座位永远不会绊到。最后一个座位之外没有人；倒数第二个座位之外至多一人，而另一侧有 Vasya，
人数相同时它自己那一端更近。

远侧的其余所有人都可以被绊到。先让最远的两个座位坐下，再从远端向 Vasya 依次坐满远侧。
这样每个新来的人从 Vasya 那一端进入时途中只有 Vasya，从另一端进入时途中至少两人，所以他从 Vasya 身边经过。

近侧的人也可能被绊到，但只有在近侧已经比远侧满得多时才会发生，而那时远侧的人会发现 Vasya 那一侧人太多，
就不再被绊到。这样做从来不划算。

样例中远侧有三个座位，所以有一人被绊到：在座位 3 和 4 坐下之后，座位 2 上的人。

注意事项：

- n = 2 或 Vasya 坐在四个座位中间时答案为 0，而不是负数；
- 远侧可能在 Vasya 的任意一边。

对于所有不超过 16 的偶数 n 和所有 k，公式与穷举所有到达顺序的结果一致。

## 优化解法

优化的 C++ 解法用 `scanf` 读入两个数、用 `printf` 输出，而不是 `std::cin` 和
`std::cout`，这样程序不需要 `iostream` 库及其缓冲区；公式不变：
{1725_math_optimized.cpp}。

优化的 Java 解法用 `System.in.read` 逐字节读入两个数，而不是创建 `Scanner`，这样
JVM 不必加载扫描器及其正则表达式；公式不变：{1725_math_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1725_math_optimized.cpp`: 时间降低 +0.00%; 内存降低 +74.75%; 基础版本: `1725_math.cpp`.

- `1725_math_optimized.java`: 时间降低 +25.60%; 内存降低 +77.89%; 基础版本: `1725_math.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1725_math.go](1725_math.go).
- [1725_math.rs](1725_math.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1725_math.cpp](1725_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB | 11289360 |
| [1725_math.go](1725_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB | 11289361 |
| [1725_math.java](1725_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1592 KB | 11289365 |
| [1725_math.py](1725_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 340 KB | 11289363 |
| [1725_math.rs](1725_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 244 KB | 11304071 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1725_math_optimized.cpp](1725_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 100 KB | 11304482 |
| [1725_math_optimized.java](1725_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 352 KB | 11304483 |
