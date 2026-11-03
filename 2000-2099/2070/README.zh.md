# 2070. 因数个数为质数的质数幂

[Timus 2070](https://acm.timus.ru/problem.aspx?space=1&num=2070) · 难度 235 · number_theory

原题作者 Alexey Danilyuk，出自 2015 年乌拉尔地区团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个人认为整数是质数时有趣，另一个人认为整数的正因数个数是质数时有趣。若两人看法一致（都认为有趣或都认为无趣），这个数就令人满意。统计 [L; R] 中令人满意的整数个数。时间限制 2 秒，内存限制 64 MB。

## 输入

L 和 R（2 ≤ L ≤ R ≤ 10¹²）。

## 输出

[L; R] 中令人满意的整数个数。

## 评测方式

精确比较完整输出，包括空格和换行。

## 样例

### 样例 1

输入：

```
3 7
```

输出：

```
4
```

### 样例 2

输入：

```
2 2
```

输出：

```
1
```

### 样例 3

输入：

```
77 1010
```

输出：

```
924
```

## 解法

质数有 2 个因数，而 2 是质数，所以每个质数两人都认为有趣。合数只要因数个数不是质数就令人满意。对 x = p₁^a₁ · … · pₛ^aₛ，因数个数为 (a₁ + 1) · … · (aₛ + 1)，乘积是质数只可能在只有一个因子时。所以不满意的数恰好是质数的幂 p^k，其中 k ≥ 2 且 k + 1 为质数，答案是 R − L + 1 减去它们在 [L; R] 中的个数。

由于 k ≥ 2 时 p^k ≤ 10¹²，这样的 p 都不超过 10⁶。筛出 10⁶ 以内的质数，对每个满足 p² ≤ R 的质数 p，依次枚举 p²、p³、… 直到 R，统计不小于 L 且指数加一为质数的那些。大于 10⁴ 的质数只有平方一项，所以枚举很短；主要耗时在筛法，O(N log log N)，N = 10⁶。

第一个样例中 4 = 2² 有 3 个因数，是 3 … 7 中唯一不满意的数，答案为 4。

## 优化解法

将素数平方与其他合格偶次幂分开。用以不同整数商为状态的素数计数 DP，计算所需平方根以内的素数个数。只有更高次幂需要显式筛，其素数底数不超过四次根。按基础数论证明统计合格指数，用前缀计数相减得到区间答案。整数修正根值，避免浮点边界错误。

R 为区间右端点，M=floor(sqrt(R))，P 为更高次幂所需的小素数数目。统计的是不合格数，应从区间长度减去其数量。

- `2070_number_theory_dp.cpp`: 0.015 s / 172 KB; 基础版 `2070_number_theory.cpp`: 0.015 s / 284 KB; 相对基础版的变化: 时间 -0.0%, 内存 -39.4%.
- `2070_number_theory_dp.go`: 0.031 s / 1116 KB; 基础版 `2070_number_theory.go`: 0.031 s / 2136 KB; 相对基础版的变化: 时间 -0.0%, 内存 -47.8%.
- `2070_number_theory_dp.java`: 0.125 s / 492 KB; 基础版 `2070_number_theory.java`: 0.140 s / 2584 KB; 相对基础版的变化: 时间 -10.7%, 内存 -81.0%.
- `2070_number_theory_dp.py`: 0.093 s / 940 KB; 基础版 `2070_number_theory.py`: 0.109 s / 2772 KB; 相对基础版的变化: 时间 -14.7%, 内存 -66.1%.
- `2070_number_theory_dp.rs`: 0.046 s / 228 KB; 基础版 `2070_number_theory.rs`: 0.046 s / 1200 KB; 相对基础版的变化: 时间 -0.0%, 内存 -81.0%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `2070_number_theory.cpp`; 覆盖实现 `2070_number_theory.cpp`; 时间/内存名次 1/1, 其他作者记录 76/76.

- Go: 优先教学基础版 `2070_number_theory.go`; 覆盖实现 `2070_number_theory.go`; 时间/内存名次 1/1, 其他作者记录 1/1.

- Java: 优先教学基础版 `2070_number_theory.java`; 覆盖实现 `2070_number_theory.java`; 时间/内存名次 1/1, 其他作者记录 3/3.

- Python/PyPy: 优先教学基础版 `2070_number_theory.py`; 覆盖实现 `2070_number_theory.py`; 时间/内存名次 1/1, 其他作者记录 13/13.

- Rust: 优先教学基础版 `2070_number_theory.rs`; 覆盖实现 `2070_number_theory.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2070_number_theory.cpp](2070_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log log N) | AC | 0.015 s | 284 KB | 11309222 |
| [2070_number_theory.go](2070_number_theory.go) | Go 1.14 x64 | number_theory | O(N log log N) | AC | 0.031 s | 2136 KB | 11294446 |
| [2070_number_theory.java](2070_number_theory.java) | Java 1.8 | number_theory | O(N log log N) | AC | 0.140 s | 2584 KB | 11309223 |
| [2070_number_theory.py](2070_number_theory.py) | Python 3.12 x64 | number_theory | O(N log log N) | AC | 0.109 s | 2772 KB | 11309224 |
| [2070_number_theory.rs](2070_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log log N) | AC | 0.046 s | 1200 KB | 11309225 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2070_number_theory_dp.cpp](2070_number_theory_dp.cpp) | G++ 13.2 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.015 s | 172 KB | 11308159 |
| [2070_number_theory_dp.go](2070_number_theory_dp.go) | Go 1.14 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.031 s | 1116 KB | 11308162 |
| [2070_number_theory_dp.java](2070_number_theory_dp.java) | Java 1.8 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.125 s | 492 KB | 11308164 |
| [2070_number_theory_dp.py](2070_number_theory_dp.py) | Python 3.12 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.093 s | 940 KB | 11308156 |
| [2070_number_theory_dp.rs](2070_number_theory_dp.rs) | Rust 1.75 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.046 s | 228 KB | 11308166 |
