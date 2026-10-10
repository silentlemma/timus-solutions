# 1142. 统计 N 个对象允许并列的排序方式数

[Timus 1142](https://acm.timus.ru/problem.aspx?space=1&num=1142) · 难度 154 · combinatorics

原题来自 Timus，未注明作者和出处。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

`N` 个可比较的对象中任意两个之间满足 `a = b`、`a < b`、`b < a` 之一。
统计在这种意义下（允许相等）排列 `N` 个对象的不同方式数：三个对象有 13
种，从 `a = b = c` 到 `c < b < a`。对若干个 2 到 10 之间的 `N` 作答；输入以
`-1` 结束。

时间限制：1 秒。内存限制：64 MB。

## 输入

若干个 `N`，每行一个，最后是 `-1`。

## 输出

每个 `N` 对应的数目，每行一个。

## 样例

### 样例 1

输入：

```
2
3
-1
```

输出：

```
3
13
```

## 解法

允许并列的排序就是一列由相等对象组成的组，各组严格递增。看第一组：它是
任意一个含 `k` 个对象的非空集合，有 `C(n, k)` 种选法，剩下的 `n − k` 个对象
自己构成一个允许并列的排序。所以令 `a(0) = 1`，

`a(n) = Σ_{k=1..n} C(n, k)·a(n − k)`。

这就是有序贝尔数（Fubini 数）1, 1, 3, 13, 75, 541, …；需要的最大值
`a(10) = 102247563` 在 32 位范围内。用帕斯卡三角形一次建好表，每个询问只需
查表。建表 `O(10²)`。

注意事项：

- 输入没有给出个数，要读到 `-1` 为止；
- 同一个 `N` 可能被询问多次。

这些值已与独立的公式 `a(n) = Σ k!·S(n, k)`（第二类斯特林数）比对，`n ≤ 6`
时还与列举全部排序的结果比对。

## 各语言说明

- 所有语言都在读入询问之前建好同一张表。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1142_combinatorics.cpp](1142_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(1) per query | AC | 0.001 s | 128 KB |
| [1142_combinatorics.go](1142_combinatorics.go) | Go 1.14 x64 | combinatorics | O(1) per query | AC | 0.001 s | 1084 KB |
| [1142_combinatorics.java](1142_combinatorics.java) | Java 1.8 | combinatorics | O(1) per query | AC | 0.093 s | 1604 KB |
| [1142_combinatorics.py](1142_combinatorics.py) | Python 3.12 x64 | combinatorics | O(1) per query | AC | 0.031 s | 436 KB |
| [1142_combinatorics.rs](1142_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(1) per query | AC | 0.001 s | 220 KB |
