# 1295. 胡思乱想

[Timus 1295](https://acm.timus.ru/problem.aspx?space=1&num=1295) · 难度 151 · number_theory

原题作者 Den Raskovalov，出自 2004 年 3 月 13 日第九届中学生公开团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

当 1 ≤ n ≤ 300 000 时，十进制数 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ 末尾有几个零？

时间限制：0.5 秒。内存限制：64 MB。

## 输入

数 n。

## 输出

末尾零的个数。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
1
```

输出：

```
1
```

### 样例 2

输入：

```
3
```

输出：

```
2
```

## 解法

n 最大时这个和超过 180 000 位，但末尾零的个数受其中 2 的幂次限制。设 S = 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ。

- n = 1：S = 10，一个零。
- n 为偶数：1ⁿ + 3ⁿ ≡ 1 + 1 = 2 (mod 4)，而 2ⁿ、4ⁿ 是 4 的倍数，所以 S 能被 2 整除但不能被 4
  整除。
- n 为奇数且 n ≥ 3：3ⁿ ≡ 3 (mod 8)，所以 1ⁿ + 3ⁿ ≡ 4 (mod 8)，而 2ⁿ 和 4ⁿ 是 8 的倍数；S 能被
  4 整除但不能被 8 整除。

因此 S 末尾不会有三个零，一切由 S mod 100 决定：为 0 时两个零，末位为 0 时一个零，否则没有。
四个幂模 100 的值用快速幂求出。`O(log n)`。

实际上答案只取决于 n mod 20：n 被 4 整除时为 0，n 模 4 余 3 或模 20 余 5 时为 2，其余为 1。
解法直接计算，而不依赖这张表。

注意事项：

- n 模 4 余 1 时通常只有一个零，但 n = 5、25、… 有两个（测试 05 和 06）；
- 完整的和可以用高精度构造，但完全没有必要：只有最后两位重要。

对 3000 以内的每个 n，结果都与高精度精确和比较过。

## 优化解法

优化的 Java 解法从由 `System.in` 填充的 4 KB 缓冲区中手工解析 `n`，而不是创建
`Scanner`，这样 JVM 不必加载扫描器及其正则表达式；模 100 的幂运算不变：
{1295_number_theory_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1295_number_theory_optimized.java`: 时间降低 +12.80%; 内存降低 +79.75%; 基础版本: `1295_number_theory.java`.

`1295_number_theory_optimized.py`. 保留模 100 判断末尾零数的论证，直接计算 1+pow(2,n,100)+pow(3,n,100)+pow(4,n,100)，不用四个底数的生成器。模幂不构造巨大整数。已证明至多两个末尾零，因此余零对应二，可被十整除对应一，否则零。时间 O(log n) 次有界模运算，状态 O(1)。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1295_number_theory.py` 相比：时间 0.093 s → 0.125 s；内存 464 KB → 200 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1295_number_theory_optimized.py`：在该可比样本中，时间名次 37/57，内存名次 1/57。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory.cpp](1295_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log n) | AC | 0.015 s | 128 KB | 11284634 |
| [1295_number_theory.go](1295_number_theory.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 1080 KB | 11284638 |
| [1295_number_theory.java](1295_number_theory.java) | Java 1.8 | number_theory | O(log n) | AC | 0.125 s | 1600 KB | 11284648 |
| [1295_number_theory.py](1295_number_theory.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.093 s | 464 KB | 11284644 |
| [1295_number_theory.rs](1295_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log n) | AC | 0.046 s | 240 KB | 11284651 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory_optimized.java](1295_number_theory_optimized.java) | Java 1.8 | number_theory | O(log n) | AC | 0.109 s | 324 KB | 11305839 |
| [1295_number_theory_optimized.py](1295_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(log n) | AC | 0.125 s | 200 KB | 11325070 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
