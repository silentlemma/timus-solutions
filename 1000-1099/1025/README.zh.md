# 1025. 在两级多数表决中获胜所需的最少支持者

[Timus 1025](https://acm.timus.ru/problem.aspx?space=1&num=1025) · 难度 67 · greedy, sorting

原题出自 2000 年 10 月 7 日斯维尔德洛夫斯克州第二届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

选民被分成 `K` 组（`K` 为奇数，`1 ≤ K ≤ 101`），每组人数为奇数；总人数不超过 9999。一组中超过半数投赞成时
该组表示“赞成”，超过半数的组表示“赞成”时决议通过。求最少需要多少支持者，在合适地分配到各组后能通过任何
决议。

时间限制：1 秒。内存限制：64 MB。

## 输入

`K`，然后是 `K` 个组的人数。

## 输出

最少的支持者人数。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
5
9 3 11 1 7
```

输出：

```
7
```

### 样例 2

输入：

```
1
9999
```

输出：

```
5000
```

## 题解

要通过决议，支持者必须赢得 `K / 2 + 1` 个组（整数除法，`K` 为奇数），而赢得一个 `s` 人的组（`s` 为奇数）
需要 `s / 2 + 1` 名支持者；该组中多出的支持者是浪费，输掉的组中的支持者也是浪费。

所以要选出 `K / 2 + 1` 个组，使代价 `s / 2 + 1` 的总和最小。代价随人数增大而增大，因此最好的组就是最小
的那些：把人数排序，累加前 `K / 2 + 1` 个组的代价。`O(K log K)`。

注意事项：

- 组的多数是 `K / 2 + 1`，`s` 人组内的多数是 `s / 2 + 1`，不是 `s / 2`；
- 输入中的人数没有排序。

## 优化解法

优化的 Java 解法按 1 KB 分块读入并手工解析，而不是使用 `Scanner`：384 KB，而不是
1724 KB，时间不变。

`1025_greedy_sorting_optimized.go`. Go 保留选择最小若干组以获得多数的贪心策略。优化代码直接读取字节，把每组人数插入最多 101 项的固定数组。这里有意使用插入排序：时间为 O(K²)，而基础排序为 O(K log K)；在这个小规模限制下，它省去动态容器和 fmt 的开销。对前 floor(K/2)+1 组求 floor(size/2)+1 之和，并保留使用库排序的原版。

与 `1025_greedy_sorting.go` 相比：时间 0.031 s → 0.015 s；内存 1076 KB → 796 KB。

`1025_greedy_sorting_optimized.py`. Python 保留排序后求和的贪心算法。字节记号经迭代器直接转换并交给 sorted，避免单独解码全部输入以及排序前额外的完整整数列表。跳过解释器正常清理而结束进程前，显式刷新输出。时间仍为 O(K log K)，排序后的组规模占 O(K) 空间。

与 `1025_greedy_sorting.py` 相比：时间 0.093 s → 0.109 s；内存 372 KB → 212 KB。

## 各语言说明

各语言都是同样的排序与求和。

## 题解代码

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1025_greedy_sorting.cpp](1025_greedy_sorting.cpp) | G++ 13.2 x64 | greedy, sorting | O(K log K) | AC | 0.001 s | 188 KB | 11303273 |
| [1025_greedy_sorting.go](1025_greedy_sorting.go) | Go 1.14 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 1076 KB | 11278301 |
| [1025_greedy_sorting.java](1025_greedy_sorting.java) | Java 1.8 | greedy, sorting | O(K log K) | AC | 0.109 s | 1724 KB | 11278306 |
| [1025_greedy_sorting.py](1025_greedy_sorting.py) | Python 3.12 x64 | greedy, sorting | O(K log K) | AC | 0.093 s | 372 KB | 11278304 |
| [1025_greedy_sorting.rs](1025_greedy_sorting.rs) | Rust 1.75 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 220 KB | 11278307 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1025_greedy_sorting_optimized.java](1025_greedy_sorting_optimized.java) \* | Java 1.8 | greedy, sorting | O(K log K) | AC | 0.125 s | 384 KB | 11303704 |
| [1025_greedy_sorting_optimized.go](1025_greedy_sorting_optimized.go) | Go 1.14 x64 | greedy, sorting | O(K²) | AC | 0.015 s | 796 KB | 11325044 |
| [1025_greedy_sorting_optimized.py](1025_greedy_sorting_optimized.py) \* | PyPy 3.10 x64 | greedy, sorting | O(K log K) | AC | 0.109 s | 212 KB | 11324842 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
