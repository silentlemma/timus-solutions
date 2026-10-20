# 2165. 最小三角形最大的凸多边形三角剖分

[Timus 2165](https://acm.timus.ru/problem.aspx?space=1&num=2165) · 难度 1622 · dp, geometry

原题作者 Vadim Barinov，出自 2021 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

用互不相交的对角线把 N 个顶点的凸多边形切成三角形，使最小的三角形尽可能大，输出其面积，绝对误差或相对误差不超过 10⁻⁹。时间限制 1 秒，内存限制 256 MB。

## 输入

N（3 ≤ N ≤ 200），然后是逆时针给出的顶点，坐标绝对值不超过 10⁸。

## 输出

最小三角形可能的最大面积。

## 样例

### 样例 1

输入：

```
4
0 0
5 -1
8 3
0 4
```

输出：

```
11.5
```

## 解法

这是三角剖分上经典的区间动态规划。设 f(i, j) 为顶点 i … j 构成的子多边形的三角剖分中最优的最小三角形。它的边 (i, j) 恰好属于一个三角形 (i, k, j)（i < k < j），该三角形把它分成 i … k 和 k … j 两部分，所以

f(i, j) = max_k min(f(i, k), f(k, j), area(i, k, j))，

单条边时 f(i, i + 1) = +∞，因为边不应限制最小值。C++ 和 Python 使用多边形面积的两倍；Go、Java 和 Rust 使用安全上界 8 · 10¹⁶。若初始化为零，所有状态的值都会变为零，即使在测试 02 中也是如此。答案是 f(0, N − 1)。面积以两倍的精确整数保存，来自至多约 4 · 10¹⁶ 的叉积，因此最终的半整数可以精确输出。无法超过当前最优值的候选会提前跳过。工作量 O(N³)。

样例中四边形的两种剖分给出的最小块分别为 11.5 和 10，所以答案是 11.5。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2165_dp_geometry.cpp](2165_dp_geometry.cpp) | G++ 13.2 x64 | dp, geometry | O(N^3) | AC | 0.031 s | 764 KB |
| [2165_dp_geometry.go](2165_dp_geometry.go) | Go 1.14 x64 | dp, geometry | O(N^3) | AC | 0.031 s | 1444 KB |
| [2165_dp_geometry.java](2165_dp_geometry.java) | Java 1.8 | dp, geometry | O(N^3) | AC | 0.109 s | 816 KB |
| [2165_dp_geometry.py](2165_dp_geometry.py) | Python 3.12 x64 | dp, geometry | O(N^3) | AC | 0.171 s | 2656 KB |
| [2165_dp_geometry.rs](2165_dp_geometry.rs) | Rust 1.75 x64 | dp, geometry | O(N^3) | AC | 0.015 s | 464 KB |
