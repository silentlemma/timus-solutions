# 1204. 模两个素数之积的幂等元

[Timus 1204](https://acm.timus.ru/problem.aspx?space=1&num=1204) · 难度 230 · number_theory

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

## 评测方式

按词元比较输出，多余空白不影响结果。

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

## 优化解法

CRT 重构不变。Java 用基本类型素数数组、整数试除及有界 ASCII 输出，代替装箱对象和逐答案字符串。Python 使用素数乘积树：一次 GCD 检查整个块，再把非平凡因子向更小的块分流；叶子用普通试除完成。所有除数均精确验证，不依赖概率分解。必须计入乘积树构造和大整数 GCD、乘法的代价，不能把大数运算视为常数时间。

- `1204_number_theory_optimized.java`: 0.109 s / 484 KB; 基础版 `1204_number_theory.java`: 0.171 s / 1088 KB; 相对基础版的变化: 时间 -36.3%, 内存 -55.5%.
- `1204_number_theory_trees.py`: 0.093 s / 1084 KB; 基础版 `1204_number_theory.py`: 0.312 s / 1016 KB; 相对基础版的变化: 时间 -70.2%, 内存 +6.7%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1204_number_theory.cpp`; 覆盖实现 `1204_number_theory.cpp`; 时间/内存名次 3/7, 其他作者记录 75/75.

- Go: 优先教学基础版 `1204_number_theory.go`; 覆盖实现 `1204_number_theory.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1204_number_theory.java`; 覆盖实现 `1204_number_theory_optimized.java`; 时间/内存名次 2/1, 其他作者记录 3/3.

- Python/PyPy: 优先教学基础版 `1204_number_theory.py`; 覆盖实现 `1204_number_theory_trees.py`; 时间/内存名次 1/2, 其他作者记录 13/13.

- Rust: 优先教学基础版 `1204_number_theory.rs`; 覆盖实现 `1204_number_theory.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1204_number_theory.cpp](1204_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 228 KB | 11283581 |
| [1204_number_theory.go](1204_number_theory.go) | Go 1.14 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 1320 KB | 11283582 |
| [1204_number_theory.java](1204_number_theory.java) | Java 1.8 | number_theory | O(k·π(√n)) | AC | 0.171 s | 1088 KB | 11283585 |
| [1204_number_theory.py](1204_number_theory.py) | Python 3.12 x64 | number_theory | O(k·π(√n)) | AC | 0.312 s | 1016 KB | 11283583 |
| [1204_number_theory.rs](1204_number_theory.rs) | Rust 1.75 x64 | number_theory | O(k·π(√n)) | AC | 0.015 s | 268 KB | 11283586 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1204_number_theory_optimized.java](1204_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(K sqrt N) | AC | 0.109 s | 484 KB | 11309381 |
| [1204_number_theory_trees.py](1204_number_theory_trees.py) \* | Python 3.12 x64 | number_theory, trees | O(log P) bigint gcds per query | AC | 0.093 s | 1084 KB | 11309380 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
