# 1527. 糟糕的道路

[Timus 1527](https://acm.timus.ru/problem.aspx?space=1&num=1527) · 难度 1133 · shortest_paths

原题作者 Dmitry Gozman，出自 2007 年 1 月彼得罗扎沃茨克冬季集训的 Dmitry Gozman Contest 1。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 座城市（1 ≤ n ≤ 100）由 m 条单向道路（1 ≤ m ≤ 10⁴）相连。每条路耗费一定时间，可
能收取一枚通行费，并要求汽车的离地间隙不低于给定值。求能在 t 分钟内、花费不超过 b
枚通行费从 s 到达 f 的汽车的最小离地间隙及一条路线，否则输出 -1。

时间限制：2 秒。内存限制：64 MB。

## 输入

n、m、s、f；然后是 b 和 t；然后每条路：起点、终点、是否收费（0 或 1）、时间和间隙
要求。

## 输出

最小间隙、路线中道路的条数以及按顺序排列的道路编号；或者 -1。任何符合要求的路线都
可以。

## 样例

### 样例 1

输入:

```
2 2 1 2
1 100
1 2 1 100 77
1 2 1 100 66
```

输出:

```
66
1
2
```

### 样例 2

输入:

```
2 2 1 2
0 100
1 2 0 101 77
1 2 1 100 66
```

输出:

```
-1
```

## 解法

答案一定是某条路的间隙要求，而更大的间隙只会增加可用道路，所以在排序后的间隙值上二
分。检查一个间隙时，在状态（城市，已付费次数）上运行 Dijkstra 算法，只用不高于它的
道路，并满足两个限制。重复经过某城市的路线可以去掉这个环且不多付费，所以至多 n − 1
次收费有意义，预算可以截到这个值。如果更少的收费已经能同样快地到达某城市，就跳过该
状态，这让搜索保持很小。每个状态的前驱道路给出路线。状态至多 n² 个，
一次检查 `O(n·m·log(n·m))`，总共 `O(log m · n·m·log(n·m))`，实际要少得多。

注意事项：

- 收费预算可达 10⁶，但超过 n − 1 次收费永远没有用（测试 08）；
- 道路可能完全不耗时（测试 03、gen3）；
- 更省钱的路线可能太慢，反之亦然（测试 04、05）；
- 在限制内甚至完全无法到达终点（测试 02、06、gen5）；
- 间隙要求可以是 0（测试 07）；
- 符合要求的路线可能有很多，所以测试使用检查程序（所有测试）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1527_shortest_paths.cpp](1527_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(log m * n * m * log(n * m)) | AC | 0.031 s | 484 KB |
| [1527_shortest_paths.go](1527_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(log m * n * m * log(n * m)) | AC | 0.031 s | 5480 KB |
| [1527_shortest_paths.java](1527_shortest_paths.java) | Java 1.8 | shortest_paths | O(log m * n * m * log(n * m)) | AC | 0.140 s | 5672 KB |
| [1527_shortest_paths.py](1527_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(log m * n * m * log(n * m)) | AC | 0.187 s | 6608 KB |
| [1527_shortest_paths.rs](1527_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(log m * n * m * log(n * m)) | AC | 0.031 s | 1016 KB |
