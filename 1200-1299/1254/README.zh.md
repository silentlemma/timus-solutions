# 1254. 在城市中按顺序拆除炸弹

[Timus 1254](https://acm.timus.ru/problem.aspx?space=1&num=1254) · 难度 646 · shortest_paths

原题作者 Pavel Atnashev，出自 2003 年 3 月 15 日乌拉尔国立大学公开团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

城市是一个 N × M 的网格（N, M ≤ 75），由空地 `.` 和建筑 `#` 组成。John 以速度 V
在相邻的空地之间沿边或沿对角线移动。他从 (x₀, y₀) 出发，必须按给定顺序拆除 K 颗炸弹
（K ≤ 1000）；到达不了的炸弹就跳过。求最少的总时间，保留两位小数。

时间限制：5 秒。内存限制：64 MB。

## 输入

N、M、K 和 V；地图为 M 行、每行 N 个字符；起点；K 颗炸弹，形如 `x y`。

## 输出

最少时间，小数点后两位。

## 样例

### 样例 1

输入：

```
4 3 3 1.23
....
##..
....
1 1
1 3
4 1
4 3
```

输出：

```
8.66
```

## 解法

拆除是瞬间完成的，顺序是固定的，所以总时间就是从每个位置到下一颗可到达炸弹的最短
路径之和，再除以 V。沿边一步长 1，沿对角线一步长 √2；对角线一步可以擦过建筑的角，
样例在经过 `##` 时就需要这一点。

最多需要在 5625 个格子上做 1000 次最短路搜索。有三点让它们代价很低：

- 预先把城市划分成由移动连通的各个部分，所以位于别的部分的炸弹会被立即跳过，而不必
  先做一次完整搜索；
- 每次搜索都是 A*，以八方向距离 `max(dx, dy) + (√2 − 1)·min(dx, dy)` 作为估计，它
  永远不超过真实长度，所以炸弹第一次出队时距离就已确定；在开阔的城市里估计值是
  精确的；
- 已经求出的路径按两个端点（双向）记下来。

地图外围加了一圈建筑，所以移动不需要检查边界。最坏情况 `O(K · NM log NM)`。

注意事项：

- 遇到到达不了的炸弹后，John 留在原地（测试 03）；
- 起点可能与炸弹重合，此时路径长 0（测试 02）；
- 起点格子无论地图上是什么都视为空地。

这些总时间在 300 个带建筑和不可到达炸弹的随机小城市上与普通 Dijkstra 的结果比较过。

## 各语言说明

- 这里 Python 最慢：测试中最大的蜿蜒街道约需 1.5 秒，时限为 5 秒。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1254_shortest_paths.cpp](1254_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(K · NM log NM) | AC | 0.140 s | 312 KB |
| [1254_shortest_paths.go](1254_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(K · NM log NM) | AC | 0.328 s | 6896 KB |
| [1254_shortest_paths.java](1254_shortest_paths.java) | Java 1.8 | shortest_paths | O(K · NM log NM) | AC | 0.531 s | 7204 KB |
| [1254_shortest_paths.py](1254_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(K · NM log NM) | AC | 2.906 s | 1740 KB |
| [1254_shortest_paths.rs](1254_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(K · NM log NM) | AC | 0.140 s | 808 KB |
