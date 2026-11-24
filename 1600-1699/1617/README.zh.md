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

`1617_implementation_optimized.py`. 保留 600..700 的 101 个频次及 floor(frequency/4) 之和。直接读二进制，短答案用 os.write 完整输出再 os._exit(0)。split 仍保留输入 token，空间 O(I+101)，I 为输入字节，并非常数空间流式处理。O(N+101) 算术，处理全部声明轮对。保留教学 Counter 版。

精确源代码 Python 3.12 x64 Accepted #11327789：0.062 s / 660 KB。2026-11-20 保存的编译器组比较：时间 1/104、内存 90/104。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11325072 为 0.125 s / 244 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1617_implementation_optimized.py`: 0.062 s / 660 KB; 保留教学基础版 `1617_implementation.py`: 0.093 s / 368 KB.

`1617_implementation_optimized.java`. 保留对 600..700 相同直径的单遍分组。每直径一个 byte 仅存模四余数，达到四就清零并计一辆；读取之间余数至多三，有符号 byte 足够，无需最终频率遍历。O(N) 时间、101 字节分组状态。计算所用数值均在输出前读完。复用一个 256 字节数组先输入后输出，每个有符号 int 预留十二字节，只反转刚写的数字。省去独立输入、输出和数字数组，不覆盖算法尚需的数据。解析输出对已消费字节线性，缓冲固定。

精确源代码 Java 1.8 Accepted #11327764：0.078 s / 368 KB。2026-11-20 保存的编译器组比较：时间 1/221、内存 6/221。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11303764 为 0.109 s / 336 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1617_implementation_optimized.java`: 0.078 s / 368 KB; 保留教学基础版 `1617_implementation.java`: 0.14 s / 1680 KB.

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

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
| [1617_implementation_optimized.java](1617_implementation_optimized.java) | Java 1.8 | implementation | O(N) time; 101 byte remainders | AC | 0.078 s | 368 KB | 11327764 |
| [1617_implementation_optimized.py](1617_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N+101) time; O(I+101) storage | AC | 0.062 s | 660 KB | 11327789 |
