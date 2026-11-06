# 1090. 跳得最多的一排新兵：统计逆序对

[Timus 1090](https://acm.timus.ru/problem.aspx?space=1&num=1090) · 难度 366 · fenwick, binary_search

原题作者 Nikita Shamgunov，出自 2001 年 3 月 USU Open Collegiate Programming Contest（Senior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 `K` 排（`1 ≤ K ≤ 20`），每排 `N` 名新兵（`2 ≤ N ≤ 10000`），按身高从 1（最高）到 `N` 编号；每排是 `1 … N` 的
一个排列。每名新兵对站在他前面、编号比他大的每个人各跳一次。输出总跳跃次数最多的那一排；相同时输出编号最小的。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

`N` 和 `K`，然后 `K` 行，每行 `N` 个数。

## 输出

排的编号。

## 评测方式

按记号逐个比较输出；多余的空白不影响结果。

## 样例

### 样例 1

输入：

```
3 3
1 2 3
2 1 3
3 2 1
```

输出：

```
3
```

## 题解

一排的总跳跃次数就是排列的逆序对数：满足 `i < j` 且 `a[i] > a[j]` 的位置对。`N = 10000` 时二重循环太慢，所以在
读入这一排时边读边统计。位置 `i` 上的新兵 `x` 前面有 `i` 个人，其中编号比他小的人数是在编号 `1 … N` 上建立的
树状数组中的前缀和；`x` 的跳跃次数就是 `i` 减去这个数。然后把 `x` 加入树中。`O(K · N log N)`。

注意事项：

- 一排的总数最多为 `N(N − 1)/2 ≈ 5 · 10^7`；32 位放得下，但树状数组解法用 64 位累加；
- 相同时取第一排，所以只有严格更大的总数才替换当前最优；
- 每一排都要清空树状数组。

答案与用归并排序统计逆序对的结果做了核对，`N ≤ 300` 时还与二重循环做了核对。

## 优化解法

C++ 和 Go 版本保留树状数组算法，并用固定大小的缓冲区读取输入。树中的每个计数不超过 N，可用 16 位存储。PyPy 版本以树状数组替代有序列表，前缀查询和插入均需 O(log N)。这三个版本的时间复杂度均为 O(K·N log N)，额外空间均为 O(N)。

已通过评测的基础实现 [1090_fenwick.java](1090_fenwick.java), [1090_fenwick.rs](1090_fenwick.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

教学 Python 版本使用有序列表和二分查找，并在 PyPy 3.10 下通过评测。同一源文件在 CPython 3.12 下于测试 9 超时（0.515 秒）。优化 Python 版本使用树状数组，同样在 PyPy 3.10 下通过。表格记录每个已通过提交实际使用的解释器。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1090_binary_search.py](1090_binary_search.py) | PyPy 3.10 x64 | binary_search | O(K·N^2) | AC | 0.437 s | 20044 KB | 11279088 |
| [1090_fenwick.cpp](1090_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(K·N log N) | AC | 0.156 s | 236 KB | 11279084 |
| [1090_fenwick.go](1090_fenwick.go) | Go 1.14 x64 | fenwick | O(K·N log N) | AC | 0.046 s | 1916 KB | 11279085 |
| [1090_fenwick.java](1090_fenwick.java) \* | Java 1.8 | fenwick | O(K·N log N) | AC | 0.125 s | 512 KB | 11279089 |
| [1090_fenwick.rs](1090_fenwick.rs) \* | Rust 1.75 x64 | fenwick | O(K·N log N) | AC | 0.015 s | 2120 KB | 11279090 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1090_fenwick_optimized.cpp](1090_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(K·N log N) | AC | 0.015 s | 104 KB | 11310324 |
| [1090_fenwick_optimized.go](1090_fenwick_optimized.go) \* | Go 1.14 x64 | fenwick | O(K·N log N) | AC | 0.031 s | 816 KB | 11310344 |
| [1090_fenwick.py](1090_fenwick.py) \* | PyPy 3.10 x64 | fenwick | O(K·N log N) | AC | 0.156 s | 9076 KB | 11310319 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
