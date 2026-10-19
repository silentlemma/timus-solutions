# 1855. 埃拉西亚的商会

[Timus 1855](https://acm.timus.ru/problem.aspx?space=1&num=1855) · 难度 1262 · fenwick

原题作者 Alexander Fetisov（由 Denis Dublennykh 准备），出自 2011 年 8 月彼得罗扎沃茨克夏季集训的 Ural SU Team.GOV Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 座城市沿一条商路排列，每段相邻城市之间的路都要收通行费，最初为 0。事件依次发生：一次变更把城市 a 和 b 之间每一段的通行费加上 d；一个新商会在城市 a … b 中经营，其商队在这些城市的每一对之间往来的频率相同。
对每个新商会，输出此刻其一支商队平均支付的通行费。

## 输入

n 和 m（2 ≤ n ≤ 10⁵，1 ≤ m ≤ 10⁵），然后是 m 个事件 "change a b d" 或 "establish a b"，其中 1 ≤ a < b ≤ n，|d| ≤ 10 000。每段的通行费始终在 0 和 10 000 之间。

## 输出

每个新商会的平均值，绝对或相对误差不超过 10⁻⁶。

## 样例

### 样例 1

输入：

```
4 5
change 1 4 2
change 1 2 -1
establish 1 2
establish 2 4
establish 1 4
```

输出：

```
1.00000000
2.66666667
2.83333333
```

## 解法

设 tᵢ 为从城市 i 到城市 i + 1 那一段的通行费。位于城市 a … b 的商会共有 (b − a + 1)(b − a)/2 条路线，第 i 段位于其中 (i − a + 1)(b − i) 条上，即起点不晚于 i、终点在其之后的那些路线。
展开乘积，总通行费为 −S₂ + (a + b − 1)·S₁ + b(1 − a)·S₀，其中 S_k = Σ iᵏ·tᵢ，i 取 a … b − 1，所以只需在区间加的同时维护 tᵢ、i·tᵢ 和 i²·tᵢ 的区间和。

把通行费保存为差分 dif_j 的前缀和：一次变更在 a 处加 d、在 b 处加 −d。那么对 i ≤ x，iᵏ·tᵢ 之和等于 P_k(x)·Σ dif_j − Σ dif_j·P_k(j − 1)（j ≤ x），其中 P_k(x) 是 i = 1 … x 的 iᵏ 之和，预先算好。
在差分上建四棵树状数组——普通的以及分别以 P₀、P₁、P₂ 加权的——每个事件用 `O(log n)` 处理。

在样例中，通行费最终为 1、2、2。城市 1 … 4 上的商会有六条路线，通行费为 1、3、5、2、4、2，即 17/6 ≈ 2.8333。

注意事项：

- 加权和在计算过程中会超出 64 位；Python 的整数是精确的，其他解法按 2⁶⁴ 取模计算，由于最终总和小于 2.5·10¹⁸，结果仍然精确；
- 商会的总和直到最后才需要做除法；
- Python 版本在 PyPy 上运行。

在两百个小数据上平均值与直接计算一致，在大测试上与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1855_fenwick.cpp](1855_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((n + m) log n) | AC | 0.375 s | 4484 KB |
| [1855_fenwick.go](1855_fenwick.go) | Go 1.14 x64 | fenwick | O((n + m) log n) | AC | 0.109 s | 8196 KB |
| [1855_fenwick.java](1855_fenwick.java) | Java 1.8 | fenwick | O((n + m) log n) | AC | 0.421 s | 15736 KB |
| [1855_fenwick.py](1855_fenwick.py) | PyPy 3.10 x64 | fenwick | O((n + m) log n) | AC | 0.406 s | 37656 KB |
| [1855_fenwick.rs](1855_fenwick.rs) | Rust 1.75 x64 | fenwick | O((n + m) log n) | AC | 0.046 s | 11256 KB |
