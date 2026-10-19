# 2076. 二次曲线对称轴上的圆

[Timus 2076](https://acm.timus.ru/problem.aspx?space=1&num=2076) · 难度 6156 · geometry, math

原题作者 Mikhail Rubinchik。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

曲线是所有实数 t 对应的点 (a t² + b t + c, d t² + e t + f) 的集合。把点 P 投影到曲线的某条对称轴上，得到点 Q。以 Q 为圆心、R 为半径的闭圆盘是否与曲线相交？若对任意对称轴都相交，输出 `YES`；都不相交，输出 `NO`；取决于对称轴，输出 `MAYBE`。保证曲线至少有一条对称轴。时间限制 2 秒，内存限制 256 MB。

## 输入

T ≤ 7000 组测试，每组三行 `a b c`、`d e f`、`Px Py R`，均为绝对值不超过 10²⁰ 的整数，R ≥ 1。

## 输出

每组输出 `YES`、`NO` 或 `MAYBE`。

## 样例

### 样例 1

输入：

```
1
0 1 0
1 0 0
2 1 1
```

输出：

```
YES
```

## 解法

把曲线写成 C + B t + A t²，其中 A = (a, d)，B = (b, e)，C = (c, f)，并令 W = P − C。曲线是点、直线、射线或抛物线。

- A = B = 0：单个点 C。过 C 的任意直线都是对称轴，垂足 Q 跑遍以 CP 为直径的圆，从 C 本身（距离 0）到 P（距离 |CP|）。所以 |CP| ≤ R 时答案为 `YES`，否则为 `MAYBE`。
- A = 0，B ≠ 0：一条直线。直线本身是对称轴，Q 在直线上，给出 `YES`。每条垂线也是对称轴，此时 Q 到直线的距离等于 P 到直线的距离，即 |W × B| / |B|。所以同样是 `YES` 或 `MAYBE`。
- A ≠ 0：唯一的对称轴是过顶点、方向为 A 的直线（对抛物线成立，对 A × B = 0 时的射线也成立）。顶点处 t₀ = −(A·B) / (2|A|²)，Q 沿轴到顶点的坐标为 N / (4|A|³)，其中 N = 4|A|² (W·A) + (A·B)²。在垂直于轴的方向上，抛物线张开为 s = κw²，κ = |A|³ / K，K = (A × B)²。

对轴上的点 Q = (s, 0)，到曲线的距离平方是对 u = w² ≥ 0 取 (κu − s)² + u 的最小值。导数在 u = s/κ − 1/(2κ²) 处为零。若该值不为正（s ≤ 1/(2κ)，即 N ≤ 2K），最近点是顶点，距离为 |s|，判定为 N² ≤ 16 R² |A|⁶。否则距离平方为 s/κ − 1/(4κ²) = K (N − K) / (4|A|⁶)，判定为 K (N − K) ≤ 4 R² |A|⁶。对射线 K = 0，公式依然正确：在射线内部距离为 0，在其端点之后距离为 |s|。只有一条轴，所以答案为 `YES` 或 `NO`。

所有比较都是精确的。输入可达 10²⁰，乘积约达 10¹⁶³：Python、Go 和 Java 使用各自的大整数，C++ 和 Rust 解答自带一个小型有符号大整数，在 32 位分段上实现加、减、乘和比较。每组测试只需 O(1) 次大数运算。

样例中曲线是抛物线 y = x²，对称轴为 x = 0，Q = (0, 1) 位于抛物线内侧，到它的距离为 √3/2 < 1，所以答案为 `YES`。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2076_geometry_math.cpp](2076_geometry_math.cpp) | G++ 13.2 x64 | geometry, math | O(T) | AC | 0.312 s | 444 KB |
| [2076_geometry_math.go](2076_geometry_math.go) | Go 1.14 x64 | geometry, math | O(T) | AC | 0.093 s | 6760 KB |
| [2076_geometry_math.java](2076_geometry_math.java) | Java 1.8 | geometry, math | O(T) | AC | 0.203 s | 17400 KB |
| [2076_geometry_math.py](2076_geometry_math.py) | Python 3.12 x64 | geometry, math | O(T) | AC | 0.109 s | 6764 KB |
| [2076_geometry_math.rs](2076_geometry_math.rs) | Rust 1.75 x64 | geometry, math | O(T) | AC | 0.281 s | 2144 KB |
