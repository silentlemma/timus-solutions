# 2218. 统计恰好在给定曼哈顿距离上的点

[Timus 2218](https://acm.timus.ru/problem.aspx?space=1&num=2218) · 难度 817 · geometry, binary_search

原题作者 Vadim Barinov，出自 2025 年 ICPC 乌拉尔赛区资格赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 台互不相同的计算机位于整点上。位于 (x, y) 的跑者必须沿坐标轴方向恰好跑 d，且不能跑向距离小于 d 的计算机。对 Q 名跑者中的每一位，统计曼哈顿距离恰为 d 的计算机数。时间限制 3 秒，内存限制 256 MB。

## 输入

N（1 ≤ N ≤ 10⁵），然后是各计算机，然后是 Q（1 ≤ Q ≤ 10⁵）和跑者 x、y、d，坐标绝对值不超过 10⁹，0 ≤ d ≤ 4 · 10⁹。

## 输出

每名跑者对应的数目。

## 样例

### 样例 1

输入：

```
5
0 0
1 1
2 0
1 -1
1 0
4
1 0 1
2 2 2
5 1 5
0 1 4
```

输出：

```
4
2
1
0
```

## 解法

做旋转变换 u = x + y、v = x − y。曼哈顿距离变为 max(|Δu|, |Δv|)，所以距离恰为 d 的点位于一个与坐标轴平行的正方形的边界上：两条竖边 u = U ± d 且 |v − V| ≤ d，两条横边 v = V ± d 且 |u − U| < d，角点算在竖边里。

把点按 (u, v) 排序，另外再按 (v, u) 排序。于是每条边都是某个列表中连续的一段，两次二分查找就能数出来。d = 0 时只有跑者自己所在的点可能符合。

样例中位于 (1, 0)、d = 1 的跑者能到达四个邻点 (0, 0)、(1, 1)、(2, 0) 和 (1, −1)。

排序需要 O(N log N)，每名跑者最多八次二分查找：d > 0 时八次，d = 0 时两次。易错点（测试 02 和 09）：d = 0 时正方形退化为一个点，因此只检查该点一次，不应再统计四条边。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2218_geometry_binary_search.cpp](2218_geometry_binary_search.cpp) | G++ 13.2 x64 | geometry, binary_search | O((N + Q) log N) | AC | 0.203 s | 2880 KB |
| [2218_geometry_binary_search.go](2218_geometry_binary_search.go) | Go 1.14 x64 | geometry, binary_search | O((N + Q) log N) | AC | 0.250 s | 19016 KB |
| [2218_geometry_binary_search.java](2218_geometry_binary_search.java) | Java 1.8 | geometry, binary_search | O((N + Q) log N) | AC | 0.562 s | 11280 KB |
| [2218_geometry_binary_search.py](2218_geometry_binary_search.py) | PyPy 3.10 x64 | geometry, binary_search | O((N + Q) log N) | AC | 1.453 s | 61836 KB |
| [2218_geometry_binary_search.rs](2218_geometry_binary_search.rs) | Rust 1.75 x64 | geometry, binary_search | O((N + Q) log N) | AC | 0.140 s | 12772 KB |
