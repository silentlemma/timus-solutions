# 1407. 一二，一二

[Timus 1407](https://acm.timus.ru/problem.aspx?space=1&num=1407) · 难度 388 · constructive

原题作者 Sergey Pupyrev，出自 2005 年 10 月 15 日第十二届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对 1 ≤ N ≤ 100，输出一个至多 10 000 位、只由数字 1 和 2 组成且能被 2ᴺ 整除的数，
若不存在则输出 "No solution"。

时间限制：1 秒。内存限制：64 MB。

## 输入

数 N。

## 输出

这样一个数；任何一个都被接受。

## 评测方式

检查器接受任意长度为 1 到 10000 位、仅由数字 1 和 2 组成且能被 `2^N` 整除的数，并拒绝多余输出。

## 样例

### 样例 1

输入:

```
2
```

输出:

```
12
```

## 解法

总存在恰好 N 位的这样的数，从右往左构造。设 aₖ 由 k 位 1 和 2 组成且能被 2ᵏ
整除；在前面添上数字 d：d·10ᵏ + aₖ = 2ᵏ·(d·5ᵏ + aₖ / 2ᵏ)。由于 5ᵏ 是奇数，
d = 1 和 d = 2 中恰有一个使括号内为偶数，于是 aₖ₊₁ 能被 2ᵏ⁺¹ 整除。从空数开
始重复 N 次。Go/Java 为 `O(N²)`，Python 为 `O(N³)`。

选择只取决于最低的 N + 1 位，所以 C++ 和 Rust 用 128 位保存这个数并允许求和
溢出回绕；Go 和 Java 用大整数并查看最低的置位。

注意事项：

- 答案永远不会是 "No solution"；
- 2¹⁰⁰ 远超 64 位（测试 07 到 09）。

检查了从 1 到 100 的每个 N：得到的数由 N 位 1 和 2 组成且能被 2ᴺ 整除。由于
N 位的答案唯一，测试按精确比较判定。

## 优化解法

`1407_constructive_optimized.java`. Java 保留从右到左的构造规则：已有 k 位时，当前值的第 k 位为零则选择数字 2，否则选择 1。与教学 BigInteger 版不同，此文件用两对 long 分别保存当前值和十的幂，按 2^128 取模。N<=100 时所有查询位均保留；无符号进位及拆为 32 位半字的乘十实现精确模运算。数字直接写入 N+1 字节答案。此有限范围内时间 O(N)、答案存储 O(N)、算术状态 O(1)，并不声称任意 N 都能使用固定宽度算术。保留教学源代码。

精确源代码 Java 1.8 Accepted #11327478：0.093 s / 312 KB。2026-11-20 保存的编译器组比较：时间 5/44、内存 1/44。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11324811 为 0.125 s / 524 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1407_constructive_optimized.java`: 0.093 s / 312 KB; 保留教学基础版 `1407_constructive.java`: 0.109 s / 1668 KB.

`1407_constructive_optimized.py`. 仍从低位到高位构造。完成 k 位后数值可被 2^k 整除，因 10^k/2^k 为奇数，第 k 位决定选 1 还是 2，去掉两次试探取模。答案用 bytearray，最后反转一次。整数增长至 O(n) 位，因此为 O(n²) 位运算、O(n) 位及数字存储，不声称固定字长下线性时间。 Accepted 行标明实际评测运行时及成对时间/内存。先 flush 输出，再以 os._exit(0) 跳过解释器清理；实测内存收益属于该运行时，不代表渐近加速。

与 `1407_constructive.py` 相比：时间 0.078 s → 0.125 s；内存 416 KB → 244 KB。

Go 和 Rust 从右向左构造答案，按模 2¹²⁸ 保存当前值和下一个十的幂。已有 k 位时最低 k 位二进制位均为零，因此第 k 位决定下一位十进制数字是一还是二。只有最低 N ≤ 100 位相关。Go 用两个 64 位字实现 128 位运算，Rust 使用 u128 的回绕运算。Go 直接从小型可复用字节缓冲区读取指数，并直接输出构造出的数字，不做字符串转换。

通过评测的 Go 1.14 x64 版本耗时 0.031 秒，基础版为 0.015 秒，内存为 784 KB，基础版为 1140 KB。

已通过评测的基础实现 [1407_constructive.cpp](1407_constructive.cpp), [1407_constructive.java](1407_constructive.java), [1407_constructive.py](1407_constructive.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1407_constructive_optimized.java`：在该可比样本中，时间名次 32/44，内存名次 3/44。

`1407_constructive_optimized.py`：在该可比样本中，时间名次 22/27，内存名次 1/27。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1407_constructive.cpp](1407_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 188 KB | 11286054 |
| [1407_constructive.go](1407_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.015 s | 1140 KB | 11286055 |
| [1407_constructive.java](1407_constructive.java) \* | Java 1.8 | constructive | O(N^2) | AC | 0.109 s | 1668 KB | 11286057 |
| [1407_constructive.py](1407_constructive.py) \* | Python 3.12 x64 | constructive | O(N^3) | AC | 0.078 s | 416 KB | 11286056 |
| [1407_constructive.rs](1407_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 216 KB | 11286058 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1407_constructive_optimized.go](1407_constructive_optimized.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 784 KB | 11311119 |
| [1407_constructive_optimized.rs](1407_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.015 s | 188 KB | 11310807 |
| [1407_constructive_optimized.java](1407_constructive_optimized.java) | Java 1.8 | constructive | O(N) time; O(N) answer space | AC | 0.093 s | 312 KB | 11327478 |
| [1407_constructive_optimized.py](1407_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(n²) bit work; O(n) bits | AC | 0.125 s | 244 KB | 11325484 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
