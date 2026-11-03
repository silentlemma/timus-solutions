# 1444. 喂饱象河马

[Timus 1444](https://acm.timus.ru/problem.aspx?space=1&num=1444) · 难度 262 · geometry

原题由 Ekaterina Vasilyeva（构思与题面）以及 Alexander Mironenko、Alexey Lakhtin 和 Den Raskovalov（程序）完成，出自 2006 年 3 月 24–25 日第十届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 个南瓜（3 ≤ N ≤ 30000）位于互不相同的整点上，坐标在 −1000 到 1000 之间，并且
不全在一条直线上。象河马从 1 号南瓜出发并吃掉它；每吃完一个南瓜，可以让它沿直线
走向任意一个剩下的南瓜。这种动物一踩到自己的足迹就会永远停下，所以路线不能与自
身接触。求最多能吃掉的南瓜数 K 以及从 1 开始的吃南瓜顺序。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

N，然后是 1 到 N 号南瓜的坐标。

## 输出

K，然后按吃的顺序给出南瓜编号，每行一个。任何正确的路线都被接受。

## 评测方式

接受从第一点开始的任意最大遍历，点编号互异，路径不自交也不自触。

## 样例

### 样例 1

输入:

```
4
0 0
10 10
0 10
10 0
```

输出:

```
4
1
3
2
4
```

## 解法

总能吃掉全部 N 个南瓜。把其余南瓜按从 1 号南瓜出发的方向角排序，同一条射线上按
距离排序，近的在前；比较使用整数叉积，因此是精确的。按这个顺序行走，就像扇子一样
绕着 1 号南瓜扫过：每一步要么沿同一射线继续向外，要么转到下一个方向，所以路线每
时每刻都在一个窄扇形之内，永远不会回头。

唯一的危险在圆周的起点。若相邻两个方向相差半圈或更多，它们之间的一步可能经过 1
号南瓜或穿过之前的步子，所以就在这个间隙之后切开圆周；由于南瓜不全共线，这样的
间隙至多一个。没有这样的间隙时，可以在任意两个相邻且方向不同的射线组之间切开，
并从下一组最近的南瓜开始。不能把同一射线组分到切口两侧，否则最后回到该射线上
较近的南瓜时会碰到最初的线段。代码默认在角度排序的开头切开，已经满足这一要求。
`O(N log N)`。

注意事项：

- 同一射线上的多个南瓜要由近到远吃（测试 03、06、gen2）；
- 选择切口时要保持每个射线组完整，即使所有角度间隙都小于半圈（测试 06）；
- 南瓜沿一条直线分布在 1 号南瓜两侧时，会出现恰好半圈的间隙（测试 03、09）；
- 1 号南瓜在角落时会留下超过半圈的间隙（测试 04、gen3、gen4）。

## 优化解法

排序使用精确打包整数方向键，避免反复比较叉积。基于曼哈顿长度的有理参数沿圆周单调变化。坐标上界保证不同分数的最小间隔，因此放大取整不会合并不同方向。键包含方向秩、距离平方及原编号，同射线仍按由近到远排列。角度间隙给出与基础证明相同的循环切点，不计算浮点角度。

- `1444_geometry_optimized.cpp`: 0.015 s / 320 KB; 基础版 `1444_geometry.cpp`: 0.062 s / 444 KB; 相对基础版的变化: 时间 -75.8%, 内存 -27.9%.
- `1444_geometry_optimized.go`: 0.031 s / 1188 KB; 基础版 `1444_geometry.go`: 0.078 s / 2336 KB; 相对基础版的变化: 时间 -60.3%, 内存 -49.1%.
- `1444_geometry_optimized.java`: 0.093 s / 736 KB; 基础版 `1444_geometry.java`: 0.187 s / 6232 KB; 相对基础版的变化: 时间 -50.3%, 内存 -88.2%.
- `1444_geometry_optimized.py`: 0.171 s / 3976 KB; 基础版 `1444_geometry.py`: 0.453 s / 11600 KB; 相对基础版的变化: 时间 -62.3%, 内存 -65.7%.
- `1444_geometry_optimized.rs`: 0.046 s / 1244 KB; 基础版 `1444_geometry.rs`: 0.031 s / 2104 KB; 相对基础版的变化: 时间 +48.4%, 内存 -40.9%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1444_geometry.cpp`; 覆盖实现 `1444_geometry_optimized.cpp`; 时间/内存名次 1/10, 其他作者记录 352/352.

- Go: 优先教学基础版 `1444_geometry.go`; 覆盖实现 `1444_geometry_optimized.go`; 时间/内存名次 1/1, 其他作者记录 4/4.

- Java: 优先教学基础版 `1444_geometry.java`; 覆盖实现 `1444_geometry_optimized.java`; 时间/内存名次 1/1, 其他作者记录 6/6.

- Python/PyPy: 优先教学基础版 `1444_geometry.py`; 覆盖实现 `1444_geometry_optimized.py`; 时间/内存名次 13/1, 其他作者记录 59/59.

- Rust: 优先教学基础版 `1444_geometry.rs`; 覆盖实现 `1444_geometry_optimized.rs`; 时间/内存名次 1/2, 其他作者记录 1/1.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1444_geometry.cpp](1444_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.062 s | 444 KB | 11286284 |
| [1444_geometry.go](1444_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.078 s | 2336 KB | 11286286 |
| [1444_geometry.java](1444_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.187 s | 6232 KB | 11286290 |
| [1444_geometry.py](1444_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.453 s | 11600 KB | 11286289 |
| [1444_geometry.rs](1444_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 2104 KB | 11286291 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1444_geometry_optimized.cpp](1444_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 320 KB | 11309261 |
| [1444_geometry_optimized.go](1444_geometry_optimized.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1188 KB | 11309263 |
| [1444_geometry_optimized.java](1444_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.093 s | 736 KB | 11309262 |
| [1444_geometry_optimized.py](1444_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(N log N) | AC | 0.171 s | 3976 KB | 11309260 |
| [1444_geometry_optimized.rs](1444_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.046 s | 1244 KB | 11309264 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
