# 1026. 数据库中第 k 小的元素

[Timus 1026](https://acm.timus.ru/problem.aspx?space=1&num=1026) · 难度 156 · sorting, prefix_sums

原题作者 Leonid Volkov，出自 2000 年 10 月 7 日斯维尔德洛夫斯克州第二届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

数据库中有 `N` 个整数（`N ≤ 100 000`，每个在 1 到 5000 之间，顺序任意，可重复）。回答 `K` 个询问
（`1 ≤ K ≤ 100`）：给定 `i`（`1 ≤ i ≤ N`），输出第 `i` 小的元素（重复的值分别计数）。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`，然后每行一个共 `N` 个数；接着一行 `###`；然后是 `K` 和每行一个的 `K` 个询问。

## 输出

`K` 行：按顺序给出各询问的答案。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
6
42
7
5000
7
1
300
###
5
1
2
3
6
4
```

输出：

```
1
7
7
5000
42
```

### 样例 2

输入：

```
1
3000
###
1
1
```

输出：

```
3000
```

## 题解

**排序。** 把数据库排序一次；询问 `i` 的答案是位置 `i`（从 1 计）上的元素。`O(N log N + K)`。

**计数。** 值很小，因此统计每个值 `v ≤ 5000` 出现的次数并求前缀和：`atMost[v]` 是不大于 `v` 的元素个数。
第 `i` 小的元素是满足 `atMost[v] ≥ i` 的最小 `v`，可在这个不降数组上二分查找得到。`O(N + V + K log V)`，
`V = 5000`。

注意事项：

- 重复的值占据多个位置：若 7 出现两次，则位置 2 和 3 上都是 7；
- 分隔行 `###` 要跳过，不能当作数解析；
- 快速读入：共 `10^5` 行。

## 优化解法

优化的 C++ 解法和简单的计数解法一样统计各值出现的次数，但把计数放在含 5001 个
`int` 的全局数组里，从用 `fread` 反复填充的 4 KB 缓冲区中手工解析数字（`###` 这
一行和其他非数字字符一起被跳过），并用 `printf` 代替 `iostream` 输出：
{1026_prefix_sums_optimized.cpp}。

优化的 Go 解法用计数代替排序：只记录 1 到 5000 中每个值出现的次数，求前缀和，每
个询问用 `sort.SearchInts` 二分查找，因此数据库既不保存也不排序。它还从 `bufio`
读取器中手工解析数字，而不是用 `fmt.Fscan`：{1026_prefix_sums.go}。

优化的 Java 解法同样用计数代替排序：统计不超过 5000 的各值的频数，求前缀和，每个
询问二分查找一次。它按 4 KB 分块读入并手工解析数字，跳过 `###` 这一行，而不是为
每一行创建一个 `String`：{1026_prefix_sums.java}。

优化的 Python 解法也用计数代替排序。由于每个值单独占一行，它逐行读入数据库，在含
5001 个频数的列表中统计每个值，求前缀和，每个询问用 `bisect_left` 回答；既不保存
全部记号的列表，也不保存 `N` 个数排好序的列表：{1026_prefix_sums.py}。

优化的 Rust 解法把输入逐行读进同一个反复使用的 `String`，同时在含 5001 个 `u32`
的固定数组中计数，然后不排序，而是在前缀和上二分查找来回答每个询问；既不保存整个
输入，也不保存数据库：{1026_prefix_sums.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1026_prefix_sums_optimized.cpp`: 时间降低 +0.00%; 内存降低 +76.36%; 基础版本: `1026_prefix_sums.cpp`.

- `1026_prefix_sums.go`: 时间降低 +67.39%; 内存降低 +53.87%; 基础版本: `1026_sorting.go`.

- `1026_prefix_sums.java`: 时间降低 +0.00%; 内存降低 +92.25%; 基础版本: `1026_sorting.java`.

- `1026_prefix_sums.py`: 时间降低 +14.68%; 内存降低 +95.17%; 基础版本: `1026_sorting.py`.

- `1026_prefix_sums.rs`: 时间降低 -48.39%; 内存降低 +89.10%; 基础版本: `1026_sorting.rs`.

## 各语言说明

- **C++**：排序，以及计数排序加二分查找。
- **Go**、**Python**、**Java**、**Rust**：排序；Python 一次读入全部记号。

## 题解代码

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1026_prefix_sums.cpp](1026_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.015 s | 440 KB | 11278309 |
| [1026_sorting.cpp](1026_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N + K) | AC | 0.015 s | 816 KB | 11278308 |
| [1026_sorting.go](1026_sorting.go) | Go 1.14 x64 | sorting | O(N log N + K) | AC | 0.046 s | 2324 KB | 11278311 |
| [1026_sorting.java](1026_sorting.java) | Java 1.8 | sorting | O(N log N + K) | AC | 0.109 s | 5112 KB | 11278313 |
| [1026_sorting.py](1026_sorting.py) | Python 3.12 x64 | sorting | O(N log N + K) | AC | 0.109 s | 11668 KB | 11278312 |
| [1026_sorting.rs](1026_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N + K) | AC | 0.031 s | 2128 KB | 11278314 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1026_prefix_sums_optimized.cpp](1026_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.001 s | 104 KB | 11305903 |
| [1026_prefix_sums.go](1026_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.015 s | 1072 KB | 11305908 |
| [1026_prefix_sums.java](1026_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.109 s | 396 KB | 11305911 |
| [1026_prefix_sums.py](1026_prefix_sums.py) \* | Python 3.12 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.093 s | 564 KB | 11305912 |
| [1026_prefix_sums.rs](1026_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.046 s | 232 KB | 11305916 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
