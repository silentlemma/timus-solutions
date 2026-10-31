# 1082. 让快速排序恰好计数给定步数的输入

[Timus 1082](https://acm.timus.ru/problem.aspx?space=1&num=1082) · 难度 127 · constructive

原题作者 Nikita Shamgunov，出自 2001 年 3 月 4 日斯维尔德洛夫斯克州第三届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定的程序读入 `N` 个整数（`1 ≤ N ≤ 1000`）并用快速排序排序：以区间的第一个元素为基准，两个下标相向移动，
`j` 从右边在元素大于基准时移动，`i` 从左边在元素小于基准时移动，下标未交错时交换（Hoare 划分）。程序统计所有
调用中 `i` 和 `j` 的每一次移动，若总数恰好为 `(N² + 3N − 4)/2` 则获胜。输出 `N` 个绝对值不超过 `10^9` 的整数，
使它获胜。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`。

## 输出

用空格分隔的 `N` 个整数。

## 评测方式

接受任何满足要求的数。检查程序对输出执行同样的划分，并把计数与 `(N² + 3N − 4)/2` 比较。

## 样例

### 样例 1

输入：

```
3
```

输出：

```
1 2 3
```

## 题解

输出有序的数 `1, 2, …, N`。在长度为 `k`、基准位于左端的有序区间上，`j` 从右端一直走到基准，移动 `k` 次，`i`
移动一次到达基准；两者立即相遇，于是区间分成单独的基准和其余 `k − 1` 个仍然有序的元素。对从 `N` 到 2 的每个 `k`，
计数都是 `k + 1`：

`(N + 1) + N + … + 3 = (N² + 3N − 4)/2`，

正好是目标值。`O(N)`。

注意事项：

- 其他顺序会得到其他计数：对 `3 2 1`，程序计数 8 次移动而不是 7 次，因为交换改变了区间的划分方式；
- `N = 1` 时程序什么也不计数，目标值也是 0。

检查程序用显式栈模拟划分并比较计数。

## 优化解法

优化的 Java 解法直接从 `System.in` 逐字节读入 `N`，而不是创建 `Scanner`，后者的
正则表达式和区域设置数据比输出一千个数还费资源；输出与简单解法一样在一个
`StringBuilder` 中拼好：{1082_constructive_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1082_constructive_optimized.java`: 时间降低 -17.20%; 内存降低 +77.14%; 基础版本: `1082_constructive.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1082_constructive.cpp](1082_constructive.cpp).

- 各语言都输出用空格连接的 `1 … N`。

## 题解代码

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1082_constructive.cpp](1082_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 128 KB | 11279016 |
| [1082_constructive.go](1082_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 1116 KB | 11279017 |
| [1082_constructive.java](1082_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.093 s | 1592 KB | 11279019 |
| [1082_constructive.py](1082_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.062 s | 452 KB | 11279018 |
| [1082_constructive.rs](1082_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 252 KB | 11279020 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1082_constructive_optimized.java](1082_constructive_optimized.java) \* | Java 1.8 | constructive | O(N) | AC | 0.109 s | 364 KB | 11304423 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
