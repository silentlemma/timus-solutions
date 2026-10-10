# 1139. 沿对角线飞越街道网格时经过的街区数

[Timus 1139](https://acm.timus.ru/problem.aspx?space=1&num=1139) · 难度 78 · number_theory

原题出自 2001 年 10 月 17–18 日在雷宾斯克举行的俄罗斯中部赛区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

`N` 条大道和 `M` 条街道（`1 < N, M < 32000`）把城市分成正方形街区。直升机
从西南角沿直线飞到东北角。求它飞越的街区数；街区是其正方形的开内部，
所以只碰到角不算。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N` 和 `M`。

## 输出

街区数。

## 样例

### 样例 1

输入：

```
4 3
```

输出：

```
4
```

### 样例 2

输入：

```
3 3
```

输出：

```
2
```

## 解法

街区构成 `a × b` 的网格，`a = N − 1`，`b = M − 1`，飞行路线是它的对角线。
它从第一个街区内部出发，每穿过一条网格线就进入一个新街区。它穿过 `a − 1`
条内部竖线和 `b − 1` 条内部横线，但在网格的内部角点处会同时穿过各一条，
只进入一个新街区。对角线经过点 `(k·a/g, k·b/g)`，所以恰好遇到 `g − 1` 个
内部角点，其中 `g = gcd(a, b)`。总数为
`1 + (a − 1) + (b − 1) − (g − 1) = a + b − gcd(a, b)`。`O(log min(a, b))`。

注意事项：

- 输入给的是线的条数而不是街区数，各减一；
- 在正方形网格中，对角线经过沿途所有角点，只穿过 `a` 个街区；
- 只有一行或一列时，飞行会经过其中每个街区。

答案已对所有 `N, M ≤ 40` 以及所有测试，与按列精确取整统计对角线下街区数的
结果比对。

## 各语言说明

- 所有语言使用同一个公式。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1139_number_theory.cpp](1139_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 128 KB |
| [1139_number_theory.go](1139_number_theory.go) | Go 1.14 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 1060 KB |
| [1139_number_theory.java](1139_number_theory.java) | Java 1.8 | number_theory | O(log min(N, M)) | AC | 0.109 s | 1592 KB |
| [1139_number_theory.py](1139_number_theory.py) | Python 3.12 x64 | number_theory | O(log min(N, M)) | AC | 0.078 s | 400 KB |
| [1139_number_theory.rs](1139_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 248 KB |
