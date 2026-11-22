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

`1082_constructive_optimized.java`. 保留使快速排序达到所需最坏情形的递增 1..N 构造。用复用数位数组和 4096 字节输出缓冲逐数输出，不建立完整 StringBuilder。工作量与输出数位数成正比，O(N log N)；辅助输出空间固定。保留构造证明和教学源代码。

精确源代码 Java 1.8 Accepted #11327337：0.078 s / 336 KB。2026-11-20 保存的编译器组比较：时间 1/165、内存 1/165。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。两项均第一，也满足单独语言目标，无需星号。此前记录的优化运行 #11304423 为 0.109 s / 364 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1082_constructive_optimized.java`: 0.078 s / 336 KB; 保留教学基础版 `1082_constructive.java`: 0.093 s / 1592 KB.

Python 优化版输出同一有序序列，每批最多 128 个数，从而限制临时字符串的大小。

### 实测改进

每个优化版本均已获 Accepted，并且符合排名条件，或相对基础版本减少至少 30% 的时间或内存。基础源代码均保留。星号只表示尚未达到排名目标。

- `1082_constructive_optimized.py` 使用 440 KB，基础版本使用 452 KB；用时从 0.062 秒增至 0.078 秒。在 2026 年 11 月 16 日的现行 Python/PyPy 解释器排名中，45 个结果中时间排第 4，内存排第 12。两项均进入前 30%，且内存排名优于基础版本的第 15 名。

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
| [1082_constructive_optimized.java](1082_constructive_optimized.java) | Java 1.8 | constructive | O(N log N) time; O(1) auxiliary space | AC | 0.078 s | 336 KB | 11327337 |
| [1082_constructive_optimized.py](1082_constructive_optimized.py) \* | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 440 KB | 11307455 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
