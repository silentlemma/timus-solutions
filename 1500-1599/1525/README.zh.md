# 1525. 路径

[Timus 1525](https://acm.timus.ru/problem.aspx?space=1&num=1525) · 难度 376 · implementation

原题作者 Dmitry Gozman，出自 2007 年 1 月彼得罗扎沃茨克冬季集训的 Dmitry Gozman Contest 1。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

机器人位于 n × m × k 盒子（1 ≤ n, m, k ≤ 10⁵）中未知的一格，执行一段最多 10⁵ 步的程
序：'l'、'r' 沿宽度，'d'、'u' 沿高度，'b'、'f' 沿长度。会走出盒子的步骤被忽略。求机
器人最终可能所在的格子数。

时间限制：1 秒。内存限制：64 MB。

## 输入

n、m、k，然后是一行程序。

## 输出

可能的最终格子数。

## 样例

### 样例 1

输入:

```
1 1 1
uuuur
```

输出:

```
1
```

### 样例 2

输入:

```
2 2 2
ulf
```

输出:

```
1
```

### 样例 3

输入:

```
13 14 15
uudlbdrruffbr
```

输出:

```
1560
```

## 解法

三个坐标轴互不影响，所以答案是各轴数量的乘积。在一条轴上，每一步要么把每个起点移动
一格，要么让它停在墙边，所以相邻两个起点始终保持顺序且相距不超过一。因此所有起点的
终点填满两个端点起点 1 和 L 的终点之间的整个区间，这条轴贡献 f(L) − f(1) + 1。只需模
拟这两个起点。`O(len)`。

注意事项：

- 数目可达约 10¹⁵，需要 64 位（测试 04、gen1）；
- 程序可能为空，这时每个格子都算（测试 05）；
- 足够长的一串同向步骤会把所有起点推到墙边（测试 01、06）。

## 优化解法

对每个轴记录无墙限制时的位移 s，以及包含零在内的前缀最小值 lo 和最大值 hi。坐标为 0 到 L − 1 时，可达区间两端在相遇前为 s − lo 和 L − 1 + s − hi。新的最小值使第一端贴到零，新的最大值使第二端贴到 L − 1。两端相遇后不会再分开。位置数为 max(1, L − (hi − lo))，一次扫描后相乘三个轴的结果。

已通过评测的基础实现 [1525_implementation.java](1525_implementation.java) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1525_implementation.cpp](1525_implementation.cpp) | G++ 13.2 x64 | implementation | O(len) | AC | 0.015 s | 528 KB | 11287395 |
| [1525_implementation.go](1525_implementation.go) | Go 1.14 x64 | implementation | O(len) | AC | 0.015 s | 1748 KB | 11287396 |
| [1525_implementation.java](1525_implementation.java) \* | Java 1.8 | implementation | O(len) | AC | 0.140 s | 2212 KB | 11287401 |
| [1525_implementation.py](1525_implementation.py) | Python 3.12 x64 | implementation | O(len) | AC | 0.109 s | 692 KB | 11287398 |
| [1525_implementation.rs](1525_implementation.rs) | Rust 1.75 x64 | implementation | O(len) | AC | 0.046 s | 468 KB | 11287405 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1525_math.cpp](1525_math.cpp) | G++ 13.2 x64 | math | O(len) | AC | 0.015 s | 112 KB | 11310466 |
| [1525_math.go](1525_math.go) \* | Go 1.14 x64 | math | O(len) | AC | 0.015 s | 932 KB | 11310467 |
| [1525_math.py](1525_math.py) | Python 3.12 x64 | math | O(len) | AC | 0.078 s | 520 KB | 11310470 |
| [1525_math.rs](1525_math.rs) \* | Rust 1.75 x64 | math | O(len) | AC | 0.031 s | 216 KB | 11310469 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
