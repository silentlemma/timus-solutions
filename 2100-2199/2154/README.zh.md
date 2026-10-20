# 2154. 过两点且离原点最近的直线

[Timus 2154](https://acm.timus.ru/problem.aspx?space=1&num=2154) · 难度 2318 · geometry, sorting

原题作者 Valentin Zuev，出自 2020 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 座炮台位于互不相同的整点上。从一座炮台可以乘炮弹飞向任意另一座炮台，可以在途经的任意炮台上方跳下，炮弹则一直飞下去。求用这种方式能到达的离原点最近的距离，绝对或相对误差不超过 10⁻⁶。时间限制 2 秒，内存限制 256 MB。

## 输入

n（2 ≤ n ≤ 10⁵），然后是各点，|xᵢ|, |yᵢ| ≤ 10⁵。

## 输出

最小距离。

## 样例

### 样例 1

输入：

```
4
1 0
0 1
-1 0
0 -1
```

输出：

```
0.0000000000
```

### 样例 2

输入：

```
5
0 3
1 2
1 3
1 4
2 3
```

输出：

```
0.7071067812
```

## 解法

每座炮台都能从其他任一座到达，而从 A 经过 B 的飞行加上从 B 经过 A 的飞行覆盖整条直线 AB。所以答案是原点到过两座炮台的直线的最小距离 |A × B| / |A − B|；若有炮台位于原点则为 0。

检查所有点对太慢，但只需要按模 π 的方向排序后相邻的点对：按原点到各点的直线的角度排序（键为 x / y），取所有循环相邻的点对：最近直线上的两点在这个循环顺序中总是相邻的（从某一侧）。与原点共线的点键相同，彼此相邻，给出 0。在大量随机小数据上与枚举全部点对的比较证实了这一点。工作量 O(n log n)。

易错点：答案应按数值比较，允许不超过 10⁻⁶ 的绝对或相对误差，而不能逐字比较。测试 01 中，`0` 和 `0.0000000000` 都是合法输出。检查器接受这两种格式，并拒绝非有限值及多余的标记。

第一个样例中过 (1, 0) 和 (−1, 0) 的直线经过原点。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2154_geometry_sorting.cpp](2154_geometry_sorting.cpp) | G++ 13.2 x64 | geometry, sorting | O(n log n) | AC | 0.062 s | 1580 KB |
| [2154_geometry_sorting.go](2154_geometry_sorting.go) | Go 1.14 x64 | geometry, sorting | O(n log n) | AC | 0.062 s | 9244 KB |
| [2154_geometry_sorting.java](2154_geometry_sorting.java) | Java 1.8 | geometry, sorting | O(n log n) | AC | 0.187 s | 9136 KB |
| [2154_geometry_sorting.py](2154_geometry_sorting.py) | Python 3.12 x64 | geometry, sorting | O(n log n) | AC | 0.312 s | 30008 KB |
| [2154_geometry_sorting.rs](2154_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O(n log n) | AC | 0.062 s | 6320 KB |
