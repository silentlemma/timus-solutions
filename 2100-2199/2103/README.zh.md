# 2103. 免费寄往倍数的最快便条

[Timus 2103](https://acm.timus.ru/problem.aspx?space=1&num=2103) · 难度 1199 · math, number_theory

原题作者 Alexey Danilyuk，出自 2016 年乌拉尔联邦大学青少年锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

员工编号为 1, 2, 3, …，按顺序坐在房间里。员工 x 可以把便条免费寄给大于 x 的任意 x 的倍数，或者送给任何其他员工，代价为两人编号之差。求董事会成员 s ≤ 7 把便条送到员工 t 的最便宜方式并输出路线。任何最优路线都可接受。时间限制 1 秒，内存限制 64 MB。

## 输入

s 和 t（1 ≤ s ≤ 7，1 ≤ t ≤ 10⁹）。

## 输出

代价、路线上的员工数以及路线。

## 评测方式

检查器比较代价并重放输出的路线。

## 样例

### 样例 1

输入：

```
5 7
```

输出：

```
2
2
5 7
```

### 样例 2

输入：

```
3 30
```

输出：

```
0
2
3 30
```

### 样例 3

输入：

```
6 1000000
```

输出：

```
1
3
6 5 1000000
```

## 解法

免费邮寄只能向上，所以到 t ≤ s 需要走 s − t 步，路线就是往下走。当 t > s 时：

- 代价为 0 当且仅当 t 是 s 的倍数：免费邮寄只能到达发件人的倍数。
- 代价为 1 意味着免费寄到 s 的倍数 m，走一步到 m ± 1，再免费寄到 t，所以 m ± 1 必须整除 t。用 O(√t) 枚举 t 的所有约数 r，寻找 r 旁边的 s 的倍数（至少为 s）。
- 否则代价为 2，而且总有路线。s ≤ 5 时，寄到离 t 最近的 s 的倍数，至多相差 2。s = 6 或 7 时，写 t = 2ᵃ 3ᵇ r，r 与 6 互质。若 r > 1，则 r ± 1 是 6 的倍数：走到 6（至多一步），寄到 r ± 1，走一步到 r，再寄到 t。若 t 是 2 的幂，它是 8 的倍数，离 6 两步、离 7 一步；若 t 是 3 的幂，它是 9 的倍数，可以 7 → 9 或 6 → 5 → 10 → 9 到达；而 6 的倍数的代价已经是 1 或 0。

第三个样例中 1 000 000 = 5 · 200 000，而 5 比 6 小一，所以代价为 1：6、5、1 000 000。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2103_math_number_theory.cpp](2103_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(sqrt t) | AC | 0.015 s | 432 KB |
| [2103_math_number_theory.go](2103_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(sqrt t) | AC | 0.031 s | 1116 KB |
| [2103_math_number_theory.java](2103_math_number_theory.java) | Java 1.8 | math, number_theory | O(sqrt t) | AC | 0.140 s | 468 KB |
| [2103_math_number_theory.py](2103_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(sqrt t) | AC | 0.109 s | 756 KB |
| [2103_math_number_theory.rs](2103_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(sqrt t) | AC | 0.046 s | 232 KB |
