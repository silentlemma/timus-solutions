# 2122. 各长度子序列之间的汉明距离总和

[Timus 2122](https://acm.timus.ru/problem.aspx?space=1&num=2122) · 难度 4225 · math, combinatorics

原题作者 Alexey Danilyuk 和 Oleg Merkurev，出自 2018 年夏季彼得罗扎沃茨克集训营 t.me/umnik_team 专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对长度为 n 的二进制串 s 以及从 1 到 n 的每个 k，取所有长度为 k 的子序列（按位置选取），把它们所有无序对之间的汉明距离加起来。输出这 n 个和对 40 961 取模的结果。时间限制 4 秒，内存限制 256 MB。

## 输入

字符串 s（1 ≤ n ≤ 4000）。

## 输出

n 个数，即 k = 1 … n 时的和对 40 961 取模。

## 样例

### 样例 1

输入：

```
11000110111001
```

输出：

```
48 4056 15326 31033 20654 29362 32472 13700 21357 12217 20411 12456 212 0
```

### 样例 2

输入：

```
000
```

输出：

```
0 0 0
```

## 解法

固定 k 和子序列中的位置 j。若 C(n, k) 个子序列中有 c_j 个在位置 j 上是 1，则这个位置贡献 c_j · (C(n, k) − c_j) 对不同。对 j 求和，

answer(k) = C(n, k) · Σ c_j − Σ c_j²。

Σ c_j 统计所有子序列中 1 的总数，而 s 中的每个 1 出现在其中 C(n − 1, k − 1) 个子序列里，所以 Σ c_j = （1 的个数）· C(n − 1, k − 1)。只有 Σ c_j² 需要计算。

不去选择位置，而是一个一个地删除 n − k 个位置。这样每个子序列出现 (n − k)! 次，每种删除顺序一次，令 r_k(j) = c_j · (n − k)! 统计删除顺序。从长度 k + 1 到 k（位置从 0 开始）时，删除后面 k − j 个元素之一，位置 j 上的元素保持不动；删除前 j + 1 个元素之一，位置 j + 1 上的元素移到 j：

r_k(j) = (k − j) · r_{k+1}(j) + (j + 1) · r_{k+1}(j + 1)。

从 r_n = s 开始，每个长度用时 O(k)，总共 O(n²)。其余各项也按同样方式缩放，最后整个表达式除以 ((n − k)!)²。模数 40 961 是大于 4000 的质数，所以这些阶乘都可逆。

第二个样例中所有子序列都相同，所以每个和都是 0。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2122_math_combinatorics.cpp](2122_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(n^2) | AC | 0.031 s | 464 KB |
| [2122_math_combinatorics.go](2122_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(n^2) | AC | 0.046 s | 1272 KB |
| [2122_math_combinatorics.java](2122_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(n^2) | AC | 0.156 s | 740 KB |
| [2122_math_combinatorics.py](2122_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(n^2) | AC | 3.453 s | 1228 KB |
| [2122_math_combinatorics.rs](2122_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(n^2) | AC | 0.015 s | 308 KB |
