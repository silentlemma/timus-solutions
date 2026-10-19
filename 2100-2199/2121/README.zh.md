# 2121. 两条镜像抛物线之间的面积

[Timus 2121](https://acm.timus.ru/problem.aspx?space=1&num=2121) · 难度 723 · geometry, math

原题作者 Alexey Danilyuk，出自 2018 年夏季彼得罗扎沃茨克集训营 t.me/umnik_team 专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

求抛物线 y = (x − a)² 与 x = (y − a)² 所围区域的面积，输出恰好保留小数点后 10 位。时间限制 1 秒，内存限制 64 MB。

## 输入

整数 a（1 ≤ a ≤ 10¹⁸）。

## 输出

面积。

## 样例

### 样例 1

输入：

```
2
```

输出：

```
7.6666666667
```

## 解法

把原点移到 (a, a)：令 x = a + p、y = a + q，区域为 q ≥ p² − a 且 p ≥ q² − a。两条抛物线交于四点。其中两点在 q = p 上，此时 p² = p + a，所以 p = (1 ± s)/2，s = √(4a + 1)。两式相减得 (p − q)(p + q + 1) = 0，所以另外两点在 p + q = −1 上，p = (−1 ± t)/2，t = √(4a − 3)。

对 p 积分：区域的上边界是 q = √(p + a)，下边界在两端是 q = p² − a，中间是 q = −√(p + a)。在每个角点 √(p + a) 都等于 |q|，所以每个原函数都化为角点坐标的多项式。再用每对根的和与积就能消去 s 和 t：面积恰好是 4a − 1/3。

所以答案是 4a − 1 后接 ".6666666667"。a = 10¹⁸ 时整数部分略小于 4 · 10¹⁸，可以放进 64 位整数，而浮点数会丢掉最后几位。

样例中 4 · 2 − 1/3 = 7.6666666667。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2121_geometry_math.cpp](2121_geometry_math.cpp) | G++ 13.2 x64 | geometry, math | O(1) | AC | 0.015 s | 132 KB |
| [2121_geometry_math.go](2121_geometry_math.go) | Go 1.14 x64 | geometry, math | O(1) | AC | 0.015 s | 1076 KB |
| [2121_geometry_math.java](2121_geometry_math.java) | Java 1.8 | geometry, math | O(1) | AC | 0.125 s | 1628 KB |
| [2121_geometry_math.py](2121_geometry_math.py) | Python 3.12 x64 | geometry, math | O(1) | AC | 0.078 s | 376 KB |
| [2121_geometry_math.rs](2121_geometry_math.rs) | Rust 1.75 x64 | geometry, math | O(1) | AC | 0.015 s | 240 KB |
