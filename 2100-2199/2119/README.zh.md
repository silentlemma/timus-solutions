# 2119. 张成可变顶点集的子树权值

[Timus 2119](https://acm.timus.ru/problem.aspx?space=1&num=2119) · 难度 780 · trees, fenwick

原题作者 Alexey Danilyuk，出自 2018 年夏季彼得罗扎沃茨克集训营 t.me/umnik_team 专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定一棵边带权的树和一个初始为空的顶点集合 A。每个询问向 A 加入一个顶点或从中删除一个顶点。每次询问后输出包含 A 中所有顶点的最小子树的总权值（A 为空时输出 0）。时间限制 5 秒，内存限制 256 MB。

## 输入

n（1 ≤ n ≤ 3 · 10⁵），n − 1 条边 "u v w"（0 ≤ w ≤ 10⁹），然后是 q（1 ≤ q ≤ 3 · 10⁵）以及询问 "+ v" 或 "− v"。只会加入不在 A 中的顶点，只会删除在 A 中的顶点。

## 输出

每次询问后的权值，每行一个。

## 样例

### 样例 1

输入：

```
5
1 2 1
2 3 10
3 4 100
3 5 1000
8
+ 2
+ 5
+ 4
- 5
+ 1
- 4
- 2
- 1
```

输出：

```
0
1010
1110
110
111
1
0
0
```

## 解法

把 A 中的顶点按深度优先搜索的前序编号排序：v₁, v₂, …, vₖ。沿树上路径走 v₁ → v₂ → … → vₖ → v₁，就像绕子树走一圈，所张成子树的每条边恰好经过两次，所以权值是 d(v₁, v₂) + … + d(vₖ, v₁) 的一半。当 v 插入到它在这个顺序中的循环邻居 a 和 b 之间时，总和增加 d(a, v) + d(v, b) − d(a, b)；删除时减去同样的量。

邻居由一棵建在前序位置上、标记 A 中成员的树状数组给出：v 之前被标记的位置数给出 a 的排名，再沿树状数组下降找到给定排名的元素，两端循环衔接。距离用带权深度计算，d(u, v) = D(u) + D(v) − 2 D(LCA)。当 u ≠ v 且 tin(u) < tin(v) 时，LCA 就是前序位置 tin(u) + 1 … tin(v) 上各顶点的父亲中前序编号最小的那个。在这些父亲编号上建稀疏表即可 O(1) 回答。

搜索是迭代的，因为树可能是一条链。权值可达 3 · 10¹⁴，所以总和需要 64 位整数。总时间 O((n + q) log n)。

样例中在 "+ 2"、"+ 5"、"+ 4" 之后，子树是 2 – 3 – 4 加上 3 – 5，权值 10 + 100 + 1000 = 1110。

## 各语言说明

Python 解答在 PyPy 3.10 上运行：同样的循环在 CPython 中需要好几秒。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2119_trees_fenwick.cpp](2119_trees_fenwick.cpp) | G++ 13.2 x64 | trees, fenwick | O((n + q) log n) | AC | 0.343 s | 46600 KB |
| [2119_trees_fenwick.go](2119_trees_fenwick.go) | Go 1.14 x64 | trees, fenwick | O((n + q) log n) | AC | 0.453 s | 47972 KB |
| [2119_trees_fenwick.java](2119_trees_fenwick.java) | Java 1.8 | trees, fenwick | O((n + q) log n) | AC | 0.546 s | 76516 KB |
| [2119_trees_fenwick.py](2119_trees_fenwick.py) | PyPy 3.10 x64 | trees, fenwick | O((n + q) log n) | AC | 1.953 s | 224172 KB |
| [2119_trees_fenwick.rs](2119_trees_fenwick.rs) | Rust 1.75 x64 | trees, fenwick | O((n + q) log n) | AC | 0.406 s | 94224 KB |
