# 2071. 使倒入次数最少的鸡尾酒顺序

[Timus 2071](https://acm.timus.ru/problem.aspx?space=1&num=2071) · 难度 641 · bitmask, dp

原题作者 Mikhail Rubinchik（由 Nickolai Permyakov 和 Alexey Danilyuk 整理），出自 2015 年乌拉尔地区团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 位客人各点一杯鸡尾酒：果汁 A、B、P 的一个非空集合。杯子按某种顺序排成一排，一次倒入把一种果汁倒进一段连续的杯子（先苹果，再香蕉，最后菠萝，所以倒入顺序不成问题）。每个杯子必须恰好得到其鸡尾酒中的果汁。安排杯子顺序，使倒入次数最少。时间限制 1 秒，内存限制 64 MB。

## 输入

n（1 ≤ n ≤ 10⁵），然后 n 行，每行是 A、B、P、AB、AP、BP、ABP 之一。

## 输出

最少倒入次数，然后按排列顺序输出杯子编号。任何最优排列都可接受。

## 评测方式

检查器比较倒入次数，并重新计算输出的排列所需的倒入次数。

## 样例

### 样例 1

输入：

```
3
A
B
ABP
```

输出：

```
3
1 3 2
```

## 解法

排列固定时，每种果汁对其所在杯子的每个极长连续段需要一次倒入，所以代价就是“某果汁在当前杯中有而在前一杯中没有”的位置数（第一杯的所有果汁都计入）。把一个杯子移到相同的杯子旁边永远不会增加段数，所以同一种鸡尾酒的杯子可以放在一起，只需决定至多七种不同鸡尾酒的顺序。

用子集 DP 确定顺序：best[S][last] 表示由集合 S 中的鸡尾酒组成、以 last 结尾的一排所需的最少倒入次数。在后面接上鸡尾酒 k 的代价是 k 中 last 没有的果汁数，即 popcount(k & ~last)。答案是全集下对 last 取最小，记录的前驱给出顺序。七种鸡尾酒时只有 2⁷ · 7 · 7 步，所以总工作量是读入和输出的 O(n)。

样例中顺序 B、ABP、A 需要三次倒入：每种果汁一段。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2071_bitmask_dp.cpp](2071_bitmask_dp.cpp) | G++ 13.2 x64 | bitmask, dp | O(n) | AC | 0.078 s | 440 KB |
| [2071_bitmask_dp.go](2071_bitmask_dp.go) | Go 1.14 x64 | bitmask, dp | O(n) | AC | 0.046 s | 7572 KB |
| [2071_bitmask_dp.java](2071_bitmask_dp.java) | Java 1.8 | bitmask, dp | O(n) | AC | 0.125 s | 8848 KB |
| [2071_bitmask_dp.py](2071_bitmask_dp.py) | Python 3.12 x64 | bitmask, dp | O(n) | AC | 0.140 s | 17408 KB |
| [2071_bitmask_dp.rs](2071_bitmask_dp.rs) | Rust 1.75 x64 | bitmask, dp | O(n) | AC | 0.062 s | 7116 KB |
