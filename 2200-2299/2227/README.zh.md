# 2227. 沿对角线测量和切割凸多边形

[Timus 2227](https://acm.timus.ru/problem.aspx?space=1&num=2227) · 难度 1875 · geometry, fenwick

原题作者 Vadim Barinov。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个 N 个顶点的凸多边形沿当前多边形的对角线经历 Q 次操作：测量报告两部分面积中较大者；切割扔掉较小的部分（相等时扔掉含有编号在所选两顶点之外的顶点的那部分），并报告它的面积。以 10⁻⁹ 的精度输出所有报告的面积。时间限制 0.5 秒，内存限制 256 MB。

## 输入

N 和 Q（4 ≤ N ≤ 10⁵，1 ≤ Q ≤ 10⁵），然后是逆时针给出、坐标绝对值不超过 10⁹ 的顶点，然后是操作「m l r」或「c l r」。

## 输出

每次操作输出一个面积。

## 样例

### 样例 1

输入：

```
5 4
2 0
3 1
2 2
0 2
0 0
m 5 3
m 2 4
c 1 3
m 4 1
```

输出：

```
3.0
4.0
1.0
2.0
```

## 解法

所有面积都以两倍的精确整数保存，所以每个答案都以 ".0" 或 ".5" 结尾。设 l < r，原始顶点 l, l + 1, …, r 构成的多边形的两倍面积是鞋带公式前缀和的一段，再加上闭合项 x_r y_l − y_r x_l。

切割只会去掉一些块，被当前多边形的对角线切下的每一块都位于之后任何一条对角线的同一侧。从弧 l … r 上切下的块记在树状数组中该弧的第一条边 l + 1 上；位于弧外侧的块记在边 r + 1 上，在之后所有弧的外面。对之后的对角线 (l, r)，当前多边形在内侧弧上的部分等于该弧的原始面积减去边 l + 1 … r 上的记录，另一部分等于当前总面积减去它。

测量输出较大的部分。切割扔掉较小的部分（相等时扔掉外侧部分），按上述方式记录，并减少总面积。

样例中第一次测量沿 5–3 把面积为 5 的五边形分成 3 和 2 两部分，输出 3。

复杂度 O(N + Q log N)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2227_geometry_fenwick.cpp](2227_geometry_fenwick.cpp) | G++ 13.2 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.171 s | 2900 KB |
| [2227_geometry_fenwick.go](2227_geometry_fenwick.go) | Go 1.14 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.078 s | 12032 KB |
| [2227_geometry_fenwick.java](2227_geometry_fenwick.java) | Java 1.8 | geometry, fenwick | O(N + Q log N) | AC | 0.218 s | 13944 KB |
| [2227_geometry_fenwick.py](2227_geometry_fenwick.py) | PyPy 3.10 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.343 s | 52180 KB |
| [2227_geometry_fenwick.rs](2227_geometry_fenwick.rs) | Rust 1.75 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.046 s | 11220 KB |
