# 1634. 叶螨

[Timus 1634](https://acm.timus.ru/problem.aspx?space=1&num=1634) · 难度 2218 · combinatorics

原题作者 Igor Chevdar（由 Alexander Ipatov 准备），出自第十三届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每次喷药后，N 个种着树的木桶按固定的排列 P 重新摆放；当所有木桶第一次回到各自原来的位置时，
螨卵就会死去。若 P 在 N 个元素的所有排列中等概率选取，求喷药次数的期望并输出其整数部分。

## 输入

一个整数 N（1 ≤ N ≤ 50）。

## 输出

期望喷药次数的整数部分。

## 样例

### 样例 1

输入：

```
2
```

输出：

```
1
```

## 解法

喷药次数就是 P 的阶：它各个循环长度的最小公倍数。对每个 k 恰有 m_k 个长为 k 的循环的循环类型，
在等概率选取排列时的概率是 1 / Π k^(m_k) m_k!（给定循环类型的排列计数的经典结果），所以期望是对
所有循环类型求和。

N = 50 时有 204226 种循环类型，但许多类型的最小公倍数相同。对循环长度做背包可以把它们合并：
dp[s][l] 表示 s 个元素的随机排列只用到已考虑过的长度 1…k、且这些长度的最小公倍数为 l 的概率。
加入 m ≥ 1 个长为 k 的循环，就把 dp[s][l] 的权重乘以 1 / (k^m m!)（每步将权重除以 k · m）转移
到 dp[s + mk][lcm(l, k)]。N = 50 时每个规模的不同最小公倍数只有一千个左右（Landau 函数把它们
限制在 180180 以内）。答案为 Σ l · dp[N][l]。L 为每个规模的最大状态数。

double 就够了：在全部 50 个输入上，精确的期望值（另行用分数算出）与上方整数的距离从不小于
0.005，只有 N = 1 时期望恰好为 1，加上 10⁻⁹ 可保持它为整数。期望增长很慢：N = 50 时为 1069.51。

易错点：

- 阶是循环长度的最小公倍数，而不是它们的积或和；
- 用精确大数枚举所有划分是正确的，但在某些语言中很慢；按最小公倍数合并能大大减少计算；
- 精确的整数在截断时必须保住：若和算成 0.9999999…，N = 1 时就会输出 0（测试 02）。

在全部 50 个输入上，答案与精确的有理数值一致，也与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1634_combinatorics.cpp](1634_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N² log N · L log L) | AC | 0.046 s | 1520 KB |
| [1634_combinatorics.go](1634_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N² log N · L) | AC | 0.109 s | 6216 KB |
| [1634_combinatorics.java](1634_combinatorics.java) | Java 1.8 | combinatorics | O(N² log N · L) | AC | 0.203 s | 8348 KB |
| [1634_combinatorics.py](1634_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N² log N · L) | AC | 0.203 s | 2728 KB |
| [1634_combinatorics.rs](1634_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N² log N · L) | AC | 0.046 s | 1736 KB |
