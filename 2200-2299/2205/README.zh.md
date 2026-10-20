# 2205. 最大真因数树中的最近公共祖先

[Timus 2205](https://acm.timus.ru/problem.aspx?space=1&num=2205) · 难度 1462 · number_theory

原题作者 Vadim Barinov，出自 2022 年大学学术中学生信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

两个不同的自然数相连，当且仅当其中一个是另一个的最大真因数。路径是一列互不相同的数，相邻两数相连，路径的代价是其中最小的数。对 N 对 (a, b) 中的每一对，输出从 a 到 b 的路径的最大代价，若不存在路径则输出 −1。时间限制 2 秒，内存限制 256 MB。

## 输入

N（1 ≤ N ≤ 5 · 10⁵），然后是 N 对数，1 ≤ a, b ≤ 10⁷。

## 输出

每一对的答案。

## 样例

### 样例 1

输入：

```
3
4 4
4 5
4 6
```

输出：

```
4
1
1
```

## 解法

n > 1 的最大真因数是 n / p，其中 p 是它的最小质因数，所以每个大于 1 的数恰有一个更小的邻居：这些连接构成以 1 为根的树，每对数之间恰有一条路径。越靠近根值越小，所以路径上最小的数就是最近公共祖先，−1 不会出现。

把 a 的质因数按降序写出。a 的祖先逐个去掉最小的因数，所以恰好是这个列表前若干个因数的乘积。因此公共祖先是两个降序列表的最长公共前缀的乘积。

这个乘积可以从 g = gcd(a, b) 得到。设 t 为 a / g 或 b / g 的最大质因数。每个大于 t 的质数在 a 和 b 中的指数相同，而 t 本身在 g 中的指数是两者中较小的那个，两个列表正是在这里开始不同。小于 t 的部分列表已经分开。所以答案是从 g 中去掉所有小于 t 的质因数；a = b 时答案为 a 本身，g = 1 时为 1。

只对奇数保存的、到 10⁷ 的最小奇质因数筛给出任意数的分解，2 的幂用位运算技巧去掉。

样例中 4 = 2 · 2 和 6 = 3 · 2 在最大因数上就不同，所以它们的公共祖先是 1。

筛法需要 O(V log log V)（V = 10⁷），每个查询 O(log V)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2205_number_theory.cpp](2205_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(V log log V + N log V) | AC | 0.343 s | 13416 KB |
| [2205_number_theory.go](2205_number_theory.go) | Go 1.14 x64 | number_theory | O(V log log V + N log V) | AC | 0.312 s | 54196 KB |
| [2205_number_theory.java](2205_number_theory.java) | Java 1.8 | number_theory | O(V log log V + N log V) | AC | 0.390 s | 19488 KB |
| [2205_number_theory.py](2205_number_theory.py) | PyPy 3.10 x64 | number_theory | O(V log log V + N log V) | AC | 1.921 s | 109108 KB |
| [2205_number_theory.rs](2205_number_theory.rs) | Rust 1.75 x64 | number_theory | O(V log log V + N log V) | AC | 0.234 s | 36432 KB |
