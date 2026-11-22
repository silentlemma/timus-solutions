# 1785. 本地化之难

[Timus 1785](https://acm.timus.ru/problem.aspx?space=1&num=1785) · 难度 16 · implementation

原题为民间流传的题目，出自 2010 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

某游戏用一个词而不是数字来表示军队规模：1–4 为 "few"，5–9 为 "several"，10–19 为 "pack"，20–49 为 "lots"，
50–99 为 "horde"，100–249 为 "throng"，250–499 为 "swarm"，500–999 为 "zounds"，1000 及以上为 "legion"。
给定怪物数量，输出对应的词。

## 输入

n（1 ≤ n ≤ 2000）。

## 输出

n 对应的词。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
7
```

输出：

```
several
```

### 样例 2

输入：

```
40
```

输出：

```
lots
```

## 解法

把各区间的下界从大到小（1000、500、250、100、50、20、10、5、1）和对应的词放在一起。跳过大于 n 的下界，第一个不大于 n 的下界给出答案。`O(1)`。

样例中 7 依次越过 1000 到 10，停在 5，即 "several"；40 停在 20，即 "lots"。

注意事项：

- 下界属于较大的那个词：5 是 "several"，1000 是 "legion"；
- 从 1000 到 2000 的所有 n 都是 "legion"。

在 1 到 2000 的每个 n 上，答案都与一个独立的已通过实现一致。

## 优化解法

`1785_implementation_optimized.py` 逐字节复用，不增加源文件，也不引入新算法。精确源代码的 CPython 3.12 Accepted #11327034 为 0.078 s / 704 KB。2026-11-20 保存的当前 Python 语言族编译器组中，时间排名 18/582、内存排名 494/582。本次内存低于 1024 KB，因此严格前十名或前 15% 标准只看时间；星号仍表示单独的语言排名目标。同一未改动文件另有早先的 PyPy 3.10 Accepted #11325075：0.14 s / 196 KB。这些是不同运行各自成对的指标：选择 CPython 的时间与排名，PyPy 的内存更低。本节早先的省内存说明指此 PyPy 测量，不是 CPython 表格行。全部教学源代码保持不变。

`1785_implementation_optimized.go`. 保留九个固定军队名区间及包含式下界，用递减条件分支替代并行阈值、名称数组及下标查找，取首个匹配，含边界5,10,20,50,100,250,500,1000。不引入通用排序或搜索。输入1..2000、固定九种情况使时间和状态均为 O(1)，单词拼写不变。 可移植的 os.Stdin.Read/os.Stdout.Write 与直接整数转换使用各 4096 字节的固定输入输出缓冲区。重复使用输出缓冲区前会处理部分写入。保留原有简单 Accepted 版本。

与 `1785_implementation.go` 相比：时间 0.031 s → 0.015 s；内存 1080 KB → 796 KB。

`1785_implementation_optimized.py`. 保留九个固定军队名区间及包含式下界，用递减条件分支替代并行阈值、名称数组及下标查找，取首个匹配，含边界5,10,20,50,100,250,500,1000。不引入通用排序或搜索。输入1..2000、固定九种情况使时间和状态均为 O(1)，单词拼写不变。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1785_implementation.py` 相比：时间 0.093 s → 0.14 s；内存 424 KB → 196 KB。

优化的 C++ 解法在同一张表中查找单词，但用 `scanf` 读入、用 `puts` 输出，而不是
`iostream`：116 KB，而不是 376 KB，时间不变。

优化的 Java 解法直接从 `System.in` 逐字节解析数字，而不是使用 `Scanner`：0.093 s，
而不是 0.125 s；340 KB，而不是 1600 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1785_implementation_optimized.go`：在该可比样本中，时间名次 1/21，内存名次 1/21。

早先的 PyPy 比较：`1785_implementation_optimized.py`：在该可比样本中，时间名次 566/582，内存名次 2/582。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1785_implementation.cpp](1785_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 376 KB | 11303506 |
| [1785_implementation.go](1785_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1080 KB | 11289797 |
| [1785_implementation.java](1785_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1600 KB | 11303507 |
| [1785_implementation.py](1785_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 424 KB | 11289798 |
| [1785_implementation.rs](1785_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 228 KB | 11289801 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1785_implementation_optimized.cpp](1785_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 116 KB | 11303636 |
| [1785_implementation_optimized.java](1785_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.093 s | 340 KB | 11303777 |
| [1785_implementation_optimized.go](1785_implementation_optimized.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.015 s | 796 KB | 11325055 |
| [1785_implementation_optimized.py](1785_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 704 KB | 11327034 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
