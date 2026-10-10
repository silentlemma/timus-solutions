# 1118. 真因数和与自身之比最小的数

[Timus 1118](https://acm.timus.ru/problem.aspx?space=1&num=1118) · 难度 103 · number_theory

原题作者 Leonid Volkov，出自 2001 年 10 月 USU Open Collegiate Programming Contest（Junior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

正整数 `N` 的比值是它的真因数（小于 `N` 的因数）之和除以 `N`。对 `1 ≤ I ≤ J ≤ 10^6`，输出 `[I, J]` 中比值最小的一个数。

时间限制：2 秒。内存限制：64 MB。

## 输入

一行 `I J`。

## 输出

比值最小的数。

## 评测方式

输出按记号逐个比较；多余的空白字符无关紧要。

## 样例

### 样例 1

输入：

```
24 28
```

输出：

```
25
```

## 解法

1 没有真因数，比值为 0，只要 `I = 1` 它就胜出。素数 `p` 的比值是 `1/p`，所以素数中最大的最好。它也胜过范围内每个合数
`n ≤ J`：合数除 1 外还有一个因数 `d ≥ √n`，所以它的比值至少为 `(1 + √n)/n`，而不超过 `J` 的最大素数大于 `J/2`（伯特兰假设），使得
`1/p` 更小。于是从 `J` 往下扫，遇到第一个素数就停。

只有当范围内完全没有素数时才需要比较比值；这样的范围位于两个素数之间的空隙中，在 `10^6` 以下至多 113 个数。每个因数和用试除在 `O(√n)`
内求出，两个比值精确地按 `σ(a)·b < σ(b)·a` 比较，相等时较小的数胜出。总计 `O(g · √J)`，`g` 为最大空隙。

注意事项：

- `I = 1` 时答案是 1，而不是最大的素数；
- 在没有素数的范围里，最好的数不一定最大，也不一定是平方数：`[24, 28]` 给出 25，`[8, 10]` 给出 9；
- 不必用浮点数比较比值，交叉乘积放得进 64 位。

答案经过验证：与一个对 `10^6` 以内所有数求因数和的筛法、并在整个范围上精确比较的程序比对，覆盖所有测试、200 个小于 3000 的随机范围，以及一百万以内最长的素数间隙。

## 各语言说明

- 各语言都使用同样的试除法。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1118_number_theory.cpp](1118_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.015 s | 128 KB |
| [1118_number_theory.go](1118_number_theory.go) | Go 1.14 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.031 s | 1060 KB |
| [1118_number_theory.java](1118_number_theory.java) | Java 1.8 | number_theory | O(g · √J), g ≤ 114 | AC | 0.109 s | 1552 KB |
| [1118_number_theory.py](1118_number_theory.py) | Python 3.12 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.093 s | 440 KB |
| [1118_number_theory.rs](1118_number_theory.rs) | Rust 1.75 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.031 s | 212 KB |
