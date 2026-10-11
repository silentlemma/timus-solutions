# 1252. 用相隔 K 的交换给石头排序

[Timus 1252](https://acm.timus.ru/problem.aspx?space=1&num=1252) · 难度 397 · number_theory

原题作者 Alexey Lakhtin，出自 2003 年 3 月 15 日乌拉尔国立大学公开团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 块重量互不相同的石头（1 ≤ N ≤ 130 000）排成一行。当两块石头之间恰好有 K 块别的石头时，
可以交换它们。求最大的 K（0 ≤ K < N），使这一行能按重量排好序——升序或降序都可以。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是 N 个重量，每行一个。每个重量都是 1 到 130 000 之间的整数（含端点）。

## 输出

最大的这样的 K。

## 样例

### 样例 1

输入：

```
5
30
21
56
40
17
```

输出：

```
1
```

## 解法

中间隔着 K 块石头的交换会把两块石头都移动 d = K + 1 个位置，所以一块石头始终留在模 d
的同一个位置类中，而在一个类内部，通过类中相邻位置的交换可以得到任意顺序。因此，能
排好序当且仅当 d 整除每块石头从当前位置到它在有序行中位置的距离。

所以对升序和降序分别求出这些距离的最大公约数 g。整除 g 的最大的 d 就是 g 本身，它小于
N，所以 K = g − 1；如果这一行已经是这个顺序，则 g = 0，任何 K 都行，所以 K = N − 1。
答案取两种顺序中较大的。排序需要 `O(N log N)`。

注意事项：

- 降序也算（测试 04），两种顺序可能给出不同的 K；
- 已经有序的行允许最大的 K = N − 1，尽管这时根本无法进行任何交换（测试 03 和 gen4）。

该规则在 300 行随机的、至多 7 块石头的行上，与对每个 K 搜索所有可达顺序的结果比较过。

## 各语言说明

- Java 把重量和位置打包进一个 `long` 数组再排序，而不是用比较器对装箱的下标排序。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1252_number_theory.cpp](1252_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log N) | AC | 0.093 s | 1212 KB |
| [1252_number_theory.go](1252_number_theory.go) | Go 1.14 x64 | number_theory | O(N log N) | AC | 0.125 s | 4012 KB |
| [1252_number_theory.java](1252_number_theory.java) | Java 1.8 | number_theory | O(N log N) | AC | 0.093 s | 1596 KB |
| [1252_number_theory.py](1252_number_theory.py) | Python 3.12 x64 | number_theory | O(N log N) | AC | 0.140 s | 13612 KB |
| [1252_number_theory.rs](1252_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log N) | AC | 0.031 s | 3652 KB |
