# 1204. 模两个素数之积的幂等元

[Timus 1204](https://acm.timus.ru/problem.aspx?space=1&num=1204) · 难度 229 · number_theory

原题作者 Pavel Atnashev，出自 2002 年 3 月乌拉尔国立大学团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

若 `x·x ≡ x (mod n)`，则称 `x` 是模 `n` 的幂等元。对最多 1000 个 `n < 10⁹`，
每个都是两个不同素数 `p` 与 `q` 之积，按升序列出 `0` 到 `n − 1` 之间的所有幂等元。

时间限制：1 秒。内存限制：64 MB。

## 输入

测试数 `k`，然后每个测试一个 `n`。

## 输出

每个测试一行，按升序输出它的幂等元。

## 样例

### 样例 1

输入：

```
3
6
15
910186311
```

输出：

```
0 1 3 4
0 1 6 10
0 1 303395437 606790875
```

## 解法

`x(x − 1) ≡ 0 (mod pq)` 意味着 `p` 和 `q` 各自整除 `x` 或 `x − 1`，即模每个
素数时 `x` 为 0 或 1。由中国剩余定理恰好得到四个幂等元：0、1、模 `p` 余 1 且模
`q` 余 0 的数，以及模 `p` 余 0 且模 `q` 余 1 的数。第三个是
`x = q·(q⁻¹ mod p)`，逆元用扩展欧几里得算法求出；第四个是 `n + 1 − x`，因为二者
之和模两个素数都余 1。

为了分解 `n`，用筛法预先求出不超过 `√10⁹ < 31623` 的素数逐个试除；较小的因子必在
其中。每个测试最多约 3400 次除法。`O(k·π(√n))`。

注意事项：

- 两个非平凡幂等元要按升序输出，哪一个更小都有可能；
- 只需用试除法找出较小的因子；较大的因子可达 `5·10⁸`，直接取 `n / p` 即可；
- `p` 可以小到 2。

答案已在三类共 3000 个生成的乘积上与另一份独立解答比对。

## 各语言说明

- Python 用 `pow(q, -1, p)` 求逆元；其他语言用扩展欧几里得算法。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1204_number_theory.cpp](1204_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 228 KB |
| [1204_number_theory.go](1204_number_theory.go) | Go 1.14 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 1320 KB |
| [1204_number_theory.java](1204_number_theory.java) | Java 1.8 | number_theory | O(k·π(√n)) | AC | 0.171 s | 1088 KB |
| [1204_number_theory.py](1204_number_theory.py) | Python 3.12 x64 | number_theory | O(k·π(√n)) | AC | 0.312 s | 1016 KB |
| [1204_number_theory.rs](1204_number_theory.rs) | Rust 1.75 x64 | number_theory | O(k·π(√n)) | AC | 0.015 s | 268 KB |
