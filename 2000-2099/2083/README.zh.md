# 2083. 沿循环加权的置换幂之和

[Timus 2083](https://acm.timus.ru/problem.aspx?space=1&num=2083) · 难度 2652 · math

原题作者 Denis Dublennykh。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 1 … n 的置换 p。m × n 矩阵 A 的第 t 行是 p 作用 t 次：A[t][j] = pᵗ(j)（第一行就是 p）。对给定长度为 m 的 q 计算向量 q × A，即 v[j] = q₁ p(j) + q₂ p²(j) + … + q_m pᵐ(j)。时间限制 4 秒，内存限制 256 MB。

## 输入

m 和 n（2 ≤ m, n ≤ 5·10⁴），然后是 p(1) … p(n)，然后是 q₁ … q_m（0 ≤ qᵢ ≤ 10⁹）。

## 输出

q × A 的 n 个分量。

## 样例

### 样例 1

输入：

```
3 4
3 2 4 1
3 5 8
```

输出：

```
37 32 41 50
```

## 解法

把 p 分解成循环。在循环 c₀, c₁, …, c_{L−1} 上，p(c_s) = c_{s+1}（下标模 L），所以 pᵗ(c_s) = c_{(s+t) mod L}。按 t 模 L 的余数折叠 q：Q[r] 为所有 t ≡ r (mod L) 的 q_t 之和。于是 v[c_s] = Σ_r Q[r] · c_{(s+r) mod L}，是长度为 L 的循环相关。折叠只依赖于 L，而不同的循环长度至多约 √(2n) 种，所以折叠总共 O(m √n)。

相关就是多项式乘积：反转的 Q 乘以写两遍的循环，系数 s + L − 1 就是 v[c_s]。数值可达 5·10⁴ · 5·10⁴ · 10⁹ = 2.5·10¹⁸，所以乘积必须精确。C++、Go、Java 和 Rust 在三个素数（998244353、167772161、469762049）下做数论变换，再用 Garner 方法合并系数；结果小于 2⁶³，所以带溢出的 64 位运算能精确得到它。Python 把每个序列打包成一个大整数，每个数占十个字节，把两个整数相乘后再读回系数，因为没有系数会超出它的十个字节。短循环（长度至多 32）直接求和。乘积总计 O(n log n)。

样例中 p 是循环 1 → 3 → 4 → 1 加上不动点 2，v[2] = (3 + 5 + 8) · 2 = 32。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2083_math.cpp](2083_math.cpp) | G++ 13.2 x64 | math | O(n log n + m sqrt n) | AC | 0.593 s | 12432 KB |
| [2083_math.go](2083_math.go) | Go 1.14 x64 | math | O(n log n + m sqrt n) | AC | 0.734 s | 19740 KB |
| [2083_math.java](2083_math.java) | Java 1.8 | math | O(n log n + m sqrt n) | AC | 1.500 s | 16236 KB |
| [2083_math.py](2083_math.py) | Python 3.12 x64 | math | O(n log n + m sqrt n) | AC | 2.781 s | 27692 KB |
| [2083_math.rs](2083_math.rs) | Rust 1.75 x64 | math | O(n log n + m sqrt n) | AC | 0.593 s | 12824 KB |
