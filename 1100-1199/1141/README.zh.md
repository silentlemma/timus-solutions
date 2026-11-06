# 1141. 通过分解模数解密小规模 RSA 消息

[Timus 1141](https://acm.timus.ru/problem.aspx?space=1&num=1141) · 难度 363 · number_theory

原题作者：Mikhail Medvedev。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对最多 `K ≤ 2000` 组询问 `e, n, c ≤ 32000`，其中 `n = p·q` 为两个不同奇素数
之积，`e < (p − 1)(q − 1)` 且与 `(p − 1)(q − 1)` 互素，求满足
`m^e ≡ c (mod n)` 的消息 `m`。

时间限制：1 秒。内存限制：64 MB。

## 输入

`K`，然后 `K` 行，每行是 `e`、`n` 和 `c`。

## 输出

每行一个 `m`。

## 样例

### 样例 1

输入：

```
3
9 187 129
11 221 56
7 391 204
```

输出：

```
7
23
17
```

## 解法

这是模数极小的 RSA，可以直接破解。从 3 开始用奇数试除，最多 `√n < 179` 步
就能找到 `p`，于是 `φ = (p − 1)(q − 1)`。由于 `e` 与 `φ` 互素，它在模 `φ` 下
有逆元 `d`，用扩展欧几里得算法求出。于是 `c^d ≡ m^(e·d) ≡ m (mod n)`：对
整除 `n` 的每个素数 `r`，`e·d = 1 + t·φ` 等于 `1` 加上 `r − 1` 的倍数，由费马
小定理得 `m^(e·d) ≡ m (mod r)`，即使 `r` 整除 `m` 也成立，再用中国剩余定理
合并两个素数。所以 `m = c^d mod n`，用快速幂求出。每组询问
`O(√n + log n)`。

注意事项：

- `c` 可能大于 `n`，快速幂会先对它取模；
- 消息可能与 `n` 有公因子；由于 `n` 不含平方因子，解密仍然成立；
- 扩展欧几里得算法得到的逆元可能为负，要调整到 `[0, φ)`；
- 所有乘积都小于 `32000²`，在 64 位整数范围内。

答案已在所有测试上与枚举 `0` 到 `n − 1` 的全部 `m` 的结果比对，同时确认了
答案唯一。

## 优化解法

Go 和 Rust 一次筛出不超过 178 的奇质数，仅用这些质数分解每个 n ≤ 32000 的模数。随后用扩展欧几里得算法求逆指数，再用二进制快速幂解密。Go 使用固定字节缓冲区并直接输出十进制数字；Rust 逐步处理输入输出。质数表使用固定大小的数组。

已通过评测的基础实现 [1141_number_theory.cpp](1141_number_theory.cpp), [1141_number_theory.java](1141_number_theory.java), [1141_number_theory.py](1141_number_theory.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

以下说明针对基础实现。

- 所有语言用同样的方式分解、求逆和求幂；Python 用内置的
  `pow(e, -1, phi)` 求逆元。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1141_number_theory.cpp](1141_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 216 KB | 11279444 |
| [1141_number_theory.go](1141_number_theory.go) | Go 1.14 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 1156 KB | 11279445 |
| [1141_number_theory.java](1141_number_theory.java) \* | Java 1.8 | number_theory | O(K (√n + log n)) | AC | 0.046 s | 596 KB | 11279448 |
| [1141_number_theory.py](1141_number_theory.py) \* | Python 3.12 x64 | number_theory | O(K (√n + log n)) | AC | 0.046 s | 992 KB | 11279446 |
| [1141_number_theory.rs](1141_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 352 KB | 11279449 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1141_number_theory_optimized.go](1141_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(K (√n + log n)) | AC | 0.015 s | 772 KB | 11311153 |
| [1141_number_theory_optimized.rs](1141_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 200 KB | 11311025 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
