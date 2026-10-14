# 1561. 小熊维尼

[Timus 1561](https://acm.timus.ru/problem.aspx?space=1&num=1561) · 难度 2840 · math

原题出自 2007 年 9 月彼得罗扎沃茨克集训的 Novosibirsk SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Winnie 吃同一种蜂蜜的每一桶都用相同的整数天数，每种蜂蜜的天数未知。依次给出至多 1000 个查询：`Add`
加入一种新蜂蜜；`Learn A0 … Ak S E` 表示从星期 S 开始吃
0 号蜂蜜 A0 桶、…、k 号蜂蜜 Ak 桶，吃完后的第一天是星期 E；`Eat A0 … Ak S` 询问吃完后的这个第一天
是星期几（0 ≤ Ai ≤ 10⁶）。对每个 `Eat`，若已
有事实能确定，输出星期几；若允许多种结果，输出 `Don't know`；若已有事实互相矛盾，输出
`Already crazy`。

时间限制：2 秒。内存限制：64 MB。

## 输入

查询个数，然后每行一个查询，星期写作 Monday … Sunday。

## 输出

每个 `Eat` 查询输出一行。

## 样例

### 样例 1

输入:

```
9
Add
Add
Learn 5 2 Saturday Monday
Eat 3 3 Tuesday
Add
Learn 0 9 4 Friday Thursday
Eat 3 0 6 Sunday
Learn 3 2 10 Saturday Friday
Eat 3 4 11 Monday
```

输出:

```
Don't know
Saturday
Already crazy
```

## 解法

对星期几来说，只有天数模 7 有意义，而且任何余数都可能，因为一种蜂蜜可以要吃 7 天。所以未知量 x₀, x₁, …
属于模 7 的剩余类域，一个事实就是线性方程 A0·x₀ + … + Ak·xk = E − S，而从 S 开始吃完后第一天是
S + A0·x₀ + … + Ak·xk。

事实以阶梯形基保存：每行在其第一个非零位置（主元）上为 1，各行主元互不相同。新向量按主元递增的顺序减去
各行的倍数，同时处理右端。化为零的事实要么是多余的，要么（右端非零时）是矛盾，此后每顿饭都回答
`Already crazy`；否则它成为新的一行。当且仅当一顿饭的向量化为零时它是确定的，这时途中累积的右端等于其
持续天数的相反数（模 7）。每次化简耗时 O(R·K)（R 行、K 种蜂蜜）。结果已在随机小测试上与枚举所有余数的
做法对照。

注意事项：

- 关于一桶也不吃的饭的事实，除非 S = E，否则就是矛盾（测试 03）；
- 7 的倍数桶数对每桶天数毫无信息（测试 04）；
- 一旦事实互相矛盾，之后每顿饭都回答 `Already crazy`，但之前的回答保持不变（测试 05）；
- 新的蜂蜜可能在事实之后才出现，所以保存的行比后来的向量短；
- Python 在 PyPy 下运行：最大的测试在 CPython 下约需 1.1 秒（限制为 2 秒），在 PyPy 下约 0.3 秒。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1561_math.cpp](1561_math.cpp) | G++ 13.2 x64 | math | O(N^2 K) | AC | 0.328 s | 1076 KB |
| [1561_math.go](1561_math.go) | Go 1.14 x64 | math | O(N^2 K) | AC | 0.171 s | 5804 KB |
| [1561_math.java](1561_math.java) | Java 1.8 | math | O(N^2 K) | AC | 0.421 s | 8276 KB |
| [1561_math.py](1561_math.py) | PyPy 3.10 x64 | math | O(N^2 K) | AC | 0.750 s | 29076 KB |
| [1561_math.rs](1561_math.rs) | Rust 1.75 x64 | math | O(N^2 K) | AC | 0.125 s | 2880 KB |
