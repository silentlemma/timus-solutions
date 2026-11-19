# 1644. 一大堆核桃

[Timus 1644](https://acm.timus.ru/problem.aspx?space=1&num=1644) · 难度 100 · implementation

原题作者 Alexey Samsonov，出自 2008 年 10 月的乌拉尔国立大学中学生竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

鹦鹉做了 n 次实验，每次吃 3 到 9 个核桃，并记下自己是还饿还是吃饱了。饱足是单调的：吃得更多绝不会
更饿。已知十个核桃一定能吃饱，两个一定吃不饱。求一定能吃饱的最少核桃数，或指出记录互相矛盾。

## 输入

n（0 ≤ n ≤ 100），然后 n 行：核桃数以及 `hungry` 或 `satisfied`。

## 输出

一定能吃饱的最少核桃数，或 `Inconsistent`。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
4
4 hungry
7 satisfied
5 hungry
8 satisfied
```

输出：

```
7
```

### 样例 2

输入：

```
2
6 hungry
5 satisfied
```

输出：

```
Inconsistent
```

## 解法

取“饿”的最大数量（从 2 开始）和“饱”的最小数量（从 10 开始）。当且仅当后者更大时，记录与一个单调
阈值相符；此时答案就是“饱”的最小数量，因为更少的数量从未被证明能吃饱。否则输出 `Inconsistent`。
`O(n)`。

易错点：

- 没有记录时答案是 10（测试 03），只有“饿”的记录时答案仍是 10（测试 04）；
- 同一数量既记为饿又记为饱就是矛盾（测试 06）。

在 180 组随机记录上，答案与一个独立的已通过实现一致。

## 优化解法

`1644_implementation_optimized.py`. 保留 hungry 最大值与 full 最小值，初始为 2 和 10。直接处理 n 对数值/字节判定，不创建两个跨步切片。仅 full 严格大于 hungry 时输出 full。算法状态是两个极值，但仍保存切分输入：时间 O(n)、总空间 O(I)，I 为输入大小。 Accepted 行标明实际评测运行时及成对时间/内存。先 flush 输出，再以 os._exit(0) 跳过解释器清理；实测内存收益属于该运行时，不代表渐近加速。

与 `1644_implementation.py` 相比：时间 0.109 s → 0.156 s；内存 444 KB → 212 KB。

优化的 Java 解法从较小的缓冲区中手工解析数字，而不是使用 `Scanner`，并且只凭
首字母 `h` 或 `s` 区分两个单词，跳过其余字母：400 KB，而不是 1708 KB，时间不变。

优化的 C++ 解法用 `scanf` 读进一个小 `char` 数组，而不是使用 `iostream` 和
`std::string`，并按首字母区分两个单词：128 KB，而不是 388 KB，时间不变。

`1644_implementation_optimized.rs`. 只更新饥饿记录的最大值和饱足记录的最小值。题目给定的两个回答单词首字节不同，据此区分并跳过剩余记号，无需分配字符串。上界严格大于下界时区间才一致。时间 O(N)，额外状态 O(1)。 Rust 通过 C 运行库输入输出，避免完整的解码输入输出 String 和 Rust 格式化。简单且已通过评测的源代码保持不变。

与 `1644_implementation.rs` 相比：时间 0.015 s → 0.031 s；内存 220 KB → 64 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1644_implementation_optimized.py`：在该可比样本中，时间名次 53/53，内存名次 1/53。

`1644_implementation_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1644_implementation.cpp](1644_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 388 KB | 11303499 |
| [1644_implementation.go](1644_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1084 KB | 11288487 |
| [1644_implementation.java](1644_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1708 KB | 11288489 |
| [1644_implementation.py](1644_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 444 KB | 11288488 |
| [1644_implementation.rs](1644_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 220 KB | 11288490 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1644_implementation_optimized.cpp](1644_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303768 |
| [1644_implementation_optimized.java](1644_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 400 KB | 11303630 |
| [1644_implementation_optimized.rs](1644_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 64 KB | 11324867 |
| [1644_implementation_optimized.py](1644_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) time; O(I) space | AC | 0.156 s | 212 KB | 11325477 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
