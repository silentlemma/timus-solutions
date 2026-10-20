# 2196. 凸多边形不断扩张的邻域到达每个点的日子

[Timus 2196](https://acm.timus.ru/problem.aspx?space=1&num=2196) · 难度 1617 · geometry, binary_search

原题作者 Vadim Barinov，出自 2023 年 ICPC 乌拉尔赛区资格赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

第 0 天一个 N 个顶点的凸多边形被感染。之后每天被感染的是到多边形距离不超过某个值的所有点，且面积每天翻倍。对 Q 个点中的每一个，求它第一次位于感染区域内部或边界上的那一天。保证点到之后每一天的边界的距离至少为 10⁻⁶。时间限制 3 秒，内存限制 256 MB。

## 输入

N（3 ≤ N ≤ 10⁵），然后是逆时针给出的顶点，然后是 Q（1 ≤ Q ≤ 10⁵）和各点，所有坐标绝对值不超过 10⁹。

## 输出

每个点对应的日子。

## 样例

### 样例 1

输入：

```
4
1 3
1 1
3 1
3 3
4
2 2
1 2
4 1
6 2
```

输出：

```
0
0
2
4
```

## 解法

面积为 A、周长为 P 的凸多边形，到它距离不超过 d 的点集面积为 A + P d + π d²：多边形本身、沿每条边的一条带，以及角上合起来恰为一个整圆的扇形。所以第 i 天的半径 dᵢ 是 A + P d + π d² = 2ⁱ A 的解，为避免抵消写成 dᵢ = (2ⁱ − 1) A / (P/2 + √(P²/4 + π (2ⁱ − 1) A))。大约 70 天后半径就超过最大可能距离，到多边形距离为 D 的点的答案就是第一个满足 dᵢ ≥ D 的 i。

每个点到凸多边形的距离用 O(log N) 求出。在以顶点 0 为中心的三角形扇上二分，判断点是否在内部（第 0 天），若不在，就找到一条朝向该点的边和一条背向该点的边。沿朝向的链，点到各边的距离先减后增，所以按投影的符号再做一次二分，就找到最近的边或顶点。

当距离与某个半径相差不超过 10⁻⁵ 时，用 double-double 算术在不开方的情况下重新比较：设距离为 √(u / v)，E = (2ⁱ − 1) A，则当 E v − π u ≥ 0 且 (E v − π u)² ≥ P² u v 时该点被感染。

样例中正方形 A = 4、P = 8；点 (6, 2) 的距离为 3，第 4 天是第一个满足 8d + πd² = 60 的日子，此时 d ≈ 3.28。

总复杂度 O(N + Q log N)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2196_geometry_binary_search.cpp](2196_geometry_binary_search.cpp) | G++ 13.2 x64 | geometry, binary_search | O(N + Q log N) | AC | 0.171 s | 7904 KB |
| [2196_geometry_binary_search.go](2196_geometry_binary_search.go) | Go 1.14 x64 | geometry, binary_search | O(N + Q log N) | AC | 0.187 s | 30296 KB |
| [2196_geometry_binary_search.java](2196_geometry_binary_search.java) | Java 1.8 | geometry, binary_search | O(N + Q log N) | AC | 0.578 s | 12632 KB |
| [2196_geometry_binary_search.py](2196_geometry_binary_search.py) | PyPy 3.10 x64 | geometry, binary_search | O(N + Q log N) | AC | 1.187 s | 49568 KB |
| [2196_geometry_binary_search.rs](2196_geometry_binary_search.rs) | Rust 1.75 x64 | geometry, binary_search | O(N + Q log N) | AC | 0.171 s | 15164 KB |
