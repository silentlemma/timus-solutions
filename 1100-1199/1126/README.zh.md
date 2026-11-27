# 1126. 每个由 M 个连续读数组成的窗口的最大值

[Timus 1126](https://acm.timus.ru/problem.aspx?space=1&num=1126) · 难度 92 · two_pointers

原题作者 Alexander Mironenko，出自 2001 年 10 月 21 日第六届乌拉尔国立大学大学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定窗口宽度 `M`（`2 ≤ M ≤ 14000`）和以 `-1` 结尾的 `N` 个读数（`M ≤ N ≤ 25000`，每个在 0 到 100000 之间），依次输出读数
`1..M`、`2..M+1`……直到最后一个完整窗口的最大值。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

`M`，然后每行一个读数，最后是 `-1`。

## 输出

`N − M + 1` 个窗口最大值，每行一个。

## 评测方式

输出按记号逐个比较；多余的空白字符无关紧要。

## 样例

### 样例 1

输入：

```
3
10
11
10
0
0
0
1
2
3
2
-1
```

输出：

```
11
11
10
0
1
2
3
3
```

## 解法

维护一个双端队列，存放下标，其对应的值从队头到队尾递减。新读数先从队尾移除所有值不大于它的下标——只要新读数还在窗口中，它们就不可能增大最大值；然后把它加到队尾。队头在离开窗口时出队。队头始终是当前窗口的最大值。每个下标最多进出各一次，所以整个扫描是
`O(N)`；对每个窗口重新计算则要 `O(N·M)`，最多约 1.56 亿步。

所有简单版都保留 N 个读数。活跃双端队列占 O(M)，但 Go/Java
用移动头的 O(N) 后备数组，过期前缀不会使容量降为 O(M)。
C++/Java/Python/Rust 累计 P 字节输出或答案及格式化结果，Go
流式写出。Python 解析峰值含 I 字节/记号及整数列表和 values
切片；Rust 保留 I 字节输入 String。相应总量为 O(N+I+P)。
流式优化 C++/Java/Rust 和紧凑 Python 使用 O(M) 队列及有界
输入输出缓冲。优化 Go 仍存所有读数及 N 容量队列，占 O(N)。

注意事项：

- 读数以 `-1` 结束，而不是给出个数；
- 相等的读数可以从队尾全部移除，只留最新的那个，它最后离开窗口；
- `M = N` 时只有一个窗口。

答案经过验证：在所有测试上与直接计算每个窗口最大值的程序比对。

## 优化解法

`1126_two_pointers_optimized.py`. 保留单调双端队列，每项改为单个整数 (value<<15)|index；N<=25000，15 位足够存下标。整数顺序先比较值再比较新旧，因此新出现的相等值替代旧值。移除过期队首和受支配队尾，用 >>15 取最大值。每项至多入队、出队一次，摊还 O(N) 时间、O(M) 项存储。4096 字节输入保留半截 token，512 个答案一批输出限制临时存储。main 内直接写出并 os._exit(0)，避免正常清理。保留易读的二元组教学版。

当前精确 Python 3.12 Accepted #11327503：0.093 s / 1452 KB。
2026-11-20 两项 2/54 名次属于历史记录；当前政策缓存审计确认
适用的两项指标。没有独立第一名目标，该表行没有星号，使用
统一[标准](../../RATING_CRITERIA.md)。

- `1126_two_pointers_optimized.py`: 0.093 s / 1452 KB; 保留教学基础版 `1126_two_pointers.py`: 0.14 s / 3448 KB.

历史 CPython 修订 #11326680 为 0.109 s / 2152 KB，保存的
时间/内存名次 6/54、4/54 属于该修订，不是当前 #11327503。
Python 没有独立第一名目标。

更早 Python 修订 #11303710 为 0.125 s / 668 KB；中间修订
#11326680（0.109 s / 2152 KB）相差一个显示刻度。当前
#11327503 为 0.093 s / 1452 KB。这是三个独立运行/修订，
测量对不混合，准入绑定当前源码，不能把所有差异都说成一刻度。

优化解法（C++、Java）不保存读数：每个读数一读入就连同下标一起进入双端
队列，窗口满时立即输出最大值。C++ 用 `getchar` 读取；Java 手工解析字节缓冲区，
用 `M` 个单元的环形缓冲区存放双端队列（窗口里不会超过这么多），并通过字节
缓冲区输出数字。C++：224 KB，而不是 776 KB，时间不变。Java：0.109 s，而不是
0.156 s；624 KB，而不是 2332 KB。

Rust 用 4 KB 输入缓冲及有界写出，不保留完整输入/输出文本。
实际为 0.031 s / 332 KB，基础版为 0.046 s / 1192 KB，
时间并不相同。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1126_two_pointers_parsing_implementation_optimized.go`. 词元转换及数值输出按实际类型专门化，移除未使用的通用分支，保留算法和注释。 使用可补充的 8192 字节输入缓冲，避免保留完整输入，保持词元及部分读取、EOF 的语义。

优化 Go 补充 8192 字节原始输入缓冲，但仍把全部读数放入
values 并预留 N 个队列下标。它改变字节解析及输出转换，
不使窗口算法流式化；读数和队列仍占 O(N)。

Accepted #11328910 (Go 1.14 x64): **0.031 s / 2344 KB**. 历史对照: `1126_two_pointers.go` (Go 1.14 x64) — 0.062 s / 2896 KB (#11279328).

当前优化 Go 修订仅命名原有 128 字节内联记号容量。Accepted
#11328910（0.窗口存储、解析数值、简单版和实质注释
均不变。

## 各语言说明

- 在简单解法中，Go 和 Java 用带移动队头的数组实现队列；C++、Rust 和 Python 使用
  库中的双端队列。

上述源码修订均已取得各自的 Accepted。解答表列出与最终源码对应的提交编号及同次运行的时间和内存；较早的观察对应此前的修订。所有有教学价值的简单实现均保留。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1126_two_pointers.cpp](1126_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 776 KB | 11279323 |
| [1126_two_pointers.go](1126_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N) | AC | 0.062 s | 2896 KB | 11279328 |
| [1126_two_pointers.java](1126_two_pointers.java) | Java 1.8 | two_pointers | O(N) | AC | 0.156 s | 2332 KB | 11279331 |
| [1126_two_pointers.py](1126_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N) | AC | 0.14 s | 3448 KB | 11279329 |
| [1126_two_pointers.rs](1126_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.046 s | 1192 KB | 11279332 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1126_two_pointers_optimized.cpp](1126_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 224 KB | 11303561 |
| [1126_two_pointers_optimized.java](1126_two_pointers_optimized.java) | Java 1.8 | two_pointers | O(N) | AC | 0.109 s | 624 KB | 11303563 |
| [1126_two_pointers_optimized.py](1126_two_pointers_optimized.py) | Python 3.12 x64 | two_pointers | O(N) amortized; O(M) deque + bounded buffers | AC | 0.093 s | 1452 KB | 11327503 |
| [1126_two_pointers_optimized.rs](1126_two_pointers_optimized.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.031 s | 332 KB | 11303711 |
| [1126_two_pointers_parsing_implementation_optimized.go](1126_two_pointers_parsing_implementation_optimized.go) | Go 1.14 x64 | two_pointers, parsing, implementation | O(N) | AC | 0.031 s | 2356 KB | 11330993 |
