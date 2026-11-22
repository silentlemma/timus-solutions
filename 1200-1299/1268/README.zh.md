# 1268. 小楚

[Timus 1268](https://acm.timus.ru/problem.aspx?space=1&num=1268) · 难度 722 · number_theory

原题作者 Pavel Atnashev，出自 2003 年 10 月 25 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

小楚在出生后第 K, K², K³, … 天醒来，并且星期几绝不能重复；一周有 N 天，N 为素数
（2 < N < 65 536），K 不超过一周。对 T ≤ 6553 个 N 中的每一个，输出使醒来次数最多的 K；
从样例可以看出，要求的是最大的那个 K。

时间限制：0.25 秒。内存限制：64 MB。

## 输入

T，然后是 T 个素数 N。

## 输出

每个 N 对应的 K，每行一个。

## 样例

### 样例 1

输入：

```
4
3
5
7
11
```

输出：

```
2
3
5
8
```

## 解法

第 i 次醒来是星期 K^i mod N。这些值以 K 模 N 的乘法阶为周期重复，所以醒来次数最多
（N − 1 次）的是原根。答案就是模 N 的最大原根。

g 是原根，当且仅当对 N − 1 的每个素因子 q 都有 g^((N−1)/q) ≠ 1 mod N。用最小素因子筛
（到 65 536）分解 N − 1，然后依次尝试 g = N − 1, N − 2, …，直到有一个通过。原根在剩余
中占相当比例，所以只需试少数几个候选，每个只做几次快速幂。重复的 N 直接查表。大约为
`O(L log log L + T · k log N)`，其中 L 为筛的上限，k 为候选个数。

注意事项：

- 任何原根都能让星期互不相同，但要求的是最大的那个（样例中 N = 11 时是 8 而不是 2）；
- 时间限制只有四分之一秒，查询多达 6553 个，所以应当用筛分解 N − 1，而不是每次从头
  试除（测试 04、05）；
- 当 N − 1 是 2 的幂时，只需检验一个幂（测试 06）。

对小于 3000 的每个素数，都与逐个列出候选数各次幂的结果比较过。

## 各语言说明

- 所有语言都建立同样的筛，并按 N 保存答案表。

## 优化解法

`1268_number_theory_optimized.cpp`. 保留只处理奇数的因子筛、原根的素因子检验与答案缓存。对 a,b<p<65536，a*b 在 32 位内。预先计算 floor(2^32/p)，取乘积再乘该值的高 32 位所得商最多小一，一次条件减法即可得到精确余数。反复模乘无需除法、浮点数或概率检验。输入输出使用 16 KiB 块，搜索条件和渐近工作量不变。

精确源代码 Accepted #11326994：0.015 s / 196 KB。2026-11-20 保存的 G++ 13.2 样本：时间排名 1/43，内存排名 2/43。教学源代码保留。

优化版本只筛选奇数，并单独处理质因数 2。遇到相同的模数时直接使用缓存的答案。

Python 3.12 x64（提交 11322010）的运行时间从 0.156 秒变为 0.125 秒，内存从 4400 KB 变为 2368 KB。

Rust 1.75 x64（提交 11322011）的运行时间从 0.031 秒变为 0.031 秒，内存从 1420 KB 变为 312 KB。

Go 1.14 x64（提交 11322012）的运行时间从 0.015 秒变为 0.031 秒，内存从 2420 KB 变为 1004 KB。

G++ 13.2 x64（提交 11326994）相较保留的基础版本：时间 0.031 → 0.015 秒；内存 692 → 196 KB。

Java 1.8（提交 11322014）的运行时间从 0.109 秒变为 0.078 秒，内存从 2928 KB 变为 920 KB。

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11322241 · Go 1.14 x64 №11322242 · Java 1.8 №11322243 · Python 3.12 x64 №11322244 · Rust 1.75 x64 №11322245.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1268_number_theory.cpp](1268_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 692 KB | 11322241 |
| [1268_number_theory.go](1268_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.015 s | 2420 KB | 11322242 |
| [1268_number_theory.java](1268_number_theory.java) | Java 1.8 | number_theory | O(L log log L + T · k log N) | AC | 0.109 s | 2928 KB | 11322243 |
| [1268_number_theory.py](1268_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.156 s | 4400 KB | 11322244 |
| [1268_number_theory.rs](1268_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 1420 KB | 11322245 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1268_number_theory_optimized.py](1268_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.125 s | 2368 KB | 11322010 |
| [1268_number_theory_optimized.rs](1268_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 312 KB | 11322011 |
| [1268_number_theory_optimized.go](1268_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 1004 KB | 11322012 |
| [1268_number_theory_optimized.cpp](1268_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.015 s | 196 KB | 11326994 |
| [1268_number_theory_optimized.java](1268_number_theory_optimized.java) | Java 1.8 | number_theory | O(L log log L + T · k log N) | AC | 0.078 s | 920 KB | 11322014 |

\* 带星号的版本仍有提升排名的空间。
