# 2138. 交换 32 位数的字节顺序

[Timus 2138](https://acm.timus.ru/problem.aspx?space=1&num=2138) · 难度 111 · math

原题作者 Aidar Islamov，出自 2019 年乌拉尔团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

不超过 2³² − 1 的数以四位 256 进制数字传送。"好"计算机从最高位开始读数字，"坏"计算机从最低位开始读。一台计算机从另一种类型的计算机收到一个数，读成了 v。输出实际发送的数。时间限制 0.5 秒，内存限制 256 MB。

## 输入

发送方类型 GOOD 或 BAD，然后是 v（0 ≤ v ≤ 4 294 967 295）。

## 输出

发送的数。

## 样例

### 样例 1

输入：

```
GOOD
16777216
```

输出：

```
1
```

### 样例 2

输入：

```
BAD
1000
```

输出：

```
3892510720
```

## 解法

无论哪一方是发送方，接收方都按相反顺序读同样的四位数字。所以答案就是把 v 的四位 256 进制数字倒序，与发送方类型无关。用 % 256 和 / 256 从最低位取出 v 的数字，再从高位开始拼出结果，或者直接做字节交换。

第一个样例中 16 777 216 的数字是 1;0;0;0，倒序后得到 1。

## 优化解法

优化的 Java 解法直接从 `System.in` 逐字节读取输入，而不是创建 `Scanner`；由于
GOOD 和 BAD 中没有数字，它只需把遇到的所有数字依次拼进 `long` 类型的 v，后者能容
纳不超过 2³² − 1 的任何值：{2138_math_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `2138_math_optimized.java`: 时间降低 +0.00%; 内存降低 +78.23%; 基础版本: `2138_math.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [2138_math.cpp](2138_math.cpp).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2138_math.cpp](2138_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 132 KB | 11304054 |
| [2138_math.go](2138_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB | 11294918 |
| [2138_math.java](2138_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1580 KB | 11304060 |
| [2138_math.py](2138_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 424 KB | 11294919 |
| [2138_math.rs](2138_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB | 11294921 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2138_math_optimized.java](2138_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.109 s | 344 KB | 11304333 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
