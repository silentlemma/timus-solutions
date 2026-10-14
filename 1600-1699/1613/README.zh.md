# 1613. 献给统计爱好者

[Timus 1613](https://acm.timus.ru/problem.aspx?space=1&num=1613) · 难度 142 · binary_search

原题作者 Alexander Ipatov，出自 2008 年 3 月 29 日第十二届乌拉尔竞技编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 个城市（n ≤ 69 999）各自运送了一定数量的乘客，都小于 10⁹。对 q 个
查询（q ≤ 69 999）`l r x` 中的每一个，回答编号在 l 到 r 之间的城市中
是否有恰好运送 x 人的。输出 q 个字符组成的字符串，`1` 表示是，`0` 表示否。

时间限制：1 秒。内存限制：64 MB。

## 输入

n、n 个数、q，然后是 q 行 `l r x`。

## 输出

答案字符串。

## 样例

### 样例 1

输入:

```
5
1234567 666666 3141593 666666 4343434
5
1 5 3141593
1 5 578202
2 4 666666
4 4 7135610
1 1 1234567
```

输出:

```
10101
```

## 解法

把 (数量, 城市编号) 对排序。数量为 x 的城市于是连成一块，按编号排列。
对每个查询，二分查找第一个不小于 (x, l) 的对：若它的数量等于 x 且城市
编号不超过 r，答案为是。`O((n + q) log n)`。

易错点：

- 答案是一个没有分隔符的字符串；
- 城市必须在 l 或之后找到，而不只是在某处数量为 x（测试 04）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1613_binary_search.cpp](1613_binary_search.cpp) | G++ 13.2 x64 | binary_search | O((n + q) log n) | AC | 0.171 s | 748 KB |
| [1613_binary_search.go](1613_binary_search.go) | Go 1.14 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 5876 KB |
| [1613_binary_search.java](1613_binary_search.java) | Java 1.8 | binary_search | O((n + q) log n) | AC | 0.140 s | 1964 KB |
| [1613_binary_search.py](1613_binary_search.py) | Python 3.12 x64 | binary_search | O((n + q) log n) | AC | 0.343 s | 26612 KB |
| [1613_binary_search.rs](1613_binary_search.rs) | Rust 1.75 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 3692 KB |
