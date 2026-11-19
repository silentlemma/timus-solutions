# 1636. 罚时

[Timus 1636](https://acm.timus.ru/problem.aspx?space=1&num=1636) · 难度 61 · implementation

原题作者 Alex Samsonov，出自第十三届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

QXX 和 ZZZ 两队都做出了全部十道题；QXX 以罚时 T1 胜过 ZZZ 的 T2。每次被拒的提交加 20 分钟。
给出 ZZZ 在每道题上被拒的次数，判断没有这些罚时 ZZZ 能否获胜。罚时相同时按队名排序，所以 ZZZ
仍会是第二。

## 输入

第一行为 T1 和 T2（250 ≤ T1 ≤ T2 ≤ 2400），然后是 ZZZ 在十道题上被拒的次数。

## 输出

若这些被拒的提交让 ZZZ 失去第一，输出 `Dirty debug :(`，否则输出 `No chance.`。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
290 420
0 0 0 2 1 0 2 0 1 0
```

输出：

```
No chance.
```

### 样例 2

输入：

```
300 719
0 0 0 0 0 0 21 0 0 0
```

输出：

```
Dirty debug :(
```

## 解法

从 T2 中按每次被拒减去 20 分钟。只有严格少于 T1 时 ZZZ 才能获胜，因为平局时 QXX 按字母序在前。
`O(1)`。

易错点：

- 去掉罚时后相等仍然是输（测试 03），少一分钟就是赢（测试 04）；
- 答案末尾的句点和哭脸都是期望输出的一部分。

在 100 个随机测试上，答案与一个独立的已通过实现一致。

## 优化解法

优化的 Java 解法直接从 `System.in` 逐字节解析数字，而不是使用 `Scanner`：
368 KB，而不是 1600 KB，时间不变。

`1636_implementation_optimized.py`. 保留严格比较 T2-20*sum(rejections)<T1，相等仍输出 No chance。通过 map 读取整数字节记号，用 sum 直接消费剩下十个次数，避免单独的 attempts 整数列表和解码输入。P=10 个次数时工作量 O(P)，仍有解析记号存储。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1636_implementation.py` 相比：时间 0.078 s → 0.109 s；内存 428 KB → 216 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1636_implementation_optimized.py`：在该可比样本中，时间名次 62/80，内存名次 1/80。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1636_implementation.cpp](1636_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 116 KB | 11303772 |
| [1636_implementation.go](1636_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB | 11288447 |
| [1636_implementation.java](1636_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1600 KB | 11288449 |
| [1636_implementation.py](1636_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 428 KB | 11288448 |
| [1636_implementation.rs](1636_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 244 KB | 11303773 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1636_implementation_optimized.java](1636_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.093 s | 368 KB | 11303765 |
| [1636_implementation_optimized.py](1636_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(P), P=10 | AC | 0.109 s | 216 KB | 11325073 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
