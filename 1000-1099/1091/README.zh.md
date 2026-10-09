# 1091. 统计有公因数的数集

[Timus 1091](https://acm.timus.ru/problem.aspx?space=1&num=1091) · 难度 526 · number_theory

原题作者 Stanislav Vasiliev，出自 2001 年 3 月 USU Open Collegiate Programming Contest（Senior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计由 `K` 个不同正整数组成、每个数都不超过 `S`（`2 ≤ K ≤ S ≤ 50`）且最大公因数大于 1 的集合个数。输出这个数；
若它大于 10000，则输出 10000。

时间限制：1 秒。内存限制：64 MB。

## 输入

`K` 和 `S`。

## 输出

集合个数，最多 10000。

## 评测方式

按记号逐个比较输出；多余的空白不影响结果。

## 样例

### 样例 1

输入：

```
3 10
```

输出：

```
11
```

## 题解

所有数都是 `d` 的倍数的集合共有 `C(⌊S/d⌋, K)` 个。公因数大于 1 的集合一定有一个公共的素因数，所以答案是这些
集合族在所有素数上的并集大小。对无平方因子的 `d > 1` 做容斥得到

`答案 = Σ −μ(d) · C(⌊S/d⌋, K)`，

其中莫比乌斯函数 `μ(d)` 对无平方因子的 `d` 等于 `(−1)^(素因子个数)`，否则为 0：奇数个素数之积加上，偶数个减去。
用一个小筛法求出 `S` 以内的 `μ`，二项式系数取自杨辉三角。`O(S²)`。

注意事项：

- 真实的个数可能远大于 10000，例如 `K = 5` 时仅由偶数组成的集合就有 `C(25, 5)` 个，所以只对最终结果取上限，
  中间的和用 64 位保存；
- 对 `d = 2` 和 `d = 3` 都计数的集合，对 `d = 6` 也计数了，这就是符号交替的原因；
- 各数必须不同，所以 `m < K` 时 `C(m, K)` 为 0。

答案对所有 `K ≤ S ≤ 50` 的数对，与“最大公因数恰为 `g` 的集合数”（从最大的 `g` 往下，减去 `g` 的倍数的计数）
做了核对；`S ≤ 20` 时还与枚举所有集合的结果做了核对。

## 各语言说明

- Python 使用 `math.comb`；其他语言填写二项式系数表。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1091_number_theory.cpp](1091_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(S^2) | AC | 0.015 s | 232 KB |
| [1091_number_theory.go](1091_number_theory.go) | Go 1.14 x64 | number_theory | O(S^2) | AC | 0.015 s | 1088 KB |
| [1091_number_theory.java](1091_number_theory.java) | Java 1.8 | number_theory | O(S^2) | AC | 0.109 s | 1640 KB |
| [1091_number_theory.py](1091_number_theory.py) | Python 3.12 x64 | number_theory | O(S^2) | AC | 0.078 s | 424 KB |
| [1091_number_theory.rs](1091_number_theory.rs) | Rust 1.75 x64 | number_theory | O(S^2) | AC | 0.046 s | 228 KB |
