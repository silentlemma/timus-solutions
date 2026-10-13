# 1422. 萤火虫

[Timus 1422](https://acm.timus.ru/problem.aspx?space=1&num=1422) · 难度 855 · geometry

原题作者 Ilya Grebnov、Dmitry Kovalioff 与 Nikita Rybak，出自 Timus Top Coders: First Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 只苍蝇（1 ≤ N ≤ 2000）静止悬在整点上，坐标绝对值不超过 10⁷。一个点状火球沿任
意直线飞行，把途中遇到的每只苍蝇变成萤火虫。求一个火球最多能击中多少只苍蝇，也
就是一条直线上最多有多少个点。

时间限制：3 秒。内存限制：64 MB。

## 输入

N，然后 N 行 X Y Z。

## 输出

一条直线上苍蝇的最大数目。

## 样例

### 样例 1

输入:

```
6
-1 1 -1
0 1 2
0 0 -1
-2 -1 2
2 -1 -2
-1 0 2
```

输出:

```
3
```

## 解法

依次把每只苍蝇当作直线上的第一只，考察它到后面各只苍蝇的方向。两只苍蝇与第一只
共线，当且仅当它们的差向量互为倍数，所以把每个向量除以各分量的最大公约数，并调
整符号使第一个非零分量为正。相等的约化向量表示同一条直线；对它们计数（用哈希表
或排序）就得到经过这只苍蝇的最佳直线。与第一只位于同一点的苍蝇在经过它的每条直
线上，要加到最佳计数中。由于求最大公约数，复杂度为 `O(N² log C)`，其中
C = 2·10⁷。

注意事项：

- 多只苍蝇可能位于同一点（测试 03、05、gen4）；
- 只有一只苍蝇时答案也是 1（测试 02）；
- 差值可达 2·10⁷，仍在 32 位范围内，整数键避免了方向的舍入误差（测试 06、
  gen2）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1422_geometry.cpp](1422_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2 log C) | AC | 0.328 s | 224 KB |
| [1422_geometry.go](1422_geometry.go) | Go 1.14 x64 | geometry | O(N^2 log C) | AC | 0.468 s | 6524 KB |
| [1422_geometry.java](1422_geometry.java) | Java 1.8 | geometry | O(N^2 log C) | AC | 0.343 s | 744 KB |
| [1422_geometry.py](1422_geometry.py) | Python 3.12 x64 | geometry | O(N^2 log C) | AC | 1.828 s | 1868 KB |
| [1422_geometry.rs](1422_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2 log C) | AC | 0.312 s | 312 KB |
