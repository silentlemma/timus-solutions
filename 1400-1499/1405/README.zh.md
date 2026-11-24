# 1405. 放山羊进菜园 5

[Timus 1405](https://acm.timus.ru/problem.aspx?space=1&num=1405) · 难度 709 · geometry

原题作者 Vladimir Yakovlev，出自 2005 年 10 月 15 日第十二届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

菜园里有 2 ≤ N ≤ 1000 棵树，坐标精确到厘米。两只山羊分别拴在两棵不同的树
上。山羊不能碰到其他的树，两只山羊不能碰到对方，绳长至少 1 米、至多 50 米。
求两只山羊能到达的最大总面积，精确到 1 平方厘米。保证存在合法的拴法。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是各棵树的坐标。

## 输出

最大面积（平方米），保留四位小数。

## 样例

### 样例 1

输入:

```
8
1 1
-2 0
5 3
-2 3
8 3.10
-2 -1
-2 2
8 4.10
```

输出:

```
36.8060
```

## 解法

在树 i 上，绳子不能碰到最近的另一棵树，再加上 50 米的上限，绳长至多为
topᵢ = min(50, 到最近另一棵树的距离)。对于拴在相距 d 的树 i 和 j 上的山羊，
绳长 a 和 b 需满足

1 ≤ a ≤ topᵢ，1 ≤ b ≤ topⱼ，a + b ≤ d，

面积为 π(a² + b²)。这是多边形上的凸函数，所以最大值在顶点处取得：矩形的角，
或直线 a + b = d 与矩形边的交点。检验这七个点中落在区域内的那些，并对所有树
对取最大值。`O(N²)`。Python 解答按 top 从大到小遍历树，一旦两棵树的 top²
之和都无法超过当前最优就结束这一行。

注意事项：

- 1 米和 50 米的限制很容易漏看：相距 141 米的两棵树给出 5000π，而不是距离的
  平方（测试 02）；
- 邻树距离小于 1 米的树不能拴山羊（测试 03 和 06）；
- 恰好相等的情形是允许的：绳长恰为 1 米，或两根绳长之和恰好等于距离（测试
  05 和生成测试 4）；
- 评测机上的 C++ 没有 M_PI，所以 π 取 acos(-1)。

在 3 000 个随机情形上把顶点枚举与区域上的细网格做了比较，论坛中的例子也给出
了预期的答案。

## 优化解法

用距离平方计算每棵树的绳长上限，再按上限降序排列。若一对树的两个上限无法改进当前面积，就跳过。若能同时取到两个上限，则直接使用，否则检查两根绳子恰好相接的两个端点。

**优化版本的 Timus 提交记录**

Go 按横坐标排序，并用水平距离提前结束最近邻扫描。

`1405_geometry_optimized.cpp` (G++ 13.2 x64) №11317478 · `1405_geometry_optimized.go` (Go 1.14 x64) №11322346 · `1405_geometry_optimized.java` (Java 1.8) №11317519 · `1405_geometry_optimized.py` (Python 3.12 x64) №11317508 · `1405_geometry_optimized.rs` (Rust 1.75 x64) №11323258.

Rust 按横坐标排序以提前停止最近邻扫描，并优先检查允许半径较大的点对。 Rust 1.75 x64（提交 11323258）的运行时间从 0.031 秒变为 0.015 秒，内存从 308 KB 变为 76 KB。

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11322120 · Go 1.14 x64 №11322121 · Java 1.8 №11322122 · Python 3.12 x64 №11322132 · Rust 1.75 x64 №11322133.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1405_geometry.cpp](1405_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.046 s | 224 KB | 11322120 |
| [1405_geometry.go](1405_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.062 s | 1136 KB | 11322121 |
| [1405_geometry.java](1405_geometry.java) | Java 1.8 | geometry | O(N^2) | AC | 0.14 s | 5548 KB | 11322122 |
| [1405_geometry.py](1405_geometry.py) | Python 3.12 x64 | geometry | O(N^2) | AC | 0.625 s | 1236 KB | 11322132 |
| [1405_geometry.rs](1405_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.031 s | 308 KB | 11322133 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1405_geometry_optimized.cpp](1405_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.015 s | 232 KB | 11317478 |
| [1405_geometry_optimized.go](1405_geometry_optimized.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.031 s | 1016 KB | 11322346 |
| [1405_geometry_optimized.rs](1405_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.015 s | 76 KB | 11323258 |
| [1405_geometry_optimized.py](1405_geometry_optimized.py) | Python 3.12 x64 | geometry | O(N^2) | AC | 0.125 s | 1064 KB | 11317508 |
| [1405_geometry_optimized.java](1405_geometry_optimized.java) | Java 1.8 | geometry | O(N^2) | AC | 0.171 s | 3204 KB | 11317519 |
