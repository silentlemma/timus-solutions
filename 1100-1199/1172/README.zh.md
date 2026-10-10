# 1172. 只乘船游遍三个岛的环游路线计数

[Timus 1172](https://acm.timus.ru/problem.aspx?space=1&num=1172) · 难度 549 · combinatorics

原题作者 Mugurel Ionut Andreica，出自 2001 年 12 月的 Romanian Open Contest（罗马尼亚公开赛）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

三个岛各有 `N ≤ 30` 座城市。任意两座不同岛上的城市之间都有船，同一岛内不能
通行。从指定城市出发，统计恰好访问其他每座城市一次并返回的环游路线数；一条路线
和它反向读出的路线算作同一条。

时间限制：1 秒。内存限制：16 MB。

## 输入

`N`。

## 输出

路线数；`N` 较大时有几十位。

## 样例

### 样例 1

输入：

```
2
```

输出：

```
16
```

## 解法

把路线拆成岛屿的排列模式和城市的选择。模式是一个长度为 `3N` 的循环岛屿标号
序列，以游客所在岛开头，每种标号各 `N` 个，且相邻（包括最后一个与第一个）不
相同。模式固定后，本岛其余 `N − 1` 座城市填入其位置有 `(N − 1)!` 种方式，其他
每个岛各有 `N!` 种方式。反向读一条路线会得到从同一起点出发的另一个序列（路线至少
有三座城市），所以总数要除以二。

用 `ways[a][b][c][i]` 统计模式：从岛 0 开始、分别使用三个岛的 `a`、`b`、`c` 个
位置、以岛 `i` 结尾的序列数。每个值等于岛 `i` 少一个位置、以其他岛结尾的两个值
之和。答案统计不以岛 0 结尾的完整序列。只保留 `a` 固定的两层平面，因此大整数
的个数不多。共 `O(N³)` 次大整数加法。

注意事项：

- 环游要求最后一座城市也不能在本岛；
- 起点城市固定，所以本岛贡献 `(N − 1)!` 而不是 `N!`；
- `N = 30` 时完整的表约有 90,000 个大整数，而两层只需约 6,000 个。

答案已在 `N ≤ 3` 时与枚举所有顺序的暴力比对，并在 `N` 不超过 30 的所有值上与
另一份独立编写的解答比对。

## 各语言说明

- Python、Go 和 Java 使用各自的大整数；C++ 和 Rust 用以 10⁹ 为基的数组表示
  数，实现加法、乘以小数和除以二。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1172_combinatorics.cpp](1172_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 376 KB |
| [1172_combinatorics.go](1172_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 6024 KB |
| [1172_combinatorics.java](1172_combinatorics.java) | Java 1.8 | combinatorics | O(N³) big additions | AC | 0.125 s | 4580 KB |
| [1172_combinatorics.py](1172_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N³) big additions | AC | 0.093 s | 884 KB |
| [1172_combinatorics.rs](1172_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N³) big additions | AC | 0.031 s | 568 KB |
