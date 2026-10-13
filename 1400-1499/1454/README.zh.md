# 1454. 矩形 2

[Timus 1454](https://acm.timus.ru/problem.aspx?space=1&num=1454) · 难度 2530 · backtracking

原题作者 Nikita Rybak、Ilya Grebnov 与 Dmitry Kovalioff，出自 Timus Top Coders: Second Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给出五个矩形 W[i] × H[i]（1 ≤ W[i], H[i] ≤ 1000）。判断能否把这五个矩形按需旋转，
不重叠也不切割，拼成一个大矩形。

时间限制：1 秒。内存限制：64 MB。

## 输入

五行，每行 W[i] 和 H[i]。

## 输出

"YES" 或 "NO"。

## 样例

### 样例 1

输入:

```
2 4
3 2
5 3
2 5
2 5
```

输出:

```
YES
```

## 解法

大矩形的面积就是总面积 A，所以它的宽 w 是 A 的约数，由对称性只需尝试 w² ≤ A 的
宽度。固定尺寸后，用“天际线”方式放置：把已填部分的轮廓记为若干等高段，取最低的
一段（最低中最靠左的），在它的左角放一个尚未使用的矩形，两种方向都试。在任何一种
拼法中，最低最左的空格都是某个矩形的左下角，并且这个矩形不会比这一段宽，因为两侧
相邻的段都更高；所以这个搜索能找到每一种拼法。

五个矩形每个尺寸至多 5! · 2⁵ 种放法，宽高限制会剪掉大部分；同一角上同形状的矩形
不重复尝试。面积的约数至多几百个，所以整个搜索规模很小。

注意事项：

- 风车形拼法，没有一块覆盖大矩形的整条边（测试 02、06、14）；
- 总面积为质数时只剩宽为 1 的长条（测试 04）；
- 每块都要尝试两种方向（测试 02、07、11）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1454_backtracking.cpp](1454_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(d · 5! · 2^5) | AC | 0.015 s | 188 KB |
| [1454_backtracking.go](1454_backtracking.go) | Go 1.14 x64 | backtracking | O(d · 5! · 2^5) | AC | 0.031 s | 1268 KB |
| [1454_backtracking.java](1454_backtracking.java) | Java 1.8 | backtracking | O(d · 5! · 2^5) | AC | 0.140 s | 2356 KB |
| [1454_backtracking.py](1454_backtracking.py) | Python 3.12 x64 | backtracking | O(d · 5! · 2^5) | AC | 0.093 s | 680 KB |
| [1454_backtracking.rs](1454_backtracking.rs) | Rust 1.75 x64 | backtracking | O(d · 5! · 2^5) | AC | 0.031 s | 396 KB |
