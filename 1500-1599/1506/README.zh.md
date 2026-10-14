# 1506. 数字列

[Timus 1506](https://acm.timus.ru/problem.aspx?space=1&num=1506) · 难度 138 · implementation

原题作者 Stanislav Vasiliev，出自 2006 年第 31 届 ACM ICPC 叶卡捷琳堡四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把 N 个 0 到 999 之间的数（1 ≤ N ≤ 100）排成 K 列（1 ≤ K ≤ N），行数尽可能少。除最
后一列可以较短外，各列高度相同。数先从上到下填满第一列，再填第二列，依此类推。每个
数在 4 个字符宽的字段中右对齐，行末没有多余空格。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 K，然后是 N 个数。

## 输出

排好的表格。

## 样例

### 样例 1

输入:

```
7 3
1 2 30 40 50 600 700
```

输出:

```
   1  40 700
   2  50
  30 600
```

## 解法

最少的行数是 H = ⌈N / K⌉。第 c 列放下标从 c·H 到 c·H + H − 1 的数，所以第 r 行由
c = 0, 1, … 时存在的数 c·H + r 组成；它们在第一个用完的列处停止，而这只可能是最后
一列。每个数占 4 个字符输出，然后结束这一行。`O(N)`。

注意事项：

- 数是沿列往下排的，而不是沿行（测试 01）；
- 每个数都占 4 个字符，第一个也是，所以每行都以空格开头（测试 01）；
- 最后一列较短时，下面的行少一个数提前结束，且没有行末空格（测试 06）；
- K = N 时只有一行，K = 1 时只有一列（测试 03、04）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1506_implementation.cpp](1506_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB |
| [1506_implementation.go](1506_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1108 KB |
| [1506_implementation.java](1506_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 976 KB |
| [1506_implementation.py](1506_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.093 s | 460 KB |
| [1506_implementation.rs](1506_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 252 KB |
