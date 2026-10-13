# 1499. 三角帽

[Timus 1499](https://acm.timus.ru/problem.aspx?space=1&num=1499) · 难度 1474 · constructive

原题作者 Alex Samsonov，出自 2006 年 10 月 14 日第十三届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

顶点为 1 … N（3 ≤ N ≤ 50000）的正多边形上已经沿对角线切了 K 刀，互不相交
（0 ≤ K ≤ N − 3）。需要再沿对角线切若干刀，与其他刀都不相交，直到多边形被分成三
角形，并输出新切的刀。

时间限制：2 秒。内存限制：64 MB。

## 输入

N、K，然后是 K 行，每行一刀的两个顶点。

## 输出

新切的刀数，然后是各刀的两个顶点。任何三角剖分都可以。

## 样例

### 样例 1

输入:

```
5
1
1 4
```

输出:

```
1
3 1
```

## 解法

N 边形的任何三角剖分都有 N − 3 条对角线，所以恰好缺少 N − 3 − K 刀。已有的刀把多边
形分成若干凸面，任何一个面都可以用从它某个顶点出发的扇形对角线剖分。

按顺序遍历顶点 1 … N，用栈找出这些面。每个顶点 v 入栈；然后对每条已有的刀 u–v
（u < v），按 u 由近到远的顺序，栈中 u 之上的顶点连同 u 和 v 构成一个面：把它们
弹出，从 u 出发做扇形剖分，再把 v 压回。遍历结束后栈中剩下的是含边 N–1 的面，也做
扇形剖分。每个顶点入栈出栈的次数有界，所以除了在每个顶点对刀排序之外，遍历是线性
的。`O(N log N)`。

注意事项：

- 一刀可能先给出较大的顶点（测试 06）；
- 多刀可能在同一个顶点结束，它们的面要由内向外依次闭合（测试 05、gen4）；
- 若 N − 3 刀已全部给出，或 N = 3，答案为 0（测试 02、03、gen3）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1499_constructive.cpp](1499_constructive.cpp) | G++ 13.2 x64 | constructive | O(N log N) | AC | 0.078 s | 2108 KB |
| [1499_constructive.go](1499_constructive.go) | Go 1.14 x64 | constructive | O(N log N) | AC | 0.093 s | 9344 KB |
| [1499_constructive.java](1499_constructive.java) | Java 1.8 | constructive | O(N log N) | AC | 0.171 s | 10440 KB |
| [1499_constructive.py](1499_constructive.py) | Python 3.12 x64 | constructive | O(N log N) | AC | 0.187 s | 14896 KB |
| [1499_constructive.rs](1499_constructive.rs) | Rust 1.75 x64 | constructive | O(N log N) | AC | 0.031 s | 4108 KB |
