# 1683. 冰箱

[Timus 1683](https://acm.timus.ru/problem.aspx?space=1&num=1683) · 难度 137 · greedy

原题作者 Stanislav Vasilyev，出自 2009 年 2 月 28 日第十届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把宽 1 厘米、长 n 厘米的纸条折成 1 × 1 厘米、共 n 层的方块。每次折叠都从左端量出整数厘米，
把这一段向右翻折，于是左端移动了这个长度。求最少的折叠次数以及每次量出的长度。

## 输入

n（1 ≤ n ≤ 10⁹）。

## 输出

折叠次数，然后按顺序给出量出的长度。任何最短的序列都可以。

## 评测方式

仓库使用语义检查器，接受满足以下条件的任意输出。 仓库检查器要求与参考相同的最优次数及恰好这么多个整数折长。每个 x 须满足1<=x<=current-x，再令 current 减 x，最终长度须为一。任意合法最短序列均有效。

## 样例

### 样例 1

输入：

```
12
```

输出：

```
4
5 3 2 1
```

## 解法

长为 L 的纸条只有在翻过去的部分能放在剩余部分上时，即 x ≤ L − x，才能折 x 厘米，
此后剩下长度 L − x ≥ ⌈L / 2⌉。所以每次折叠至多把纸条减半（向上取整），
而每次折 ⌊L / 2⌋ 恰好做到这一点：折叠次数是满足 2ᵐ ≥ n 的最小 m。`O(log n)`。

注意事项：

- n = 1 不需要折叠：输出 0 和一个空列表；
- 样例中的 5 3 2 1 只是众多答案之一，所以检查器比较次数并重放每次折叠。

检查器重放每次折叠，并把次数与贪心的结果比较。

## 优化解法

`1683_greedy_optimized.java`. 保留最优反复半折。1≤N≤10^9 时 ceil(log2 N)=32−numberOfLeadingZeros(N−1)，N=1 为零折。长度容于 int，至多三十个值容于完整 384 字节答案。原地编码数字，一次输出并 flush 后 System.exit(0)，无需字符串构造或通用 long 输出缓冲。O(log N) 折叠、有界辅助空间。当前 0.078 s/452 KB 与旧 0.093 s/452 KB 为不同配对；一计时刻度本身不证明 30% 提升。教学源码及 Python 运行时选择证据不变。

精确源代码 Java 1.8 Accepted #11327867：0.078 s / 452 KB。2026-11-20 保存的编译器组比较：时间 1/62、内存 5/62。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11304448 为 0.093 s / 452 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1683_greedy_optimized.java`: 0.078 s / 452 KB; 保留教学基础版 `1683_greedy.java`: 0.125 s / 1664 KB.

`1683_greedy_optimized.py` 逐字节复用，不增加源文件，也不引入新算法。精确源代码的 CPython 3.12 Accepted #11327033 为 0.062 s / 620 KB。2026-11-20 保存的当前 Python 语言族编译器组中，时间排名 1/21、内存排名 21/21。本次内存低于 1024 KB，因此严格前十名或前 15% 标准只看时间；星号仍表示单独的语言排名目标。同一未改动文件另有早先的 PyPy 3.10 Accepted #11324922：0.125 s / 208 KB。这些是不同运行各自成对的指标：选择 CPython 的时间与排名，PyPy 的内存更低。本节早先的省内存说明指此 PyPy 测量，不是 CPython 表格行。全部教学源代码保持不变。

`1683_greedy_optimized.py`. 保留从左折 floor(length/2)，剩 ceil(length/2)。合法折叠不可能缩得更快，因此最少次数 ceil(log2 n)，n=1 为零次。n<=10^9 下共 O(log n) 次有界整数步骤。 先用 (n-1).bit_length() 求次数，再生成长度；仍保存并连接所有折叠字符串，因此额外输出空间为 O(log n)。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1683_greedy.py` 相比：时间 0.125 s → 0.125 s；内存 372 KB → 208 KB。

`1683_greedy_optimized.rs`. 保留从左折 floor(length/2)，剩 ceil(length/2)。合法折叠不可能缩得更快，因此最少次数 ceil(log2 n)，n=1 为零次。n<=10^9 下共 O(log n) 次有界整数步骤。 先一遍减半计数，再重复同样步骤直接输出，避免 Vec<String> 和拼接输出：额外状态 O(1)，两遍各 O(log n)。 Rust 版本通过 C 运行库读写，不保留解码后的输入 String，也不构造格式化的输出 String。保留简单版本及其 Accepted。

与 `1683_greedy.rs` 相比：时间 0.015 s → 0.062 s；内存 244 KB → 52 KB。

优化的 C++ 解法把各次折叠放在栈上 30 个数的固定数组里，而不是不断增长的
`std::vector`。因为 n ≤ 10⁹ < 2³⁰，最多对半折 30 次纸条就只剩 1 厘米，所以数组总
够用，程序本身也不在堆上分配内存：{1683_greedy_optimized.cpp}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1683_greedy_optimized.cpp`: 时间降低 +0.00%; 内存降低 +47.92%; 基础版本: `1683_greedy.cpp`.

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

早先的 PyPy 比较：`1683_greedy_optimized.py`：在该可比样本中，时间名次 18/21，内存名次 1/21。

`1683_greedy_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy.cpp](1683_greedy.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 192 KB | 11288846 |
| [1683_greedy.go](1683_greedy.go) | Go 1.14 x64 | greedy | O(log n) | AC | 0.031 s | 1096 KB | 11288848 |
| [1683_greedy.java](1683_greedy.java) | Java 1.8 | greedy | O(log n) | AC | 0.125 s | 1664 KB | 11288850 |
| [1683_greedy.py](1683_greedy.py) | Python 3.12 x64 | greedy | O(log n) | AC | 0.125 s | 372 KB | 11288849 |
| [1683_greedy.rs](1683_greedy.rs) | Rust 1.75 x64 | greedy | O(log n) | AC | 0.015 s | 244 KB | 11288851 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy_optimized.cpp](1683_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 100 KB | 11304447 |
| [1683_greedy_optimized.java](1683_greedy_optimized.java) \* | Java 1.8 | greedy | O(log N) time; bounded 384-byte answer | AC | 0.078 s | 452 KB | 11327867 |
| [1683_greedy_optimized.py](1683_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(log n) | AC | 0.062 s | 620 KB | 11327033 |
| [1683_greedy_optimized.rs](1683_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(log n) | AC | 0.062 s | 52 KB | 11325142 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
