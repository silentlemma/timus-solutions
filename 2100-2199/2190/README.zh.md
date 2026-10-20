# 2190. 把石堆调成指定比例的最少搬动次数

[Timus 2190](https://acm.timus.ru/problem.aspx?space=1&num=2190) · 难度 1081 · math, sorting

原题作者 Vadim Barinov，出自 2022 年 ICPC 乌拉尔赛区资格赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 N 堆石头，第 i 堆有 sᵢ 块。每分钟可以加上或拿走一块石头。求最少多少分钟后各堆满足比例 p₁ : … : p_N，且不全为空。时间限制 2 秒，内存限制 256 MB。

## 输入

N（2 ≤ N ≤ 10⁵），然后是 s₁ … s_N 和 p₁ … p_N，都在 1 到 10⁹ 之间。

## 输出

最少的分钟数。

## 样例

### 样例 1

输入：

```
2
21 34
2 3
```

输出：

```
2
```

## 解法

把所有 pᵢ 除以它们的最大公约数得到 qᵢ。满足这个比例的非空石堆恰好是 k · qᵢ，其中 k ≥ 1 为整数，所以答案是下式对 k 的最小值：

cost(k) = Σ |sᵢ − k qᵢ| = Σ qᵢ · |sᵢ / qᵢ − k|。

这是 k 到各点 sᵢ / qᵢ 的距离以 qᵢ 为权的和，是凸函数，在实数上于加权中位数处取最小：把比值排序，比较 a / b 与 c / d 时用 64 位比较 a · d 和 c · b，取累计权重第一次达到总和一半的那个比值。最优整数是该比值的下取整或再加一，下取整为零时跳过。两个候选值与实数最小点的距离都不超过 1，所以每个代价都不超过 cost(1) + Σqᵢ ≤ 2 · 10¹⁴，在 64 位范围内。

样例中比值为 10.5 和 11.33，第二个的权重是 5 中的 3，它就是中位数，k = 11 得到 22 和 33，代价为 1 + 1。

排序使复杂度为 O(N log N)。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2190_math_sorting.cpp](2190_math_sorting.cpp) | G++ 13.2 x64 | math, sorting | O(N log N) | AC | 0.203 s | 1564 KB |
| [2190_math_sorting.go](2190_math_sorting.go) | Go 1.14 x64 | math, sorting | O(N log N) | AC | 0.078 s | 5848 KB |
| [2190_math_sorting.java](2190_math_sorting.java) | Java 1.8 | math, sorting | O(N log N) | AC | 0.140 s | 2732 KB |
| [2190_math_sorting.py](2190_math_sorting.py) | Python 3.12 x64 | math, sorting | O(N log N) | AC | 0.875 s | 24836 KB |
| [2190_math_sorting.rs](2190_math_sorting.rs) | Rust 1.75 x64 | math, sorting | O(N log N) | AC | 0.062 s | 5304 KB |
