# 1294. 火星卫星

[Timus 1294](https://acm.timus.ru/problem.aspx?space=1&num=1294) · 难度 317 · geometry

原题作者 Vladimir Yakovlev，出自 2004 年 3 月 13 日第九届中学生公开团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

四颗卫星 A、B、C、D 按此顺序位于同一圆形轨道上。已知距离 AD、AC、BD、BC，单位为千公里（1 到
10 000 的整数）；轨道半径未知。求 CD 的距离（公里，四舍五入到整数），或者报告它不能唯一确定。

时间限制：1 秒。内存限制：64 MB。

## 输入

AD、AC、BD 和 BC。

## 输出

`Distance is X km.` 或 `Impossible.`

## 样例

### 样例 1

输入：

```
4 7 5 7
```

输出：

```
Distance is 5385 km.
```

## 解法

记 a = AD，b = AC，c = BD，d = BC，x = CD。点 A 和 B 位于弦 CD 截出的同一段弧上，所以它们看 CD
的圆周角相同，记为 t。在三角形 ACD 和 BCD 中用余弦定理得

x² = a² + b² − 2ab cos t = c² + d² − 2cd cos t，

这是关于 x² 和 cos t 的两个方程。由此

cos t = (a² + b² − c² − d²) / (2 (ab − cd))，

x² = (ab (c² + d²) − cd (a² + b²)) / (ab − cd)。

- 若 ab = cd，两个方程要么矛盾，要么对 t 没有任何约束。后一种情况（例如等腰梯形）下 CD 确实可以
  取很多值（测试 02）。两种情况的答案都是 `Impossible.`（测试 02 和 03）。
- 若 |a² + b² − c² − d²| ≥ 2 |ab − cd|，则不存在非退化三角形。等号也不允许，因为圆上三个不同的点
  不可能共线（测试 04 和 07）。
- 对于给定的顶点顺序，托勒密定理要求 AB · CD = bc − ad > 0。因此 bc ≤ ad 时输出
  `Impossible.`（测试 05 和 07）。结合严格的余弦界限，这项检查保证重建的点具有正确顺序。
- 否则 x = 1000 · √x² 公里，四舍五入。

所有可行性检查都用精确的 64 位整数完成（原始乘积小于 2 · 10¹⁶）。先将分子和分母化为正数。
用浮点平方根估计公里数的整数部分 m，再精确判断是否向上舍入：
(2m + 1)² ≤ floor(4 · 1000² · num / den)。为避免溢出，将右侧计算为
s · (num div den) + (s · (num mod den)) div den，其中 s = 4 · 1000²。
新的中间值均小于 2 · 10¹⁵。时间和额外空间均为 `O(1)`。

修正后的可行性检查和舍入结果由独立的精确参考程序验证，参考程序使用托勒密定理、对角互补及严格的三角不等式。

注意事项：

- 输入单位是千公里，答案单位是公里（测试 01）；
- AD · AC = BD · BC 并不总是意味着数据矛盾，有时意味着答案有很多个（测试 02 和 03）；
- 余弦在 [−1, 1] 内并不足以保证轨道有效：还要排除退化三角形并检查顶点顺序（测试 07）。

## 各语言说明

- Python 的 `round` 把一半舍入到偶数。五种解法都用精确整数比较半公里边界的平方，
  因此恰好一半时都一致地向上舍入。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1294_geometry.cpp](1294_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 124 KB |
| [1294_geometry.go](1294_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1084 KB |
| [1294_geometry.java](1294_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1648 KB |
| [1294_geometry.py](1294_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 448 KB |
| [1294_geometry.rs](1294_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 236 KB |
