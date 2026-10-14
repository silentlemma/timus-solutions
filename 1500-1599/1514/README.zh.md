# 1514. 国家公园

[Timus 1514](https://acm.timus.ru/problem.aspx?space=1&num=1514) · 难度 1753 · geometry

原题作者 Nikita Rybak、Ilya Grebnov 与 Dmitry Kovalioff，出自 Timus Top Coders: Third Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 棵树（3 ≤ N ≤ 50000）位于坐标绝对值不超过 10⁶ 的整点上，几棵树可以在同一点。选出
三棵不同的树，使它们构成的三角形周长最小；面积为零的三角形也算。输出周长（小数点后
至少四位）和这三棵树的编号。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是 N 棵树的坐标。

## 输出

最小周长，然后以任意顺序输出三棵树的编号。任何最优的三元组都可以。

## 样例

### 样例 1

输入:

```
5
0 0
1 1
3 0
0 3
3 3
```

输出:

```
6.6503
1 2 3
```

## 解法

分治，和最近点对一样。按 x 排序，分别解决左右两半，设 d 为目前最好的周长。三角形的
每条边都不超过周长的一半，所以更好的三角形的三棵树两两距离都小于 d/2。因此一个跨越
分界线的更好三角形位于分界线两侧各宽 d/2 的带内：把带按 y 排序，对每棵树，枚举比它
高不到 d/2 的树对，每当 d 变小就收紧界限。与最近点对相同的装箱论证保证这样的树数量
有界，所以每层只需一次排序，总计 `O(N log² N)`。不超过 8 棵树的小块直接枚举三元组。

注意事项：

- 同一点上的三棵树给出周长 0（测试 03、gen7）；
- 退化三角形也算，所以共线的树给出两端距离的两倍（测试 02、06、gen2、gen3）；
- 所有树的 x 相同时，每棵树都落入每条带中，只有 y 的界限让工作量保持很小（gen2）；
- 50000 棵树约有 2·10¹³ 个三元组，不可能全部枚举（gen1）；
- 最优三元组可能有很多，所以测试使用检查程序（所有测试）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1514_geometry.cpp](1514_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log^2 N) | AC | 0.109 s | 1024 KB |
| [1514_geometry.go](1514_geometry.go) | Go 1.14 x64 | geometry | O(N log^2 N) | AC | 0.078 s | 6540 KB |
| [1514_geometry.java](1514_geometry.java) | Java 1.8 | geometry | O(N log^2 N) | AC | 0.515 s | 8444 KB |
| [1514_geometry.py](1514_geometry.py) | Python 3.12 x64 | geometry | O(N log^2 N) | AC | 0.890 s | 16368 KB |
| [1514_geometry.rs](1514_geometry.rs) | Rust 1.75 x64 | geometry | O(N log^2 N) | AC | 0.062 s | 3348 KB |
