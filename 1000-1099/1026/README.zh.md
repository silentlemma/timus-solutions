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

## 各语言说明

- **C++**：排序，以及计数排序加二分查找。
- **Go**、**Python**、**Java**、**Rust**：排序；Python 一次读入全部记号。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1026_prefix_sums.cpp](1026_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.015 s | 440 KB |
| [1026_sorting.cpp](1026_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N + K) | AC | 0.015 s | 816 KB |
| [1026_sorting.go](1026_sorting.go) | Go 1.14 x64 | sorting | O(N log N + K) | AC | 0.046 s | 2324 KB |
| [1026_sorting.java](1026_sorting.java) | Java 1.8 | sorting | O(N log N + K) | AC | 0.109 s | 5112 KB |
| [1026_sorting.py](1026_sorting.py) | Python 3.12 x64 | sorting | O(N log N + K) | AC | 0.109 s | 11668 KB |
| [1026_sorting.rs](1026_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N + K) | AC | 0.031 s | 2128 KB |
