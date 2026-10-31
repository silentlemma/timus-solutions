# 2102. 恰好二十个质因子

[Timus 2102](https://acm.timus.ru/problem.aspx?space=1&num=2102) · 难度 147 · number_theory

原题作者 Vladimir Leskov，出自 2016 年乌拉尔联邦大学青少年锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

判断 n 的质因数分解中指数之和是否恰好为 20，即 n 是否恰好是 20 个（计重数）质数之积。时间限制 2 秒，内存限制 64 MB。

## 输入

n（1 ≤ n ≤ 10¹⁸）。

## 输出

`Yes` 或 `No`。

## 样例

### 样例 1

输入：

```
2
```

输出：

```
No
```

### 样例 2

输入：

```
1048576
```

输出：

```
Yes
```

### 样例 3

输入：

```
10000000000
```

输出：

```
Yes
```

## 解法

用从 2 到 B = 2·10⁶ 的每个 d 去除 n（当 d² ≤ n 时），统计除掉的质因子数。若循环因 d² 超过剩余部分而停止，剩下的是 1 或质数，贡献 0 或 1。否则剩余部分至少为 B² = 4·10¹²，因此已除掉的部分至多 10¹⁸ / B²，小于 2¹⁸，即目前不到 18 个因子；剩余部分没有小于 B 的因子且至多 10¹⁸ < B³，所以至多再贡献两个。总数不可能达到 20，答案为 No。时间复杂度为 O(min(sqrt n, B))。

第三个样例中 10¹⁰ = 2¹⁰ · 5¹⁰ 有 20 个质因子。

## 优化解法

优化的 Java 解法从由 `System.in` 填充的 4 KB 缓冲区中手工解析 n，而不是创建
`Scanner`，这样 JVM 不必加载扫描器及其正则表达式；不超过 10¹⁸ 的 n 放得进
`long`，试除过程不变：{2102_number_theory_optimized.java}。

优化的 Python 解法倒数还需要的素因子个数，一旦答案确定就停止。比当前除数小的素数
都已除尽，所以剩下的因子都不小于当前除数：当还需要两个以上因子，而除数的这么多次
幂已超过 n 剩下的部分时，答案立即是 No，因此大素数 n 只需几次除法就结束。当至多
还需要两个因子时，已除去至少 18 个，剩下的部分至多 10¹⁸ / 2¹⁸，试除至多到它的平
方根结束，即不超过 1 953 125，不需要界 B。除过 2 之后只试奇数除数：
{2102_number_theory_optimized.py}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `2102_number_theory_optimized.java`: 时间降低 -12.00%; 内存降低 +74.87%; 基础版本: `2102_number_theory.java`.

- `2102_number_theory_optimized.py`: 时间降低 +41.50%; 内存降低 -9.28%; 基础版本: `2102_number_theory.py`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [2102_number_theory.rs](2102_number_theory.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2102_number_theory.cpp](2102_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 116 KB | 11304072 |
| [2102_number_theory.go](2102_number_theory.go) | Go 1.14 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.046 s | 1120 KB | 11294722 |
| [2102_number_theory.java](2102_number_theory.java) | Java 1.8 | number_theory | O(min(sqrt n, B)) | AC | 0.125 s | 1592 KB | 11304073 |
| [2102_number_theory.py](2102_number_theory.py) | Python 3.12 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.453 s | 388 KB | 11304074 |
| [2102_number_theory.rs](2102_number_theory.rs) | Rust 1.75 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 232 KB | 11294726 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2102_number_theory_optimized.java](2102_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(min(sqrt n, B)) | AC | 0.140 s | 400 KB | 11304532 |
| [2102_number_theory_optimized.py](2102_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.265 s | 424 KB | 11304531 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
