# 1142. 统计 N 个对象允许并列的排序方式数

[Timus 1142](https://acm.timus.ru/problem.aspx?space=1&num=1142) · 难度 155 · combinatorics

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

## 优化解法

优化的 Java 解法用基于 `BufferedReader` 的 `StreamTokenizer` 读入询问，而不是
`Scanner`，后者的正则表达式机制加载起来既费时间又占内存；每个答案都立即通过带缓
冲的 `PrintWriter` 输出，而不是先把全部答案收集到 `StringBuilder` 中：
{1142_combinatorics_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1142_combinatorics_optimized.java`: 时间降低 -34.41%; 内存降低 +74.81%; 基础版本: `1142_combinatorics.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1142_combinatorics.cpp](1142_combinatorics.cpp).
- [1142_combinatorics.go](1142_combinatorics.go).
- [1142_combinatorics.rs](1142_combinatorics.rs).

- 所有语言都在读入询问之前建好同一张表。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1142_combinatorics.cpp](1142_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(1) per query | AC | 0.001 s | 128 KB | 11279451 |
| [1142_combinatorics.go](1142_combinatorics.go) | Go 1.14 x64 | combinatorics | O(1) per query | AC | 0.001 s | 1084 KB | 11279453 |
| [1142_combinatorics.java](1142_combinatorics.java) | Java 1.8 | combinatorics | O(1) per query | AC | 0.093 s | 1604 KB | 11279455 |
| [1142_combinatorics.py](1142_combinatorics.py) | Python 3.12 x64 | combinatorics | O(1) per query | AC | 0.031 s | 436 KB | 11279454 |
| [1142_combinatorics.rs](1142_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(1) per query | AC | 0.001 s | 220 KB | 11279457 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1142_combinatorics_optimized.java](1142_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O(1) per query | AC | 0.125 s | 404 KB | 11305854 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
