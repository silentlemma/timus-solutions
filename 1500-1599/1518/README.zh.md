# 1518. 绝地谜题 3

[Timus 1518](https://acm.timus.ru/problem.aspx?space=1&num=1518) · 难度 1045 · math

原题作者 Ilya Grebnov、Nikita Rybak 与 Dmitry Kovalioff，出自 Timus Top Coders: Third Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给出密钥 K1 … KN（1 ≤ N ≤ 100，每个在 0 到 100 之间），之后的每个密钥满足
Ki = (Ki−1·CN + Ki−2·CN−1 + … + Ki−N·C1) mod Y，其中偏移 Ci 为 0 或 1，
2 ≤ Y < 2²⁸。对 N < X < 2²⁸ 求 KX。

时间限制：1.5 秒。内存限制：64 MB。

## 输入

N、X、Y，然后是 N 个密钥，再是 N 个偏移。

## 输出

KX。

## 样例

### 样例 1

输入:

```
3 6 73
12 91 65
1 1 0
```

输出:

```
22
```

## 解法

从 K1 开始数，KX 是线性递推的第 X − 1 项。它的特征多项式为
P(x) = x^N − Σ x^(N−j)，求和取所有满足 C(N+1−j) = 1 的 j。用快速幂计算 x^(X−1) 模
P(x) 和 Y：两个次数小于 N 的多项式相乘，再把每个 d ≥ N 的项 x^d 折回，即把 x^N 换
成上面的和。若 x^(X−1) ≡ r0 + r1·x + … + r(N−1)·x^(N−1)，则
KX = r0·K1 + r1·K2 + … + r(N−1)·KN mod Y。每次乘法 `O(N²)`，约 2·28 次乘法，共
`O(N² log X)`，大约 10⁶ 次运算；而 100 × 100 矩阵快速幂约需 6·10⁷ 次乘法。

注意事项：

- X 可达 2²⁸ − 1，逐个推算密钥太慢（gen5）；
- 乘积小于 2⁵⁶；64 位版本每次乘后取模，Python 稍后取模（测试 05、gen5）；
- 给出的密钥可能达到 Y，也要取模（测试 07）；
- N = 1 时多项式为一次式：x 被换成 C1（测试 02、03）；
- 所有偏移都为 0 时，之后的密钥全为 0（测试 04）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1518_math.cpp](1518_math.cpp) | G++ 13.2 x64 | math | O(N^2 log X) | AC | 0.015 s | 204 KB |
| [1518_math.go](1518_math.go) | Go 1.14 x64 | math | O(N^2 log X) | AC | 0.031 s | 1200 KB |
| [1518_math.java](1518_math.java) | Java 1.8 | math | O(N^2 log X) | AC | 0.140 s | 3120 KB |
| [1518_math.py](1518_math.py) | Python 3.12 x64 | math | O(N^2 log X) | AC | 0.109 s | 544 KB |
| [1518_math.rs](1518_math.rs) | Rust 1.75 x64 | math | O(N^2 log X) | AC | 0.046 s | 244 KB |
