# 1617. 车轮擦伤

[Timus 1617](https://acm.timus.ru/problem.aspx?space=1&num=1617) · 难度 65 · implementation

原题作者 Vladimir Yakovlev，出自 2008 年 3 月 29 日第十二届乌拉尔竞技编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

车库里有 n 个轮对（1 ≤ n ≤ 150），每个的直径是 600 到 700 毫米之间的整数。
一节电车车厢需要四个直径相同的轮对。最多能装备多少节车厢？

时间限制：0.5 秒。内存限制：64 MB。

## 输入

n，然后是 n 个直径。

## 输出

车厢数。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
9
689
690
690
689
689
690
689
688
688
```

输出：

```
1
```

## 解法

统计每种直径的轮对数。有 c 对的直径能装备 ⌊c / 4⌋ 节车厢，不同直径互不影响，
所以答案是对所有直径求和。`O(n)`。

易错点：

- 不同直径剩下的轮对不能拼在一起（测试 01）；
- 同一尺寸的八对能装备两节车厢，而不是一节（测试 03）。

## 优化解法

优化的 Java 解法按 1 KB 分块读入并手工解析，而不是使用 `Scanner`，并用 101 个计
数器的普通数组统计 600 到 700 之间的直径，下标为直径减去 600：0.109 s，而不是
0.140 s；336 KB，而不是 1680 KB。

`1617_implementation_optimized.py`. 用 101 项频数列表替代 Counter，下标为 diameter-600，由范围 600..700 保证。求 frequency//4 之和，因为不能混合直径。字节记号迭代避免解码文本和哈希键，但仍保存输入记号，总空间 O(N+101)，并非常数流式空间。时间 O(N+101)。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1617_implementation.py` 相比：时间 0.093 s → 0.125 s；内存 368 KB → 244 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1617_implementation_optimized.py`：在该可比样本中，时间名次 88/104，内存名次 1/104。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1617_implementation.cpp](1617_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11288341 |
| [1617_implementation.go](1617_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1092 KB | 11288342 |
| [1617_implementation.java](1617_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1680 KB | 11288344 |
| [1617_implementation.py](1617_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 368 KB | 11288343 |
| [1617_implementation.rs](1617_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 240 KB | 11303771 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1617_implementation_optimized.java](1617_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.109 s | 336 KB | 11303764 |
| [1617_implementation_optimized.py](1617_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(N+101) | AC | 0.125 s | 244 KB | 11325072 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
