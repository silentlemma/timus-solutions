# 1052. 一条直线上最多的点

[Timus 1052](https://acm.timus.ru/problem.aspx?space=1&num=1052) · 难度 239 · geometry, sorting

原题作者 Stanislav Vasiliev，出自 2000 年 3 月 25 日乌拉尔国立大学大学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 `N` 个互不相同的点（`3 ≤ N ≤ 200`），坐标为 −2000 到 2000 的整数。求最多有多少个点位于同一条直线上。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`，然后 `N` 行，每行 `x` 和 `y`。

## 输出

一条直线上最多的点数。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
6
7 122
8 139
9 156
10 173
11 190
-100 1
```

输出：

```
5
```

### 样例 2

输入：

```
3
0 0
1 0
0 1
```

输出：

```
2
```

## 解法

枚举每对不同输入点 `i,j`，它们确定一条直线。用精确等式 `(x[k]−x[i])·(y[j]−y[i]) = (y[k]−y[i])·(x[j]−x[i])` 统计线上的所有点 `k`，取最大计数。最优直线至少经过两个输入点，因此必然被某对枚举到；反过来，每个被计入的点确实在线上。这证明最大值就是答案。

直接的 `geometry_bruteforce` 是五种语言首选的简单版本。时间 `O(N³)`，`N=200` 时至多检查 3,980,000 次；输入存储占 `O(N)` 空间。若某条线已包含全部 `N` 个点，答案最优，可以立即结束。坐标差绝对值至多 4000，每个乘积绝对值至多 16,000,000，适合有符号 32 位整数。不需要浮点斜率、除法或 gcd 归一化。

竖直、水平、相反方向和非常接近的斜率都用同一等式处理。输入点互异，所选向量不会为零；答案至少为二。直接实现均已通过评测，局部测试还与独立的规范直线方程算法对照。

## 优化解法

保留的方向计数算法固定一个锚点，把每个 `(dx,dy)` 除以 `gcd(|dx|,|dy|)`。翻转符号使 `dx>0` 或 `dx=0,dy>0`，相反向量就有同一表示。相同方向与锚点在同一条线上。只统计输入顺序靠后的点即可，因为最优直线上最早的点仍能看到其余所有点。

哈希表版本的期望时间为 `O(N² log C)`、工作空间 `O(N)`，`C=4000` 限制坐标差。C++ 使用有序 `std::map`，包含其操作的时间界为 `O(N²(log N+log C))`。不把哈希表最坏查询时间视为常数。

相对新的简单基础版本，未改动的 Python 方向计数文件被列为优化版：其 CPython Accepted 为 0.078 s、508 KB，简单 PyPy 为 0.250 s、2840 KB，时间降低 68.8%，内存降低 82.1%。比较同时包含算法和解释器影响；表中明确列出接受时的运行环境。旧原生语言方向表实现保留为额外的已接受算法，但相对各自的新简单基础版本没有达到 30% 的实测优势。一个计时刻度不能作为准入理由。

新的 Rust `geometry_sorting` 同样精确归一化方向，然后排序固定数组并统计相等段。
它以确定性的 `O(N²(log N+log C))` 时间和 `O(N)` 空间替代旧哈希表。
最优直线上最早输入的点能看到其余所有点；若含锚点在内的剩余点不超过 `best`，便不可能改进答案。
两个各含 200 个坐标/方向对的数组和有界原始 I/O 缓冲区不使用堆；C ABI 入口省去未使用的 Rust 启动和格式化设施。
独立 Accepted 为 0.015 s / 52 KB，首选三次复杂度 Rust 为 0.031 s / 212 KB，内存减少 75.5%。
时间仅相差一个评测刻度，不作为准入依据。除仓库测试外，还把有符号 3×3 网格中所有至少含两点的 466 个子集
与独立的点对叉积算法逐一对照。

## 各语言说明

三次复杂度 Python 使用 PyPy 3.10 通过，方向计数使用 CPython 3.12。其他简单实现采用普通评测编译器和标准输入。方向计数中 C++ 使用 `std::map`，Go/Rust 使用哈希表，Python 使用 `Counter`，Java 使用 `HashMap`，其方向键 `dx·8192+dy` 在 `|dy|≤4000` 时无冲突。

## 解答

### 简单版本

前五行是首选简单实现；后四行保留旧原生语言方向表算法供比较。

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1052_geometry_bruteforce.cpp](1052_geometry_bruteforce.cpp) | G++ 13.2 x64 | geometry, bruteforce | O(N³) | AC | 0.015 s | 108 KB | 11308047 |
| [1052_geometry_bruteforce.go](1052_geometry_bruteforce.go) | Go 1.14 x64 | geometry, bruteforce | O(N³) | AC | 0.031 s | 1076 KB | 11308048 |
| [1052_geometry_bruteforce.java](1052_geometry_bruteforce.java) | Java 1.8 | geometry, bruteforce | O(N³) | AC | 0.125 s | 452 KB | 11308050 |
| [1052_geometry_bruteforce.py](1052_geometry_bruteforce.py) | PyPy 3.10 x64 | geometry, bruteforce | O(N³) | AC | 0.250 s | 2840 KB | 11308046 |
| [1052_geometry_bruteforce.rs](1052_geometry_bruteforce.rs) | Rust 1.75 x64 | geometry, bruteforce | O(N³) | AC | 0.031 s | 212 KB | 11308054 |
| [1052_geometry.cpp](1052_geometry.cpp) | G++ 13.2 x64 | geometry | O(N²(log N+log C)) | AC | 0.001 s | 208 KB | 11278696 |
| [1052_geometry.go](1052_geometry.go) | Go 1.14 x64 | geometry | O(N² log C) expected | AC | 0.015 s | 3264 KB | 11278697 |
| [1052_geometry.java](1052_geometry.java) | Java 1.8 | geometry | O(N² log C) expected | AC | 0.156 s | 4180 KB | 11278700 |
| [1052_geometry.rs](1052_geometry.rs) | Rust 1.75 x64 | geometry | O(N² log C) expected | AC | 0.015 s | 412 KB | 11278703 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1052_geometry.py](1052_geometry.py) | Python 3.12 x64 | geometry | O(N² log C) expected | AC | 0.078 s | 508 KB | 11278698 |
| [1052_geometry_sorting.rs](1052_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O(N²(log N+log C)) | AC | 0.015 s | 52 KB | 11309709 |
