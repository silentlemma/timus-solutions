# 1598. 攻击 DSA

[Timus 1598](https://acm.timus.ru/problem.aspx?space=1&num=1598) · 难度 3852 · math

原题由 Vladimir Yakovlev 准备。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

DSA 公钥 (q, p, g, y) 包含一个 N 位素数 q（3 ≤ N ≤ 36）、一个 L 位素数 p（L ≤ 60，且 q 整除 p − 1）、
模 p 阶为 q 的 g，以及对秘密的 0 < x < q 有 y = gˣ mod p。给定公钥和哈希值 H，输出任意一个合法签名 (r, s)：
0 < r, s < q，并且令 w = s⁻¹、u₁ = H·w、u₂ = r·w（模 q），有 ((g^u₁·y^u₂) mod p) mod q = r。

时间限制：1 秒。内存限制：64 MB。

## 输入

N、L、q、p、g、y 和 H。

## 输出

r 和 s。

## 样例

### 样例 1

输入:

```
3 6 5 41 10 16 2
```

输出:

```
3 3
```

## 解法

哈希值是给定的，所以那些为某条消息伪造签名的常见技巧都没用：解法要求出私钥。g 的阶为 q，所以 x 是 y 在至多 2³⁶
个元素的群中的离散对数，用小步大步法约 √q ≈ 2.6·10⁵ 步即可求出：把 j < m = ⌈√q⌉ 的 gʲ 存进哈希表，
然后不断把 y 乘以 g⁻ᵐ = g^(q − m)，直到值出现在表中；若 i 步后得到 gʲ，则 x = i·m + j。

知道 x 后按题目所述签名，k 依次取 1, 2, …，直到 r = (gᵏ mod p) mod q 与 s = k⁻¹(H + x·r) mod q 都不为零。
q 是素数，所以 k⁻¹ = k^(q − 2) mod q。验证随之成立：u₁ + x·u₂ = (H + x·r)·w = k，故 g^u₁·y^u₂ = gᵏ。
总共 `O(√q)` 的时间和内存。

测试使用按题目方式验证签名的检查器。它在严格按描述生成的、从极小到 N = 36、L = 60 各种规模的公钥上都接受了输出。

注意事项：

- p 最多 60 位，乘积需要 128 位：C++ 和 Rust 用 128 位整数，Go 用 bits.Mul64 加 bits.Rem64，
  Java 8 两者都没有，于是每次乘两位，使每个和都小于 2⁶³；
- k = 1 时可能 r = g mod q = 0（样例就是如此），所以 k 要继续往后试；
- H 有 N 位，可能大于 q，按模 q 使用。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1598_math.cpp](1598_math.cpp) | G++ 13.2 x64 | math | O(√q) | AC | 0.109 s | 12456 KB |
| [1598_math.go](1598_math.go) | Go 1.14 x64 | math | O(√q) | AC | 0.093 s | 20784 KB |
| [1598_math.java](1598_math.java) | Java 1.8 | math | O(√q) | AC | 0.312 s | 9832 KB |
| [1598_math.py](1598_math.py) | Python 3.12 x64 | math | O(√q) | AC | 0.265 s | 26936 KB |
| [1598_math.rs](1598_math.rs) | Rust 1.75 x64 | math | O(√q) | AC | 0.046 s | 17656 KB |
