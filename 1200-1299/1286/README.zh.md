# 1286. VAZ 牌星际飞船

[Timus 1286](https://acm.timus.ru/problem.aspx?space=1&num=1286) · 难度 654 · number_theory

原题作者 Alexander Klepinin，出自 2004 年乌拉尔国立大学个人赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

位于整点 (x, y) 的飞船只能像广义的马一样跳：跳 (±p, ±q) 或 (±q, ±p)。它能到达 (x1, y1)
吗？所有数都是绝对值不超过 2 · 10⁹ 的整数。

时间限制：1 秒。内存限制：64 MB。

## 输入

p 和 q，然后 x 和 y，然后 x1 和 y1。

## 输出

`YES` 或 `NO`。

## 样例

### 样例 1

输入：

```
4 6
0 0
10 10
```

输出：

```
YES
```

### 样例 2

输入：

```
4 6
0 0
9 9
```

输出：

```
NO
```

## 解法

设 g = gcd(|p|, |q|)。每一跳都使两个坐标改变 g 的倍数，所以位移 (dx, dy) 必须能被 g 整除。
全部除以 g 后得到互素的步长 a 和 b。跳 (a, b) 与 (a, −b) 相加得 (2a, 0)，同理可得 (2b, 0)，
由裴蜀定理可得 (2, 0) 和 (0, 2)。于是：

- 若 a、b 都是奇数，每一跳使 x + y 改变一个偶数，所以 dx/g + dy/g 必须为偶数；而跳 (a, b)
  再用 (2, 0)、(0, 2) 的倍数平移可得 (1, 1)，因此所有这样的点都可达；
- 否则不妨设 a 奇 b 偶：跳 (a, b) 同样平移可得 (1, 0)，跳 (b, a) 可得 (0, 1)，任何点都可达。

若 p = q = 0，飞船根本不能移动。`O(log max(|p|, |q|))`。

注意事项：

- p 和 q 可能都为零（测试 03、04），也可能只有一个为零（测试 05）；
- 步长可能为负（测试 11）；
- 位移可达 4 · 10⁹，超出 32 位（测试 08、09）；
- 在类 C 语言中负奇数对 2 取余为 −1，所以奇偶性要用 `% 2 != 0` 判断。

对 0 到 4 的所有步长以及距起点 8 以内的所有目标，与大棋盘上的广度优先搜索比较过。

## 各语言说明

- 所有语言都进行相同的最大公约数计算和奇偶性判断。C++、Go、Java 和 Rust 使用有符号 64 位整数，
  Python 使用任意精度整数。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1286_number_theory.cpp](1286_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 124 KB |
| [1286_number_theory.go](1286_number_theory.go) | Go 1.14 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 1092 KB |
| [1286_number_theory.java](1286_number_theory.java) | Java 1.8 | number_theory | O(log max(abs p, abs q)) | AC | 0.125 s | 1588 KB |
| [1286_number_theory.py](1286_number_theory.py) | Python 3.12 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.109 s | 464 KB |
| [1286_number_theory.rs](1286_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.031 s | 212 KB |
