# 2183. 翻转一段的符号以提高最小值

[Timus 2183](https://acm.timus.ru/problem.aspx?space=1&num=2183) · 难度 745 · binary_search, dp

原题作者 Artyom Abaturov，出自 2024 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把数组中恰好一个非空区间内所有数的符号取反，使数组的最小值尽可能大，输出这个最小值。数组中有负数。时间限制 1 秒，内存限制 256 MB。

## 输入

n（1 ≤ n ≤ 10⁵），然后是 a₁ … aₙ（−10⁹ ≤ aᵢ ≤ 10⁹）。

## 输出

最大可能的最小值。

## 样例

### 样例 1

输入：

```
5
-1 3 -2 -4 5
```

输出：

```
-1
```

### 样例 2

输入：

```
4
2 -4 -3 -10
```

输出：

```
2
```

## 解法

问最小值能否至少为 x。所有小于 x 的数都必须翻转，所以区间要覆盖它们全部，而区间内的每个数翻转后都必须至少为 x，即本身至多为 −x。更长的区间只会增加条件，所以只需检查最短的那个——从第一个到最后一个小于 x 的数。若没有数小于 x，仍然要翻转某个至多为 −x 的数，只要最小的数至多为 −x 就成立。

x 越大检查只会越难，所以在 −10⁹ 到 10⁹ 上对 x 二分查找能找到通过检查的最大值；每次检查 O(n)，总共 O(n log C)。

第二个样例中翻转 −4 −3 −10 得到 2 4 3 10，最小值为 2。

## 各语言说明

- Python 解法不用二分：从左到右扫描一次，分别记录变号尚未开始、正在进行和已经结束时前缀最小值的最佳值，复杂度 O(n)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2183_binary_search.cpp](2183_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n log C) | AC | 0.093 s | 984 KB |
| [2183_binary_search.go](2183_binary_search.go) | Go 1.14 x64 | binary_search | O(n log C) | AC | 0.031 s | 3496 KB |
| [2183_binary_search.java](2183_binary_search.java) | Java 1.8 | binary_search | O(n log C) | AC | 0.156 s | 1320 KB |
| [2183_binary_search.rs](2183_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n log C) | AC | 0.031 s | 3708 KB |
| [2183_dp.py](2183_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.125 s | 7524 KB |
