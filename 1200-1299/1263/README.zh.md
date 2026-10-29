# 1263. 选举

[Timus 1263](https://acm.timus.ru/problem.aspx?space=1&num=1263) · 难度 42 · implementation

原题作者 Den Raskovalov，出自 2003 年 10 月 11 日斯维尔德洛夫斯克州中学生公开团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 N 名候选人（1 ≤ N ≤ 10 000）和 M 名选民（1 ≤ M ≤ 10 000）；每名选民投给一名候选人。
对每名候选人，输出其得票占比的百分数，保留小数点后两位并带 `%` 号。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 M，然后是 M 个 1 到 N 之间的候选人编号。

## 输出

N 行百分数。

## 样例

### 样例 1

输入：

```
3 6
1
2
3
2
1
1
```

输出：

```
50.00%
33.33%
16.67%
```

## 解法

统计每名候选人的票数，输出保留两位小数的 100 · 票数 / M。`O(N + M)`。

注意事项：

- 没有得票的候选人也要输出一行 `0.00%`（测试 03）；
- 占比可能恰好落在最后一位的一半上，例如 1/32 = 3.125%（测试 04、05）。这些解答像 C 的
  `printf` 一样把这种情况舍入到偶数：3.12%；
- N = 10 000 时，某些语言逐行输出很慢：先把输出收集起来。

## 优化解法

优化的 Python 解法通过生成器逐行读取选票，而不是一次性切分全部输入；每种不同的票
数只格式化一次百分比，票数相同的候选人共用同一行结果。各行通过带缓冲的
`sys.stdout.write` 逐行输出，而不是先拼接起来：856 KB，而不是 1948 KB，时间不变。

优化的 C++ 解法用 `getchar` 而不是 `scanf` 解析数字，并用定长的 16 位计数器数组
计票：128 KB，而不是 252 KB，时间不变。优化的 Rust 解法从加锁标准输入的字节中手
工解析数字，而不是把整个输入读成字符串，用 16 位计数器计票，并通过 1 KB 的带缓冲
写入器输出：252 KB，而不是 468 KB，时间不变。

## 各语言说明

- C++、Go、Python 和 Rust 直接格式化 double；四者都对 double 的精确值按“半数取偶”舍入。
- Java 的 `String.format` 是“半数进位”，所以 Java 对同一个 double 取 `BigDecimal`，并用
  `HALF_EVEN` 舍入。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1263_implementation.cpp](1263_implementation.cpp) | G++ 13.2 x64 | implementation | O(N + M) | AC | 0.031 s | 252 KB | 11284152 |
| [1263_implementation.go](1263_implementation.go) | Go 1.14 x64 | implementation | O(N + M) | AC | 0.031 s | 1456 KB | 11284153 |
| [1263_implementation.java](1263_implementation.java) | Java 1.8 | implementation | O(N + M) | AC | 0.156 s | 5696 KB | 11284158 |
| [1263_implementation.py](1263_implementation.py) | Python 3.12 x64 | implementation | O(N + M) | AC | 0.078 s | 1948 KB | 11284154 |
| [1263_implementation.rs](1263_implementation.rs) | Rust 1.75 x64 | implementation | O(N + M) | AC | 0.015 s | 468 KB | 11284161 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1263_implementation_optimized.cpp](1263_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(N + M) | AC | 0.031 s | 128 KB | 11303730 |
| [1263_implementation_optimized.py](1263_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N + M) | AC | 0.078 s | 856 KB | 11303586 |
| [1263_implementation_optimized.rs](1263_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N + M) | AC | 0.015 s | 252 KB | 11303731 |

\* 未进入当前评测机上该语言解法的前 10 名或前 15%，可能还能进一步优化。
