# 1330. 区间

[Timus 1330](https://acm.timus.ru/problem.aspx?space=1&num=1330) · 难度 95 · prefix_sums

原题作者 Den Raskovalov，出自 2004 年 10 月 16 日第十届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N ≤ 10 000 个传感器给出 −10 000 到 10 000 之间的整数读数。回答最多 100 000 个问题：第 i 到第 j 个传感器
（i ≤ j）读数之和。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

N，然后 N 个读数，然后 Q 和 Q 对 i, j。

## 输出

每行一个和。

## 样例

### 样例 1

输入：

```
5
1
2
3
-1
4
3
1 5
4 4
1 4
```

输出：

```
9
-1
5
```

## 解法

维护 before[i]，即前 i 个读数之和，before[0] = 0。从 i 到 j 的和就是 before[j] − before[i − 1]，每个问题
一次减法。`O(N + Q)`。

注意事项：

- 和在 −10⁸ 到 10⁸ 之间，32 位整数放得下；
- 可能根本没有问题（测试 03）；
- 有 100 000 个问题时，输入输出要大块读写，才能在 0.5 秒内完成。

## 优化解法

优化的 C++ 和 Java 解法用 32 位整数保存前缀和，这对 −10⁸ 到 10⁸ 之间的和已经足够。
C++ 通过 4 KB 的缓冲区手工解析数字、手工写出答案，并把前缀和放在静态数组中：
0.015 s，而不是 0.125 s；132 KB，而不是 2784 KB。

优化的 Java 解法按 4 KB 分块读入并手工解析，而不是使用 `StreamTokenizer`，答案写
进 4 KB 的字节缓冲区，而不是拼接字符串：0.125 s，而不是 0.156 s；452 KB，而不是
7324 KB。优化的 Python 解法逐行解析输入，而不是一次切分全部输入，并按每批 1024
行输出答案：1440 KB，而不是 27608 KB，但时间从 0.125 s 增加到 0.203 s。

## 各语言说明

- 简单的 Java 解法用能处理负数读数的 `StreamTokenizer` 读入，并把答案收集成一个
  字符串。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1330_prefix_sums.cpp](1330_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 2784 KB | 11284999 |
| [1330_prefix_sums.go](1330_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 2828 KB | 11285000 |
| [1330_prefix_sums.java](1330_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + Q) | AC | 0.156 s | 7324 KB | 11303461 |
| [1330_prefix_sums.py](1330_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 27608 KB | 11285001 |
| [1330_prefix_sums.rs](1330_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 3736 KB | 11285004 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1330_prefix_sums_optimized.cpp](1330_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(N + Q) | AC | 0.015 s | 132 KB | 11303598 |
| [1330_prefix_sums_optimized.java](1330_prefix_sums_optimized.java) | Java 1.8 | prefix_sums | O(N + Q) | AC | 0.125 s | 452 KB | 11303742 |
| [1330_prefix_sums_optimized.py](1330_prefix_sums_optimized.py) \* | Python 3.12 x64 | prefix_sums | O(N + Q) | AC | 0.203 s | 1440 KB | 11303743 |

\* 未进入当前评测机上该语言解法的前 10 名或前 15%，可能还能进一步优化。
