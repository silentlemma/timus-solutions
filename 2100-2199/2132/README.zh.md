# 2132. 把图的边分成相邻的边对

[Timus 2132](https://acm.timus.ru/problem.aspx?space=1&num=2132) · 难度 1528 · graphs, constructive

原题作者 Alexander Petrov（由 Alexander Ipatov 整理），出自 “迟到总比不到好”专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给出一个边数为偶数的简单图的边表。把所有边分成若干对有公共顶点的边，或者报告无法做到。任何合法的划分都可接受。时间限制 1 秒，内存限制 128 MB。

## 输入

顶点编号对，每条边一对：边数为 2 到 10⁵ 之间的偶数，顶点编号从 1 到 10⁵。

## 输出

对数 m 和 m 个三元组 a b c，表示边 {a, b} 和 {b, c}，或者 −1。

## 评测方式

检查器验证这些三元组恰好把每条边用了一次。

## 样例

### 样例 1

输入：

```
1 2
2 3
3 1
1 10
```

输出：

```
2
1 2 3
3 1 10
```

### 样例 2

输入：

```
1 2
2 3
3 1
4 10
```

输出：

```
-1
```

## 解法

不同连通分量中的边不能配对，所以只要有一个分量的边数为奇数，答案就是 −1。边数为偶数的连通图总能划分，下面的构造说明了这一点。

用搜索为每个分量建一棵生成树，并按每个顶点都排在其所有后代之后的顺序处理顶点。每条非树边分给它的一个端点，即先被处理的那个。在顶点 v 处，收集到孩子的仍空闲的边以及分给 v 的非树边，两两通过 v 配对。若剩下一条边，就把它与 v 到父亲的边配对，父边随之被占用；否则父边保持空闲，留给父亲使用。若某个分量的根剩下一条边，说明该分量的边数为奇数。搜索是迭代的，总时间 O(V + E)。

第二个样例中三角形 1 – 2 – 3 有三条边，而边 4 – 10 单独一条，所以不存在划分。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2132_graphs_constructive.cpp](2132_graphs_constructive.cpp) | G++ 13.2 x64 | graphs, constructive | O(V + E) | AC | 0.109 s | 7376 KB |
| [2132_graphs_constructive.go](2132_graphs_constructive.go) | Go 1.14 x64 | graphs, constructive | O(V + E) | AC | 0.078 s | 21920 KB |
| [2132_graphs_constructive.java](2132_graphs_constructive.java) | Java 1.8 | graphs, constructive | O(V + E) | AC | 0.156 s | 8900 KB |
| [2132_graphs_constructive.py](2132_graphs_constructive.py) | Python 3.12 x64 | graphs, constructive | O(V + E) | AC | 0.359 s | 30520 KB |
| [2132_graphs_constructive.rs](2132_graphs_constructive.rs) | Rust 1.75 x64 | graphs, constructive | O(V + E) | AC | 0.046 s | 12784 KB |
