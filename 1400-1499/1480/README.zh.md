# 1480. 餐券

[Timus 1480](https://acm.timus.ru/problem.aspx?space=1&num=1480) · 难度 471 · constructive

原题作者 Sergey Pupyrev，出自 2006 年 10 月 7 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把 1 … N²（2 ≤ N ≤ 50）填入 N × N 的表格，使有公共边的两格之和的最大值尽可能小。
输出这个和以及达到它的表格；若按行依次填写，这个和是 2N² − 1。

时间限制：1 秒。内存限制：64 MB。

## 输入

N。

## 输出

可能的最小的最大和，然后是表格的 N 行。任何满足要求的表格都可以。

## 样例

### 样例 1

输入:

```
2
```

输出:

```
6
1 4
3 2
```

## 解法

把表格像国际象棋棋盘那样染色。两个大数不能相邻，所以按阅读顺序把 N²、N² − 1、…
放在一种颜色的格子上，把 1、2、… 也按阅读顺序放在另一种颜色上。这样每个和都是一
个小数加一个大数，最坏的一对是某个小数与它正上方的大数：按阅读顺序两者之间每种
颜色约有 N/2 个格子，和恰为 N² + ⌊N/2⌋ + 1（对 50 以内的每个 N 都检验过）。

不存在更好的表格。从最大的数开始逐个放置、并为每个格子记下已放邻居留下的上限的
完全搜索表明，对 9 以内的任何 N 都找不到更小的和，而这也正是评测期望的值。
`O(N²)`。

注意事项：

- 第一行是和，而不是 N；表格紧随其后（所有测试）；
- 染色对奇数和偶数 N 都适用，但 ⌊N/2⌋ 是向下取整（测试 05、06、07）；
- 按阅读顺序直接填写的表格给出 2N² − 1（题面中已指出），远非最优。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1480_constructive.cpp](1480_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.031 s | 128 KB |
| [1480_constructive.go](1480_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.031 s | 1108 KB |
| [1480_constructive.java](1480_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.125 s | 1640 KB |
| [1480_constructive.py](1480_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.078 s | 432 KB |
| [1480_constructive.rs](1480_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.031 s | 256 KB |
