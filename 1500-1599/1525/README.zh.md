# 1525. 路径

[Timus 1525](https://acm.timus.ru/problem.aspx?space=1&num=1525) · 难度 375 · implementation

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
- 一长串同向的步骤会把所有起点推到墙边（测试 01、06、gen3）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1525_implementation.cpp](1525_implementation.cpp) | G++ 13.2 x64 | implementation | O(len) | AC | 0.015 s | 528 KB |
| [1525_implementation.go](1525_implementation.go) | Go 1.14 x64 | implementation | O(len) | AC | 0.015 s | 1748 KB |
| [1525_implementation.java](1525_implementation.java) | Java 1.8 | implementation | O(len) | AC | 0.140 s | 2212 KB |
| [1525_implementation.py](1525_implementation.py) | Python 3.12 x64 | implementation | O(len) | AC | 0.109 s | 692 KB |
| [1525_implementation.rs](1525_implementation.rs) | Rust 1.75 x64 | implementation | O(len) | AC | 0.046 s | 468 KB |
