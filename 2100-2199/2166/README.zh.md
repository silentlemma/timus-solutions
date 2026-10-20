# 2166. 按 L1 距离离原点最远的直线交点

[Timus 2166](https://acm.timus.ru/problem.aspx?space=1&num=2166) · 难度 2116 · geometry, sorting

原题作者 Vadim Barinov，出自 2022 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给出 N 条两两不平行的直线，每条由两个整点确定，任意两条直线的交点都是一个车站。从原点沿坐标轴方向到达车站 (x, y) 的代价是 |x| + |y|。输出所有车站中最大的代价，相对误差不超过 10⁻⁴。时间限制 3 秒，内存限制 256 MB。

## 输入

N（2 ≤ N ≤ 10⁵），然后是各直线 x₁ y₁ x₂ y₂，坐标绝对值不超过 1000。

## 输出

所有交点中最大的 |x| + |y|。

## 样例

### 样例 1

输入：

```
3
0 0 1 1
1 0 1 1
1 3 2 1
```

输出：

```
4
```

## 解法

代价 |x| + |y| 是四个线性函数 ±x ± y 中最大的一个，所以答案是在四个方向上，线性函数在直线排布所有交点上的最大值。关于直线排布有一个经典事实：在任意方向上最极端的交点由斜率循环顺序中相邻的两条直线构成。所以用精确的叉积比较按方向排序，检查 N 对循环相邻直线的交点即可。

把直线写成 dy · x − dx · y = c，两条直线的交点是分母为 |dx₁ dy₂ − dy₁ dx₂| 的分数，其 L1 范数为 (|dx₁ c₂ − c₁ dx₂| + |dy₁ c₂ − c₁ dy₂|) 除以这个分母。用整数交叉相乘精确保存最优分数，并精确舍入输出。工作量 O(N log N)。

样例中直线 y = x 与 x = 1 交于 (1, 1)，过 (1, 3) 和 (2, 1) 的直线与 y = x 交于 (5/3, 5/3)，与 x = 1 交于 (1, 3)，后者最远，代价为 4。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2166_geometry_sorting.cpp](2166_geometry_sorting.cpp) | G++ 13.2 x64 | geometry, sorting | O(N log N) | AC | 0.078 s | 2312 KB |
| [2166_geometry_sorting.go](2166_geometry_sorting.go) | Go 1.14 x64 | geometry, sorting | O(N log N) | AC | 0.078 s | 8296 KB |
| [2166_geometry_sorting.java](2166_geometry_sorting.java) | Java 1.8 | geometry, sorting | O(N log N) | AC | 0.218 s | 9168 KB |
| [2166_geometry_sorting.py](2166_geometry_sorting.py) | Python 3.12 x64 | geometry, sorting | O(N log N) | AC | 0.953 s | 44364 KB |
| [2166_geometry_sorting.rs](2166_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O(N log N) | AC | 0.046 s | 5304 KB |
