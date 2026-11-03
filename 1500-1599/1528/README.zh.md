# 1528. 数列

[Timus 1528](https://acm.timus.ru/problem.aspx?space=1&num=1528) · 难度 272 · math

原题作者 Dmitry Gozman，出自 2007 年 1 月彼得罗扎沃茨克冬季集训的 Dmitry Gozman Contest 1。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

f(1) = g(1) = 1，f(n) = 1 + f(1)g(1) + … + f(n − 1)g(n − 1)，
g(n) = 1 + 2g(1) + … + 2g(n − 1) − g(n − 1)²。对至多 5000 组数据
（1 ≤ n ≤ 10000，2 ≤ p ≤ 2·10⁹）输出 f(n) mod p。

时间限制：3 秒。内存限制：64 MB。

## 输入

每行一对 n 和 p，以 0 0 结束。

## 输出

每组数据的 f(n) mod p。

## 评测方式

精确比较完整输出，包括空格和换行。

## 样例

### 样例 1

输入:

```
1 2
2 11
0 0
```

输出:

```
1
2
```

## 解法

两个数列都有闭式。若对 i < n 有 g(i) = i，则 g(n) = 1 + (n − 1)n − (n − 1)² = n。于
是 f(n) − f(n − 1) = f(n − 1)·(n − 1)，即 f(n) = n·f(n − 1) = n!。所以每组数据求的是
n! mod p。当 n ≥ p 时 p 本身就是一个因子，答案为 0。否则一路乘到 n 并随时取模；乘积小
于 2·10¹³，在 64 位范围内。所有数据合计至多 5·10⁷ 次乘法，编译型语言很快（每组 O(n)）。Python 中
朴素循环约需 6 秒，所以 Python 解法把每个 100 的倍数的阶乘精确地存为大整数，对其中一
个取模，再乘上至多 99 个因子：每组 O(n log n) 次位运算。

注意事项：

- 公式看起来复杂，其实 g(n) = n、f(n) = n!（所有测试）；
- n ≥ p 时答案直接为 0（测试 02、gen3）；
- p 可达 2·10⁹，乘积需要 64 位（测试 03、gen1）；
- 略大于 n 的质数 p 是很好的检验：由威尔逊定理 (p − 1)! ≡ −1（测试 05）。

## 优化解法

仍归约为给定模数下的阶乘。原生实现先乘相邻因子再取余，题目界限保证乘积不溢出有符号 64 位；不假设模数为素数或存在模逆。Python 计算精确的稀疏阶乘检查点及短块乘积，利用内建大整数乘法，仅对相同参数复用尾积。这些乘积按输入界限计算，并非存储答案常量。两者都沿用简单阶乘递推的正确性。

- `1528_math_optimized.cpp`: 0.203 s / 112 KB; 基础版 `1528_math.cpp`: 0.328 s / 132 KB; 相对基础版的变化: 时间 -38.1%, 内存 -15.2%.
- `1528_math_optimized.go`: 0.218 s / 916 KB; 基础版 `1528_math.go`: 0.343 s / 1224 KB; 相对基础版的变化: 时间 -36.4%, 内存 -25.2%.
- `1528_math_optimized.java`: 0.375 s / 840 KB; 基础版 `1528_math.java`: 0.609 s / 904 KB; 相对基础版的变化: 时间 -38.4%, 内存 -7.1%.
- `1528_math_optimized.py`: 0.359 s / 1388 KB; 基础版 `1528_math.py`: 0.359 s / 17900 KB; 相对基础版的变化: 时间 -0.0%, 内存 -92.2%.
- `1528_math_optimized.rs`: 0.156 s / 444 KB; 基础版 `1528_math.rs`: 0.250 s / 520 KB; 相对基础版的变化: 时间 -37.6%, 内存 -14.6%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1528_math.cpp`; 覆盖实现 `1528_math_optimized.cpp`; 时间/内存名次 3/1, 其他作者记录 58/58.

- Go: 优先教学基础版 `1528_math.go`; 覆盖实现 `1528_math.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1528_math.java`; 覆盖实现 `1528_math_optimized.java`; 时间/内存名次 1/1, 其他作者记录 4/4.

- Python/PyPy: 优先教学基础版 `1528_math.py`; 覆盖实现 `1528_math_optimized.py`; 时间/内存名次 3/1, 其他作者记录 5/5.

- Rust: 优先教学基础版 `1528_math.rs`; 覆盖实现 `1528_math.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1528_math.cpp](1528_math.cpp) | G++ 13.2 x64 | math | O(n) per case | AC | 0.328 s | 132 KB | 11287420 |
| [1528_math.go](1528_math.go) | Go 1.14 x64 | math | O(n) per case | AC | 0.343 s | 1224 KB | 11287421 |
| [1528_math.java](1528_math.java) | Java 1.8 | math | O(n) per case | AC | 0.609 s | 904 KB | 11287423 |
| [1528_math.py](1528_math.py) | Python 3.12 x64 | math | O(n log n) bit operations per case | AC | 0.359 s | 17900 KB | 11287422 |
| [1528_math.rs](1528_math.rs) | Rust 1.75 x64 | math | O(n) per case | AC | 0.250 s | 520 KB | 11287424 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1528_math_optimized.cpp](1528_math_optimized.cpp) | G++ 13.2 x64 | math | O(sum N) | AC | 0.203 s | 112 KB | 11309294 |
| [1528_math_optimized.go](1528_math_optimized.go) | Go 1.14 x64 | math | O(sum N) | AC | 0.218 s | 916 KB | 11309296 |
| [1528_math_optimized.java](1528_math_optimized.java) | Java 1.8 | math | O(sum N) | AC | 0.375 s | 840 KB | 11309295 |
| [1528_math_optimized.py](1528_math_optimized.py) \* | Python 3.12 x64 | math | O(N) product construction + bigint query work | AC | 0.359 s | 1388 KB | 11309298 |
| [1528_math_optimized.rs](1528_math_optimized.rs) | Rust 1.75 x64 | math | O(sum N) | AC | 0.156 s | 444 KB | 11309297 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
