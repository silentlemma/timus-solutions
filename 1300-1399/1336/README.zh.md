# 1336. 本·贝察列尔问题

[Timus 1336](https://acm.timus.ru/problem.aspx?space=1&num=1336) · 难度 123 · math

原题作者 Den Raskovalov，出自 2004 年 10 月 16 日第十届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把整数 n（1 ≤ n ≤ 10⁹）写成平方与立方之比：求 1 到 10¹⁰⁰ 之间的整数 m 和 k，使 m² = k³ · n。任何这样的一对
都被接受。

时间限制：1 秒。内存限制：64 MB。

## 输入

整数 n。

## 输出

第一行是 m，第二行是 k。

## 检查

检查器接受任何 1 到 10¹⁰⁰ 之间、满足 m² = k³ · n 的 m 和 k。

## 样例

### 样例 1

输入：

```
18
```

输出：

```
12
2
```

### 样例 2

输入：

```
1
```

输出：

```
1
1
```

## 解法

取 k = n，m = n²。则 m² = n⁴ = n³ · n。所以这样的一对总是存在，这也是题目总有解的原因。`O(1)`。

注意事项：

- m 可达 10¹⁸，需要 64 位整数（测试 03）；
- 第一个样例给出的是更小的一对；任何正确的都被接受。

## 优化解法

优化的 Java 解法直接从 `System.in` 逐字节读入 n，而不是创建 `Scanner`；对只做一
次乘法的程序来说，`Scanner` 的正则表达式和区域设置数据才是主要开销。n² 不超过
10¹⁸，仍放得进 `long`：{1336_math_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1336_math_optimized.java`: 时间降低 +0.00%; 内存降低 +77.24%; 基础版本: `1336_math.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1336_math.cpp](1336_math.cpp).
- [1336_math.go](1336_math.go).
- [1336_math.rs](1336_math.rs).

- 五种解答都输出 n² 和 n。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1336_math.cpp](1336_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11285033 |
| [1336_math.go](1336_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB | 11285034 |
| [1336_math.java](1336_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1564 KB | 11285036 |
| [1336_math.py](1336_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 352 KB | 11285035 |
| [1336_math.rs](1336_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB | 11285038 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1336_math_optimized.java](1336_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 356 KB | 11304378 |
