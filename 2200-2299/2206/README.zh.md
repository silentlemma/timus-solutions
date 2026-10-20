# 2206. 凸多边形内坐标互质的格点

[Timus 2206](https://acm.timus.ru/problem.aspx?space=1&num=2206) · 难度 1066 · geometry, number_theory

原题作者 Vadim Barinov，出自 2022 年大学学术中学生信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定一个 N 个顶点的凸多边形，坐标恰有三位小数。统计位于其内部或边界上、坐标为互质正整数的点 (x, y) 的个数。时间限制 4.5 秒，内存限制 512 MB。

## 输入

N（3 ≤ N ≤ 2 · 10⁵），然后是逆时针给出的顶点，每个坐标在 1 到 2 · 10⁶ 之间。

## 输出

互质点的个数。

## 样例

### 样例 1

输入：

```
3
1.000 1.000
3.000 1.000
1.000 3.000
```

输出：

```
5
```

## 解法

把所有坐标乘以 1000 变成整数。对每个整数列 x，多边形覆盖下链与上链之间的一段 y。沿每条边遍历它跨过的整数列，用精确的整数除法得到 upper(x) = ⌊上界⌋ 和 lower(x) = ⌈下界⌉ − 1，于是该列含有 upper(x) − lower(x) 个整点；竖直的边不带来新的东西。

其中 gcd(x, y) = 1 的点用关于公因数 d 的莫比乌斯反演计数：

对 d 求和 μ(d) · 对能被 d 整除的列 x 求和 (⌊upper(x) / d⌋ − ⌊lower(x) / d⌋)。

设 R = ⌊max x⌋ 为原始坐标中的最右整数列，R ≤ 2 · 10⁶。对每个 d，内层和至多访问 ⌊R / d⌋ 列，因此总工作量为 O(R log R)。边界数组各有 R + 1 个元素，筛法计算到 min(R, max upper(x)) 的 μ。当 d > R / 2 时，唯一可能的倍数是列 x = d；Python 用一项单独处理。

易错点（测试 gen5）：即使多边形很小，只要靠近坐标上限，数组和筛法仍按绝对坐标索引。多边形的宽度不能限制它们的大小或总运行时间。

样例中三角形包含 (1, 1)、(1, 2)、(1, 3)、(2, 1)、(2, 2) 和 (3, 1)，只有 (2, 2) 不互质，所以答案为 5。

时间复杂度 O(N + R log R)，空间复杂度 O(N + R)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2206_geometry_number_theory.cpp](2206_geometry_number_theory.cpp) | G++ 13.2 x64 | geometry, number_theory | O(N + R log R) | AC | 0.359 s | 26576 KB |
| [2206_geometry_number_theory.go](2206_geometry_number_theory.go) | Go 1.14 x64 | geometry, number_theory | O(N + R log R) | AC | 1.421 s | 67156 KB |
| [2206_geometry_number_theory.java](2206_geometry_number_theory.java) | Java 1.8 | geometry, number_theory | O(N + R log R) | AC | 0.781 s | 28460 KB |
| [2206_geometry_number_theory.py](2206_geometry_number_theory.py) | PyPy 3.10 x64 | geometry, number_theory | O(N + R log R) | AC | 1.968 s | 122932 KB |
| [2206_geometry_number_theory.rs](2206_geometry_number_theory.rs) | Rust 1.75 x64 | geometry, number_theory | O(N + R log R) | AC | 0.875 s | 61056 KB |
