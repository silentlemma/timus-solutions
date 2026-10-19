# 2120. 部分度数固定的随机带标号树的期望权值

[Timus 2120](https://acm.timus.ru/problem.aspx?space=1&num=2120) · 难度 1911 · math, probability

原题作者 Alexey Danilyuk，出自 2018 年夏季彼得罗扎沃茨克集训营 t.me/umnik_team 专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

顶点为 1 … n 的树的权值定义为对所有边 (u, v) 求 u · s(u) + v · s(v) 之和，其中 s(u) 是删去这条边后 u 所在部分的大小。一部分顶点的度数固定，其余顶点度数任意。在具有这些度数的树中等概率随机选一棵，输出其权值期望的整数部分。时间限制 2 秒，内存限制 64 MB。

## 输入

n（2 ≤ n ≤ 10⁶），然后是 a₁ … aₙ：从 1 到 n − 1 的固定度数，或表示任意度数的 −1。所有 |aᵢ| 之和不超过 2n − 2。

## 输出

权值期望的整数部分。

## 样例

### 样例 1

输入：

```
5
1 -1 -1 -1 -1
```

输出：

```
67
```

### 样例 2

输入：

```
5
-1 -1 -1 -1 1
```

输出：

```
52
```

### 样例 3

输入：

```
4
1 1 1 3
```

输出：

```
42
```

### 样例 4

输入：

```
4
1 1 2 2
```

输出：

```
38
```

## 解法

按顶点归并各项。删去顶点 v 的 d 条边，把其余 n − 1 个顶点分成 d 个分支，在每条边上 v 一侧保留除该分支外的所有顶点，所以 v 各条边上的 s(v) 之和为 d · n − (n − 1)。因此权值只依赖于度数：

W = Σ v · (n (d_v − 1) + 1) = n(n + 1)/2 + n · Σ v (d_v − 1)。

由 Prüfer 序列，度数为 d₁ … dₙ 的树的个数为 (n − 2)! / ∏ (d_v − 1)!，自由顶点之间交换度数时它不变。所以所有自由顶点的 d_v − 1 期望相同，且这些值之和为 R = n − 2 − Σ (固定的 d_v − 1)。设有 c 个自由顶点，其编号之和为 S，由期望的线性性得

E = n(n + 1)/2 + n · Σ_固定 v (d_v − 1) + n · R · S / c。

只有最后一项是分数；用整数除法精确求出它的整数部分，先把 R · S 对 c 做带余除法，以保持在 64 位之内。工作量 O(n)。

第三个样例中所有度数都固定，Σ v (d_v − 1) = 4 · 2 = 8，W = 10 + 4 · 8 = 42。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2120_math_probability.cpp](2120_math_probability.cpp) | G++ 13.2 x64 | math, probability | O(n) | AC | 0.156 s | 448 KB |
| [2120_math_probability.go](2120_math_probability.go) | Go 1.14 x64 | math, probability | O(n) | AC | 0.062 s | 1088 KB |
| [2120_math_probability.java](2120_math_probability.java) | Java 1.8 | math, probability | O(n) | AC | 0.171 s | 572 KB |
| [2120_math_probability.py](2120_math_probability.py) | Python 3.12 x64 | math, probability | O(n) | AC | 0.468 s | 3036 KB |
| [2120_math_probability.rs](2120_math_probability.rs) | Rust 1.75 x64 | math, probability | O(n) | AC | 0.015 s | 280 KB |
