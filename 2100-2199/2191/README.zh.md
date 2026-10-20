# 2191. 把折线写成恰好 N 个带符号绝对值之和

[Timus 2191](https://acm.timus.ru/problem.aspx?space=1&num=2191) · 难度 1765 · math, constructive

原题作者 Valentin Zuev 和 Vadim Barinov，出自 2022 年 ICPC 乌拉尔赛区资格赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

分段线性函数由 N 个顶点 (xᵢ, yᵢ) 给出，xᵢ 严格递增。在 [x₁, x_N] 上把它写成恰好 N 项的 ±|a₁x + b₁| ± … ± |a_N x + b_N|，格式同样例。时间限制 3 秒，内存限制 256 MB。

## 输入

N（2 ≤ N ≤ 10⁵），然后是 N 个顶点，整数坐标的绝对值不超过 10⁵。

## 输出

一行表达式。

## 样例

### 样例 1

输入：

```
2
1 0
2 1
```

输出：

```
|1x-1|+|0x+0|
```

### 样例 2

输入：

```
2
0 1
1 2
```

输出：

```
|1x-0|+|0x+1|
```

### 样例 3

输入：

```
3
-1 1
0 -1
1 0
```

输出：

```
|1.5x-0|-|0.5x+0.5|-|0x+0.5|
```

## 解法

设 sᵢ 为第 i 段的斜率。在内部顶点 xᵢ 处斜率从 sᵢ₋₁ 变为 sᵢ，而项 cᵢ |x − xᵢ|（cᵢ = (sᵢ − sᵢ₋₁) / 2）恰好产生这个转折，因为它的斜率在那里跳变 2cᵢ。N − 2 个内部顶点用掉 N − 2 项，在 [x₁, x_N] 上剩下的是一个线性函数，用剩下的两项写出：

- 在区间上 α |x − x₁| 等于 α(x − x₁)。在所有转折点左侧，转折项的斜率为 −Σcᵢ = −(s_last − s₁) / 2，所以 α = (s₁ + s_last) / 2 恢复第一段的斜率。
- 常数 β 写成 |0x + β|，β 的符号放在前面，用来调整 x₁ 处的值：β = y₁ − Σ cᵢ (xᵢ − x₁)。

这个和看起来是许多分数的混合，但分部求和把 Σ (sᵢ − sᵢ₋₁)(xᵢ − x₁) 变成 s_last (x_{N−1} − x₁) − (y_{N−1} − y₁)，因为每个 sⱼ 乘以其所在段的宽度就是该段的升高量。因此 cᵢ 和 α 的分子是两个坐标差乘积的和或差，分母是两个坐标差乘积的两倍。截距 bᵢ = −cᵢ xᵢ 的分子还需要一个坐标因子。每个坐标差的绝对值不超过 2·10⁵，因此这个分子的绝对值不超过 8·10¹⁵；构造系数时的整数运算都能放进有符号 64 位。

易错点（测试 13–14）：坐标边界附近的大斜率需要 64 位中间整数，计算截距时还要包含额外的因子 xᵢ。

每个分数都用整数除法截断到 18 位小数并去掉末尾的零，所以每个系数的误差至多约 10⁻¹⁸。如果先对斜率舍入，误差就会沿折线累积。

第三个样例中斜率为 −2 和 1，所以 0 处的转折是 1.5|x|，α = −0.5，β = 1 − 1.5 = −0.5。

复杂度 O(N)，每个数 18 位。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2191_math_constructive.cpp](2191_math_constructive.cpp) | G++ 13.2 x64 | math, constructive | O(N) | AC | 0.234 s | 5020 KB |
| [2191_math_constructive.go](2191_math_constructive.go) | Go 1.14 x64 | math, constructive | O(N) | AC | 0.093 s | 14532 KB |
| [2191_math_constructive.java](2191_math_constructive.java) | Java 1.8 | math, constructive | O(N) | AC | 0.218 s | 22016 KB |
| [2191_math_constructive.py](2191_math_constructive.py) | Python 3.12 x64 | math, constructive | O(N) | AC | 0.593 s | 28096 KB |
| [2191_math_constructive.rs](2191_math_constructive.rs) | Rust 1.75 x64 | math, constructive | O(N) | AC | 0.062 s | 9732 KB |
