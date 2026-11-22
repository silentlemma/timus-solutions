# 1494. 单袋台球

[Timus 1494](https://acm.timus.ru/problem.aspx?space=1&num=1494) · 难度 90 · simulation

原题作者 Alex Samsonov，出自 2006 年 10 月 14 日第十三届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

球 1、2、…、N（1 ≤ N ≤ 100000）应当按这个顺序打进唯一的球袋。检查员不时从袋中取
出最后进袋的球，最后把所有球都取了出来。给定检查员取球的顺序，若球不可能按正确顺
序打进，输出 "Cheater"，否则输出 "Not a proof"。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是检查员取出的 N 个球的顺序。

## 输出

"Cheater" 或 "Not a proof"。

## 样例

### 样例 1

输入:

```
2
2
1
```

输出:

```
Not a proof
```

### 样例 2

输入:

```
3
3
1
2
```

输出:

```
Cheater
```

## 解法

球袋就是一个栈：球按 1、2、…、N 放入，检查员总是取最上面的球。模拟这个过程：按顺
序打进球，每打进一个，只要袋顶的球正是检查员列表中的下一个，就把它取出。等待不会
有帮助，因为不在顶上的球在它上面的球全部取走前一直被压着。若整个列表都能这样取出，
这个顺序就是可能的。`O(N)`。

注意事项：

- 压在后进的球下面的球不能先出来：3、4、1、2 是不可能的（测试 02、05）；
- 全部到最后才取出时顺序是倒过来的，每个都立即取出时顺序不变；两者都可能（gen4、
  gen5）；
- 在真实的一局中交换两个球，通常就足以使其变得不可能（gen3）。

## 优化解法

`1494_bitmask_simulation.py`. 用有序非空 32 位包表示待取球栈，不给每球一个整数槽。新最大值只插入跳过范围；旧球须等于最后包的最高置位后才能删除。索引与掩码合存，不逐步复制 N 位整数，也不扫描空字。N<=100000 时包适合 44 位；总时间 O(N)，O(ceil(N/32)) 包加 4096 字节 token 输入。确定性 bitmask_simulation 不同于保留的显式栈。当前指标来自 PyPy，旧栈的 CPython Accepted 保持独立配对。

精确源码：PyPy 3.10 x64 Accepted #11327514: 0.14 s / 3764 KB。2026-11-20 保存的编译器组排名，时间然后内存：20/164; 1/164。严格收录采用达到 1024 KB 时要求时间和内存：前十或前 15%，同值共享名次，百分比向上取整。单独语言目标为两项第一，故保留星号。保留的旧版本有自己的配对指标 #11326685 (Python 3.12 x64): 0.14 s / 4160 KB，不混合测量或运行时。教学源码保持不变。

- `1494_bitmask_simulation.py`: 0.14 s / 3764 KB; 保留教学版 `1494_simulation.py` (Python 3.12 x64): 0.14 s / 15568 KB.

`1494_simulation_optimized.py`. 读取每个观察球时模拟球袋：将尚未进入的连续球推入至该球，随后要求栈顶正是它；首次矛盾即结束。栈改为预分配 N 格 Python 列表，不再访问紧凑无符号数组。每球最多入栈、出栈一次，时间 O(N)，空间 O(N) 加当前行记号。不另存输入顺序，保留普通易读模拟。

精确源代码 CPython 3.12 Accepted #11326685：0.14 s / 4160 KB。2026-11-20 保存的当前编译器比较：时间排名 20/164，内存排名 1/164。两项必需指标均通过严格前十或前 15%（百分比界限向上取整）。星号表示 Python 单独的双指标第一名目标。

此前记录的优化提交 #11303753（Python 3.12 x64）为 0.171 s / 832 KB。当前 CPython 3.12 记录时间更低、内存更高。这是不同评测运行的成对测量，比较包含解释器选择及运行波动。

- `1494_simulation_optimized.py`: 0.14 s / 4160 KB; 保留教学基础版 `1494_simulation.py` (Python 3.12 x64): 0.14 s / 15568 KB.

优化解法一边读一边模拟球袋：对每个被取出的球，先把编号不超过它的球依次滚入，然后 袋口的球必须正是它，第一次不符就结束程序。因此不存储球的顺序；球袋用数组当作栈。 C++ 用 `getchar` 解析数字（0.031 s，而不是 0.093 s；512 KB，而不是 1540 KB），Go 手工解析数字，输出不使用 `fmt`，球袋是预先分配的 `int32` 数组，因为球号不超过 100 000（1312 KB，而不是 7684 KB，时间不变），Java 按 4 KB 分块读入并手工解析， 而不是用 `StreamTokenizer`（844 KB，而不是 1300 KB，时间不变），Rust 从 4 KB 缓冲区手工解析（604 KB，而不是 2704 KB，时间不变）。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1494_simulation.cpp](1494_simulation.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.093 s | 1540 KB | 11287211 |
| [1494_simulation.go](1494_simulation.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.062 s | 7684 KB | 11303301 |
| [1494_simulation.java](1494_simulation.java) | Java 1.8 | simulation | O(N) | AC | 0.109 s | 1300 KB | 11303468 |
| [1494_simulation.py](1494_simulation.py) | Python 3.12 x64 | simulation | O(N) | AC | 0.140 s | 15568 KB | 11287213 |
| [1494_simulation.rs](1494_simulation.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.031 s | 2704 KB | 11287216 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1494_simulation_optimized.cpp](1494_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.031 s | 512 KB | 11303751 |
| [1494_simulation_optimized.go](1494_simulation_optimized.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.046 s | 1312 KB | 11303612 |
| [1494_simulation_optimized.java](1494_simulation_optimized.java) | Java 1.8 | simulation | O(N) | AC | 0.125 s | 844 KB | 11303752 |
| [1494_simulation_optimized.py](1494_simulation_optimized.py) \* | Python 3.12 x64 | simulation | O(N) time and space | AC | 0.14 s | 4160 KB | 11326685 |
| [1494_bitmask_simulation.py](1494_bitmask_simulation.py) \* | PyPy 3.10 x64 | bitmask, simulation | O(N) time; O(ceil(N/32)) packets + fixed buffer | AC | 0.14 s | 3764 KB | 11327514 |
| [1494_simulation_optimized.rs](1494_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.015 s | 604 KB | 11303754 |

\* 已通过评测；尚未达到单独排名目标：C++ 要求时间和内存均为前十或前 15%，其他语言类别要求两项均第一。此标记与收录条件分开，该版本仍可进一步优化。
