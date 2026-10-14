# 1595. 完美序列

[Timus 1595](https://acm.timus.ru/problem.aspx?space=1&num=1595) · 难度 1154 · constructive

原题作者 Alexander Bacherikov。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

输出一个由互不相同的正整数组成的序列，每个数不超过 10¹³，序列包含 1, 2, …, N 的全部数（1 ≤ N ≤ 250000），
长度不超过 2N，且对每个 k，前 k 项之和都能被 k 整除。任何满足条件的序列都可接受。

时间限制：1 秒。内存限制：64 MB。

## 输入

N。

## 输出

用空格分隔的序列。

## 样例

### 样例 1

输入:

```
3
```

输出:

```
1 3 2 6 8
```

## 解法

按顺序放入 1, 2, …, N，每个数前面先放一个额外项 x：设 S 为当前和、k 为 x 的位置，则 x 要使 S + x 被 k 整除，
接着下一个数 m 要使 S + x + m 被 k + 1 整除。于是 x ≡ a = −S (mod k)，x ≡ b = −S − m (mod k + 1)。
k 与 k + 1 互素，由中国剩余定理得到模 k(k + 1) 的一个剩余类，而且很容易写出来：x = a + k·t，而 k ≡ −1 (mod k + 1)，
所以 t ≡ a − b (mod k + 1)，不需要求逆元。取该类中第一个大于 N 的 x，保证它不与 1..N 重复；
若与之前少数额外项相撞，就按 k(k + 1) 跳过，所有项便各不相同。序列恰有 2N 项，用哈希集合 `O(N)` 步即可构造。

除非需要跳过已用的值，每个 x 都不超过 N + k(k + 1)，而 k < 2N，所以各项远小于 10¹³；N = 250000 时最大项约为 5·10⁸。
测试使用检查器，已在所有不超过 300 的 N 以及最大的 N 上运行。

注意事项：

- 样例答案只是众多答案之一，检查器接受任何合法序列；
- 前缀和可达约 6·10¹³，超出 32 位整数；
- 500000 个数的输出有好几兆字节，所以输出要经过缓冲，而不是一个数一个数地写。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1595_constructive.cpp](1595_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.109 s | 17152 KB |
| [1595_constructive.go](1595_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.109 s | 11600 KB |
| [1595_constructive.java](1595_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.328 s | 34196 KB |
| [1595_constructive.py](1595_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.500 s | 18112 KB |
| [1595_constructive.rs](1595_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.078 s | 12540 KB |
