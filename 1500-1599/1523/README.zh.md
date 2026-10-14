# 1523. K-逆序

[Timus 1523](https://acm.timus.ru/problem.aspx?space=1&num=1523) · 难度 296 · fenwick

原题作者 Dmitry Gozman，出自 2007 年 1 月彼得罗扎沃茨克冬季集训的 Dmitry Gozman Contest 1。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 1 … n 的一个排列 a1, …, an（1 ≤ n ≤ 20000），统计它的 k-逆序（2 ≤ k ≤ 10）：满
足 ai1 > ai2 > … > aik 的下标序列 i1 < i2 < … < ik。输出数目模 10⁹。

时间限制：1 秒。内存限制：64 MB。

## 输入

n 和 k，然后是排列。

## 输出

k-逆序的数目模 10⁹。

## 样例

### 样例 1

输入:

```
3 2
3 1 2
```

输出:

```
2
```

### 样例 2

输入:

```
5 3
5 4 3 2 1
```

输出:

```
10
```

## 解法

设 ends[i] 为在位置 i 结束的长度为 L 的递减序列数；L = 1 时处处为 1。在 i 结束的长
度为 L + 1 的序列，是在更早位置 p（ap > ai）结束的长度为 L 的序列后面接上 i。所以每
一层是一次从左到右的扫描，用按值的树状数组：查询大于 ai 的值的和，再在 ai 处加上
ends[i]。把值从大到小编号，“大于”就变成前缀。k − 1 次扫描，共 `O(n·k·log n)`。

注意事项：

- k 可能超过最长递减序列的长度，甚至超过 n，这时答案为 0（测试 04、05、gen3）；
- 数目增长如 C(20000, 10)，所以累加时要取模 10⁹（gen2、gen5）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1523_fenwick.cpp](1523_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 596 KB |
| [1523_fenwick.go](1523_fenwick.go) | Go 1.14 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 4576 KB |
| [1523_fenwick.java](1523_fenwick.java) | Java 1.8 | fenwick | O(n * k * log n) | AC | 0.125 s | 3512 KB |
| [1523_fenwick.py](1523_fenwick.py) | Python 3.12 x64 | fenwick | O(n * k * log n) | AC | 0.562 s | 5172 KB |
| [1523_fenwick.rs](1523_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 1292 KB |
