# 2053. 生成含三十多万个环的平面图

[Timus 2053](https://acm.timus.ru/problem.aspx?space=1&num=2053) · difficulty 3448 · constructive

原题作者 Alexander Ipatov，出自 2015 年乌拉尔体育编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

画出一个平面图：十六个顶点位于不同的整点，边为直线段，只在公共端点相交且不经过其他顶点，并且图中的简单环超过 300 000 个。一个环只计一次，与起点和方向无关。时间限制 1 秒，内存限制 64 MB。

## 输入

没有输入。

## 输出

十六行顶点坐标，每个坐标在 [−1000, 1000] 内，然后是由 0 和 1 组成的 16 × 16 邻接矩阵，对称且对角线为零。

## 评测方式

检查器核对点、矩阵和边的几何关系，并精确统计简单环的个数；任何合法的图都被接受。原题的样例只展示格式，并不是正确答案，所以保存的样例输出标记为 `format_only`，不参与检查。

## 样例

这个样例只展示格式：它只有六个顶点、21 个环，所以不是正确答案。

```

```

```
0 0
5 -6
-5 -6
-9 3
0 8
9 3
011111
101001
110100
101010
100101
110010
```

示意图是五点外圈加一个连接所有外点的中心。三角形和更长环共 21 个，既不满足顶点数也不满足环数。下面构造则有 16 个顶点、42 条边，精确包含 301843 个环。

## 解法

### 用算法生成图

在概念上的四乘四网格中按 `v=4r+c` 从零编号。加入所有水平和竖直相邻边，共 24 条；每格再加入左上到右下对角线，共九条。网格只用于命名，不是最终坐标。

四侧顶点序列是 `(0,1,2,3)`、`(3,7,11,15)`、`(15,14,13,12)`、`(12,8,4,0)`。每侧 `(a,b,c,d)` 加边 `a-d` 与 `a-c`，最后加 `3-12`。新增边互不重复，总共 42 条。外三角形使用零、三、十二号顶点。程序通过循环生成边，不存储答案矩阵。

### 计算整数坐标

固定零号点为 `(-900,-900)`、三号点为 `(900,-900)`、十二号点为 `(0,900)`。其余每个点要求等于邻居的平均位置。每个坐标的十三个未知数满足
`degree(v)·p_v - sum_{内部邻居u} p_u = sum_{固定邻居u} p_u`。
构造十三行、两个右端项的增广矩阵，用带主元行选择的高斯消元求解，再以 `floor(value+0.5)` 舍入。

系统非奇异。把内部顶点向量在边界延伸为零，其二次型是内部边上的 `(x_u-x_v)²` 及连向固定边界的 `x_v²` 之和。总和为零使所有相邻值相同且边界为零，连通性迫使全向量为零，所以矩阵正定。最大值原理也限制精确坐标不超固定边界的极值：内部严格最大值不能是平均值，最大平台会沿邻接传播到边界。

一般谐和图直接舍入未必安全。这里图固定，因此对实际整数坐标进行精确验证。有理数消元给出下方可执行证书的十六个点；每个精确坐标与半整数舍入边界至少相距 `513/46262`，小系统的双精度计算具有充分余量。五个实际程序均得到这个整数证书。整数方向与在线段判断确认点不同、范围正确、无点落在无关边内，也无禁止的边交叉；证书任意三点亦不共线。

### 环数证明

设 `DP[M][v]` 为恰访问集合 `M`、终点为 `v`、起点为 `M` 中最小顶点的路径数。初值 `DP[{v}][v]=1`。只向未访问且编号大于起点的相邻点扩展，从而保持最小起点。每条顶点简单路径恰出现一次：删除最后一条边并对长度归纳即可。

集合至少有三个顶点时，路径恰在终点与起点相邻时闭合成简单环。累加这些状态，每个无向环因两个方向出现两次；最小起点已去掉循环起点重复，故除以二。精确验证的直线嵌入没有禁止的交叉或顶点接触，所以图上的简单环恰为合法多边形。

长度三到十六的环数依次为
`28,46,116,365,1140,3174,7922,17578,33714,53732,67908,63842,39852,12426`，
精确总和 `301843>300000`。下面完整有限验证生成图、核验几何并计算所有环长。它是证书检查程序，不是提交程序；提交程序用线性系统计算坐标。

```python
from array import array

GRID = 4
COORDINATE_BOUND = 1000
MIN_CYCLE_LENGTH = 3
points = [(-900, -900), (-275, -647), (12, -731), (900, -900),
          (-258, -48), (-239, -415), (27, -541), (310, -669),
          (-77, 241), (-74, -67), (49, -285), (301, -502),
          (0, 900), (25, 178), (56, -72), (222, -114)]
adjacency = [0] * (GRID * GRID)

def link(a, b):
    adjacency[a] |= 1 << b
    adjacency[b] |= 1 << a

for r in range(GRID):
    for c in range(GRID):
        v = GRID * r + c
        if c + 1 < GRID:
            link(v, v + 1)
        if r + 1 < GRID:
            link(v, v + GRID)
        if r + 1 < GRID and c + 1 < GRID:
            link(v, v + GRID + 1)
corners = [0, GRID - 1, GRID * GRID - 1, GRID * GRID - GRID]
for side, a in enumerate(corners):
    d = corners[(side + 1) % GRID]
    step = (d - a) // (GRID - 1)
    link(a, d)
    link(a, d - step)
link(corners[1], corners[-1])

def orientation(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def on_segment(a, b, p):
    return orientation(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and (min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))

def geometric(points, adjacency):
    size = len(points)
    if len(set(points)) != size or any((abs(x) > COORDINATE_BOUND for p in points for x in p)):
        return False
    edges = [(a, b) for a in range(size) for b in range(a + 1, size) if adjacency[a] & 1 << b]
    for a, b in edges:
        if any((v not in (a, b) and on_segment(points[a], points[b], p) for v, p in enumerate(points))):
            return False
    for index, (a, b) in enumerate(edges):
        for c, d in edges[index + 1:]:
            if len({a, b, c, d}) < 4:
                continue
            pa, pb, pc, pd = (points[a], points[b], points[c], points[d])
            x, y = (orientation(pa, pb, pc), orientation(pa, pb, pd))
            z, w = (orientation(pc, pd, pa), orientation(pc, pd, pb))
            if x * y < 0 and z * w < 0:
                return False
            if on_segment(pa, pb, pc) or on_segment(pa, pb, pd):
                return False
            if on_segment(pc, pd, pa) or on_segment(pc, pd, pb):
                return False
    return True

def cycle_histogram(adjacency):
    size = len(adjacency)
    full = (1 << size) - 1
    paths = array('Q', [0]) * ((1 << size) * size)
    for vertex in range(size):
        paths[(1 << vertex) * size + vertex] = 1
    totals = [0] * (size + 1)
    for mask in range(1, 1 << size):
        anchor = mask & -mask
        allowed = full ^ (anchor << 1) - 1
        length = mask.bit_count()
        endpoints = mask
        while endpoints:
            bit = endpoints & -endpoints
            endpoints ^= bit
            last = bit.bit_length() - 1
            value = paths[mask * size + last]
            if not value:
                continue
            if length >= MIN_CYCLE_LENGTH and adjacency[last] & anchor:
                totals[length] += value
            choices = adjacency[last] & ~mask & allowed
            while choices:
                new_bit = choices & -choices
                choices ^= new_bit
                end = new_bit.bit_length() - 1
                paths[(mask | new_bit) * size + end] += value
    return [value // 2 for value in totals]

assert geometric(points, adjacency)
histogram = cycle_histogram(adjacency)
assert histogram[3:] == [28, 46, 116, 365, 1140, 3174, 7922,
                        17578, 33714, 53732, 67908, 63842, 39852, 12426]
assert sum(histogram) == 301843 > 300000
```

所有断言均成立。独立的顶点简单路径 DFS 也枚举出相同直方图；不是凭随机测试或只数面数推断环数。

不能提交六点格式图，也不能只数三角形、面或哈密顿环。数量条件是严格大于。对称矩阵本身不能保证合法嵌入，还须检查点在线段上、非关联边交叉及共线重叠。网格只是编号方案，最终加边配旧网格坐标会交叉。保留三个固定外点，对负坐标也统一使用 `floor(x+0.5)`。每个环按循环移动及反向等价只计一次。

## 各语言说明

提交程序生成图并解 `V-3` 阶系统，时间 `O(V^3)`、空间 `O(V^2)`，其中固定 `V=16`；运行时不数环。独立证书检查器需要 `O(V^2·2^V)` 时间、`O(V·2^V)` 空间，十六个顶点的路径表占八 MiB。

各版本使用双精度消元并输出整数。Java、Rust 使用基本数值数组，C++、Go 使用固定图数组。无需输入解析或预存坐标表。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2053_constructive.cpp](2053_constructive.cpp) | G++ 13.2 x64 | constructive | O(V^3) | AC | 0.001 s | 356 KB |
| [2053_constructive.go](2053_constructive.go) | Go 1.14 x64 | constructive | O(V^3) | AC | 0.001 s | 1024 KB |
| [2053_constructive.java](2053_constructive.java) | Java 1.8 | constructive | O(V^3) | AC | 0.015 s | 368 KB |
| [2053_constructive.py](2053_constructive.py) | Python 3.12 x64 | constructive | O(V^3) | AC | 0.062 s | 668 KB |
| [2053_constructive.rs](2053_constructive.rs) | Rust 1.75 x64 | constructive | O(V^3) | AC | 0.001 s | 204 KB |
