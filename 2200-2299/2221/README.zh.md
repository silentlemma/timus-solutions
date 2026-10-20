# 2221. 点集笛卡尔树每棵子树的凸包大小

[Timus 2221](https://acm.timus.ru/problem.aspx?space=1&num=2221) · 难度 1127 · geometry, trees

原题作者 Vadim Barinov，出自 2025 年 ICPC 乌拉尔赛区资格赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 个横坐标互不相同、纵坐标互不相同的点被递归划分：一个集合中最高的点是它的代表，其左侧和右侧的点各组成一个新集合。对每个点，输出它所代表的集合的凸包顶点数（单点为 1，线段为 2）。时间限制 2 秒，内存限制 512 MB。

## 输入

N（1 ≤ N ≤ 10⁵），然后是坐标绝对值不超过 10⁹ 的各点。

## 输出

按输入顺序输出每个点对应的凸包大小。

## 样例

### 样例 1

输入：

```
5
0 0
6 4
4 7
8 9
12 1
```

输出：

```
1
1
3
4
1
```

## 解法

这种划分恰好是以 x 为键、y 为堆优先级的笛卡尔树，按 x 排序后用栈构造；代表的集合就是它的子树，是 x 上连续的一段。

子树的凸包由下链和上链组成，按 Andrew 单调链的方式构造。不在孩子集合凸包上的点不可能在父亲集合的凸包上，所以父亲只需要孩子们的链和自己这个点。自下而上，父亲把较大孩子的链作为链表保留，先插入代表点，再从链表较近的一端插入较小孩子链上的点：基链是左孩子时在右端追加，是右孩子时在左端前插。每次插入都会弹出不再构成严格转向的点，因此共线的点被去掉。

小并入大意味着每个点被插入 O(log n) 次，弹出次数不超过插入次数。凸包大小是下链长度加上链长度减去两个公共端点，且至少为 1。

样例中最高的点 (8, 9) 是全部五个点的代表，其凸包有 4 个顶点；(4, 7) 是它左侧三个点的代表，构成三角形。

复杂度 O(n log n)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2221_geometry_trees.cpp](2221_geometry_trees.cpp) | G++ 13.2 x64 | geometry, trees | O(n log n) | AC | 0.093 s | 6508 KB |
| [2221_geometry_trees.go](2221_geometry_trees.go) | Go 1.14 x64 | geometry, trees | O(n log n) | AC | 0.109 s | 21892 KB |
| [2221_geometry_trees.java](2221_geometry_trees.java) | Java 1.8 | geometry, trees | O(n log n) | AC | 0.328 s | 12136 KB |
| [2221_geometry_trees.py](2221_geometry_trees.py) | Python 3.12 x64 | geometry, trees | O(n log n) | AC | 0.859 s | 45392 KB |
| [2221_geometry_trees.rs](2221_geometry_trees.rs) | Rust 1.75 x64 | geometry, trees | O(n log n) | AC | 0.078 s | 15152 KB |
