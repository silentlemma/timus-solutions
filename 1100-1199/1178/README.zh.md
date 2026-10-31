# 1178. 用互不相交的直路把城市两两配对

[Timus 1178](https://acm.timus.ru/problem.aspx?space=1&num=1178) · 难度 151 · geometry

原题作者 Pavel Atnashev，出自 2002 年 2 月 16 日在叶卡捷琳堡举行的第三届乌拉尔国立大学个人程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

偶数个 `N ≤ 10000` 座城市位于整点上，坐标绝对值不超过 `10⁹`，任意三座不共线。
用直路把它们两两连接，使每座城市恰好在一条路上，并且任意两条路都不相交。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`，然后 `N` 行，每行是一个城市的两个坐标。

## 输出

`N/2` 行，每行是一条路连接的两座城市的编号。

## 评测方式

只要每座城市恰好配对一次且任意两条路都不相交，就被接受；检查程序比较 `x`
范围有重叠的路。

## 样例

### 样例 1

输入：

```
4
0 2
1 1
3 4
4 4
```

输出：

```
1 3
2 4
```

## 解法

把城市按 `x` 排序，第一座连第二座，第三座连第四座，依此类推。每条路位于它
两个端点的 `x` 之间的竖直带中，不同路的竖直带至多在一条边界线上重叠。在这条线上
每条路只有一个端点，而这两个端点是不同的城市，所以路不会在那里相遇。若一条路的
两座城市 `x` 相同，它是竖直的，但这时那条线上没有其他城市，因为任意三座城市
不共线。所以任意两条路都不相交。`O(N log N)`。

注意事项：

- 相同的 `x` 不需要特殊处理，不过各解答按 `y` 排定顺序，以便输出可复现；
- 坐标达到 `10⁹`，仍在 32 位整数范围内，解法只比较它们。

每个输出的方案都在所有测试上通过了检查程序，其中包括位于二次曲线上、有大量
相同 `x` 的一万座城市。

## 优化解法

优化的 Java 解法从 4 KB 缓冲区中手工解析数字，而不是把所有行拼成一个字符串交给
`StringTokenizer`，并对普通 `long` 数组排序，而不是用比较器对装箱的 `Integer` 城
市编号排序。每个键是 `x + 10⁹`（不超过 2·10⁹，即 31 位）左移到 14 位城市下标（小
于 10000 < 2¹⁴）之上。键中只有 `x`：由于没有三个城市共线，同一个 `x` 至多属于两
个城市，排序后再扫一遍，若这样相邻的一对的 `y` 顺序不对就交换它们：
{1178_geometry_optimized.java}。

优化的 Python 解法利用每行恰好一个城市这一点，逐行读入，而不是切分整个输入。它把
每个城市打包成一个整数：`x + 10⁹` 和 `y + 10⁹` 各占 31 位，放在 14 位城市编号之
上，这样普通的 `sort` 就按 `(x, y)` 排序，无需键函数或元组；配对结果边算边输出，
不再收集成行列表：{1178_geometry_optimized.py}。

优化的 Rust 解法从 4 KB 缓冲区中手工解析数字，而不是把整个输入读进 `String` 再存
成所有数的向量。它用不需要额外缓冲区的 `sort_unstable` 对 `i32` 的
`(x, y, 编号)` 元组排序，`i32` 足以容纳绝对值不超过 `10⁹` 的坐标，输出经由
`BufWriter`：{1178_geometry_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1178_geometry_optimized.java`: 时间降低 +33.57%; 内存降低 +85.16%; 基础版本: `1178_geometry.java`.

- `1178_geometry_optimized.py`: 时间降低 +0.00%; 内存降低 +66.30%; 基础版本: `1178_geometry.py`.

- `1178_geometry_optimized.rs`: 时间降低 -106.67%; 内存降低 +61.78%; 基础版本: `1178_geometry.rs`.

## 各语言说明

- 所有语言都按 `x` 对城市排序，`x` 相同时按 `y`。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1178_geometry.cpp](1178_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 388 KB | 11283266 |
| [1178_geometry.go](1178_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1676 KB | 11283270 |
| [1178_geometry.java](1178_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 6872 KB | 11283277 |
| [1178_geometry.py](1178_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 3276 KB | 11283275 |
| [1178_geometry.rs](1178_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.015 s | 764 KB | 11283279 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1178_geometry_optimized.java](1178_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.093 s | 1020 KB | 11305836 |
| [1178_geometry_optimized.py](1178_geometry_optimized.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 1104 KB | 11305838 |
| [1178_geometry_optimized.rs](1178_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 292 KB | 11305833 |
