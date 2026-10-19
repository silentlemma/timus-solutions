# 2085. 每种技术恰好用一次的树上路径

[Timus 2085](https://acm.timus.ru/problem.aspx?space=1&num=2085) · 难度 1643 · hashing, trees

原题作者 Alexander Fetisov。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 个项目构成一棵树，每个项目使用 m 种技术中的一个集合。求一条简单路径（可以只有一个项目），使得每种技术恰好出现在路径上的一个项目中，输出其两个端点，或输出 “No solution”。任何正确的路径都可接受。时间限制 5 秒，内存限制 256 MB。

## 输入

n 和 m（1 ≤ n, m ≤ 10⁵），n − 1 条边，然后对每个项目给出其技术数量和编号；所有集合的元素总数不超过 10⁶。

## 输出

路径的两个端点，或 `No solution`。

## 评测方式

检查器只在期望输出为 “No solution” 时接受它，否则沿输出的路径统计技术。

## 样例

### 样例 1

输入：

```
5 3
1 2
1 3
3 4
3 5
1 1
1 3
0
2 1 3
1 2
```

输出：

```
2 5
```

### 样例 2

输入：

```
3 3
1 2
1 3
2 2 3
3 1 2 3
1 3
```

输出：

```
2 2
```

### 样例 3

输入：

```
2 3
1 2
2 1 2
2 1 3
```

输出：

```
No solution
```

## 解法

给每种技术一个随机 64 位权值，每个项目的值为其技术权值之和。在每种技术恰好用一次的路径上，各项目值之和等于全部权值之和 G；若某技术用了两次或缺失，这个和是独立随机数的另一种线性组合，等于 G 的概率只有约 2⁻⁶⁴。于是问题变为：找一条值之和模 2⁶⁴ 等于 G 的路径。

给树定根，记 depth(v) 为从根到 v 的值之和。以最高点 x 为转折的路径 u … v 的和为 depth(u) + depth(v) − 2 depth(x) + value(x)。对每个 x，用哈希表“深度 → 顶点”保存其子树中的顶点，按小并大合并：x 从自己的表 {depth(x)} 开始，每个子节点的表合并进来，小的并入大的。合并前，小表中的每个深度 d 在大表中查找 G + 2 depth(x) − value(x) − d；命中就是经过 x 的路径，因为两侧位于 x 的不同子树中（或一端就是 x）。值为 G 的单个项目本身就是路径。每个顶点只移动 O(log n) 次，所以期望工作量为 O(n log n + Σ aᵢ)。

按广度优先顺序遍历树，回溯时子节点先于父节点处理，所以深树不需要递归。第一个样例中路径 5、3、4 依次使用技术 2、无、1 和 3；样例答案 2 … 5 同样正确。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2085_hashing_trees.cpp](2085_hashing_trees.cpp) | G++ 13.2 x64 | hashing, trees | O(n log n + sum a) | AC | 0.937 s | 23040 KB |
| [2085_hashing_trees.go](2085_hashing_trees.go) | Go 1.14 x64 | hashing, trees | O(n log n + sum a) | AC | 0.343 s | 44040 KB |
| [2085_hashing_trees.java](2085_hashing_trees.java) | Java 1.8 | hashing, trees | O(n log n + sum a) | AC | 0.593 s | 50248 KB |
| [2085_hashing_trees.py](2085_hashing_trees.py) | Python 3.12 x64 | hashing, trees | O(n log n + sum a) | AC | 1.312 s | 101000 KB |
| [2085_hashing_trees.rs](2085_hashing_trees.rs) | Rust 1.75 x64 | hashing, trees | O(n log n + sum a) | AC | 0.156 s | 31624 KB |
