# 1735. 世纪大盗

[Timus 1735](https://acm.timus.ru/problem.aspx?space=1&num=1735) · 难度 2946 · constructive

原题作者 Alexander Ipatov（创意来自 Artyom Skrobov），出自第十四届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 n 袋，每袋 k 根金属条；每袋要么全是 x 千克的金条，要么全是 y 千克的铂条，外观无法区分。
决定从每袋取多少根，使得一次精确称重就能知道哪些袋装的是铂条；若不可能则报告。

## 输入

n、k、x 和 y（3 ≤ n ≤ 20，1 ≤ k ≤ 10⁶，1 ≤ x < y ≤ 10）。

## 输出

`YES` 和 n 个数量，或者 `NO`。任何符合要求的数量都可以。

## 样例

### 样例 1

输入：

```
4 8 9 10
```

输出：

```
YES
4 5 6 8
```

## 解法

取数量 c_i 时秤显示 x·Σc_i + (y − x)·P，其中 P 是铂袋所取数量之和。第一项对任何情况都相同，
所以称重能区分铂袋当且仅当数量的全部 2ⁿ 个子集和互不相同。特别地，各数量为正且互不相同，而 x 和 y 无关紧要。

于是问题变成：n 个子集和互不相同的正整数组成的集合，其最大元素最小可以是多少。
Conway–Guy 序列 u₀ = 0，u₁ = 1，u_{m+1} = 2u_m − u_{m−r}（r = round(√(2m))）给出集合 {u_n − u_i : 0 ≤ i < n}，
它们的子集和互不相同，最大元素为 u_n：1, 2, 4, 7, 13, 24, 44, 84, 161, 309, …，n = 20 时为 267 420。
若 u_n ≤ k 则答案就是该集合，否则输出 `NO`。`O(n)`。

样例中 u₄ = 7 ≤ 8，集合为 3, 5, 6, 7。

注意事项：

- 二的幂 1, 2, 4, … 也可以，但需要 2ⁿ⁻¹ 根，n 大时远超 u_n；
- 数量为 0 会完全隐藏其所在的袋，所以每袋至少取一根。

当 n 不超过 6 时，搜索表明不存在最大元素更小的集合；对更大的 n 尚无更好的已知集合，
并且对 3 到 20 的每个 n，在 u_n 两侧的边界都与一个独立的已通过实现一致。每个输出的集合都检查过子集和互不相同。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1735_constructive.cpp](1735_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 372 KB |
| [1735_constructive.go](1735_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.015 s | 1088 KB |
| [1735_constructive.java](1735_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 1644 KB |
| [1735_constructive.py](1735_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.093 s | 460 KB |
| [1735_constructive.rs](1735_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 216 KB |
