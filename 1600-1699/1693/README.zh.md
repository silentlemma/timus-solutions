# 1693. 劳埃德问题

[Timus 1693](https://acm.timus.ru/problem.aspx?space=1&num=1693) · 难度 10340 · constructive

原题作者 Sam Loyd 和 Igor Chevdar，出自 2009 年 2 月彼得罗扎沃茨克冬季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

沿网格线把 n × n 的国际象棋棋盘切成尽可能多的连通块，使任意两块都不相同。
只差一个旋转的块视为相同，但格子的颜色要考虑：黑色单格和白色单格是两种不同的块。

## 输入

n（1 ≤ n ≤ 30）。

## 输出

块数，然后是 n 行、每行 n 个小写字母。每块用同一个字母表示，相邻的块用不同字母。任何最优的切法都可以。

## 样例

### 样例 1

输入：

```
8
```

输出：

```
18
aaaacaaa
bbbcccba
baddabbb
aacdacba
accdacaa
babdccbb
baaadbba
babbaaaa
```

## 解法

**上界。** 统计每种面积在旋转意义下的带色块数：面积 1 有 2 种，面积 2 有 1 种，面积 3 有 4 种，
面积 4 有 10 种，面积 5 有 36 种，面积 6 有 110 种，面积 7 有 392 种。互不相同的块的总面积至少是这些面积中最小的 k 个之和，
所以 k 不超过最小面积之和不超过 n² 的最大个数。n = 8 时是 2 + 1 + 4 + 10 = 17 个面积不超过 4 的块，
共 56 格，再加上由剩下 8 格组成的一块，共 18 块。

**构造。** 上界总能达到：最小面积的每种块各用一次，剩余面积并入一块更大的块，
它是唯一这么大的块，所以与众不同。不过要把多达 162 块精确地拼进正方形是很难的搜索。
因此所有 30 种尺寸的切法都事先离线用带重启的随机深度优先搜索求出，程序直接输出对应 n 的存储棋盘。`O(n²)`。

每张存储的棋盘都经过独立验证：同一字母的区域是连通的块，考虑颜色后在旋转意义下两两不同，
块数等于上面的上界。各面积的块数也通过枚举多联骨牌重新计算过。

注意事项：

- 颜色要考虑，所以单格有两种而不是一种；
- 只有旋转视为相同，镜像不算；
- 不相邻的块可以重复使用同一个字母。

检查器根据字母重建各块，验证块数和两两不同。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1693_constructive.cpp](1693_constructive.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 140 KB |
| [1693_constructive.go](1693_constructive.go) | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1084 KB |
| [1693_constructive.java](1693_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.156 s | 1784 KB |
| [1693_constructive.py](1693_constructive.py) | Python 3.12 x64 | constructive | O(n²) | AC | 0.078 s | 1100 KB |
| [1693_constructive.rs](1693_constructive.rs) | Rust 1.75 x64 | constructive | O(n²) | AC | 0.015 s | 220 KB |
