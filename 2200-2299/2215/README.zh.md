# 2215. 整个平面不断旋转时统计矩形内的点

[Timus 2215](https://acm.timus.ru/problem.aspx?space=1&num=2215) · 难度 1278 · geometry, fenwick

原题作者 Vadim Barinov，出自 2024 年大学学术中学生信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 个互不相同的点依次经历 Q 个事件：把所有点绕给定点逆时针旋转 90°、180° 或 270°，或者统计一个与坐标轴平行的矩形内的点数。时间限制 3 秒，内存限制 256 MB。

## 输入

N（1 ≤ N ≤ 4 · 10⁴），然后是各点，然后是 Q（1 ≤ Q ≤ 4 · 10⁴）和事件「r90 x y」「r180 x y」「r270 x y」或「ask x1 y1 x2 y2」，所有坐标绝对值不超过 10⁹。

## 输出

每个「ask」的计数。

## 样例

### 样例 1

输入：

```
4
1 1
2 2
3 3
4 4
4
r90 0 0
ask -2 -1 0 4
r180 1 1
ask 3 -3 6 0
```

输出：

```
2
3
```

## 解法

任意一串绕各点的四分之一圈旋转，都等于绕原点旋转若干个四分之一圈再加一个平移：原始点 p 的当前位置为 Rᵏ p + t。绕 c 再转 j 个四分之一圈把它变为 Rʲ(Rᵏ p + t − c) + c，所以只需更新 k 和 t。

当前坐标下的查询矩形减去 t 并旋转 −k 个四分之一圈，就映射回原始坐标。四分之一圈旋转把与坐标轴平行的矩形变成同样的矩形，所以只需映射两个对角顶点并把坐标排好序。这样所有查询都针对同一个固定的点集。

离线回答：每个矩形在右边和紧挨左边左侧各产生一个事件，按 x 顺序扫描事件和点，用压缩 y 坐标上的树状数组统计已插入点在 y 范围内的个数。

样例中第一次旋转后各点为 (−1, 1) … (−4, 4)，第一个矩形包含 (−1, 1) 和 (−2, 2)。

复杂度 O((N + Q) log(N + Q))。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2215_geometry_fenwick.cpp](2215_geometry_fenwick.cpp) | G++ 13.2 x64 | geometry, fenwick | O((N + Q) log(N + Q)) | AC | 0.078 s | 5076 KB |
| [2215_geometry_fenwick.go](2215_geometry_fenwick.go) | Go 1.14 x64 | geometry, fenwick | O((N + Q) log(N + Q)) | AC | 0.296 s | 10672 KB |
| [2215_geometry_fenwick.java](2215_geometry_fenwick.java) | Java 1.8 | geometry, fenwick | O((N + Q) log(N + Q)) | AC | 0.421 s | 12104 KB |
| [2215_geometry_fenwick.py](2215_geometry_fenwick.py) | Python 3.12 x64 | geometry, fenwick | O((N + Q) log(N + Q)) | AC | 0.718 s | 37016 KB |
| [2215_geometry_fenwick.rs](2215_geometry_fenwick.rs) | Rust 1.75 x64 | geometry, fenwick | O((N + Q) log(N + Q)) | AC | 0.062 s | 8496 KB |
