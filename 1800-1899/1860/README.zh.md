# 1860. 斐波阶乘

[Timus 1860](https://acm.timus.ru/problem.aspx?space=1&num=1860) · 难度 469 · number_theory

原题作者 Denis Dublennykh（创意来自 Grigoriy Nazarov），出自 2011 年 8 月彼得罗扎沃茨克夏季集训的 Ural SU Team.GOV Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

设 F₀ = F₁ = 1，Fᵢ = i·Fᵢ₋₁·Fᵢ₋₂。求 Fₙ 的约数个数模 10⁹ + 7。

## 输入

n（1 ≤ n ≤ 10⁶）。

## 输出

Fₙ 的约数个数模 10⁹ + 7。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
3
```

输出：

```
4
```

## 解法

每一步乘上一次 i，并重复前两个乘积，所以因子 k 在 Fₙ 中恰好出现 fib(n − k + 1) 次，其中 fib(1) = fib(2) = 1：它在 F_k 中出现一次，在 F_{k+1} 中一次，在 F_{k+2} 中两次，依此按斐波那契规律。因此 Fₙ = Π k^fib(n−k+1)，k = 1 … n。

约数个数等于对所有质数 p 的 Π (e_p + 1)，其中 e_p 是 p 在 Fₙ 中的指数。数 k 贡献 v_p(k) 乘以它的权重 fib(n − k + 1)，而 v_p(k) 数的是 p、p²、p³ … 中有多少个整除 k，所以 e_p 就是 p、p² 等的所有倍数的权重之和。
只需要 e_p 模 10⁹ + 7 的值，所以权重也保持取模。遍历每个质数幂的倍数共约 n·ln ln n 步；Python 版本用一次切片对每个等差数列求和。`O(n log log n)`。

在样例中 F₃ = 3·F₂·F₁ = 3·2·1 = 6，它的约数是 1、2、3 和 6。

注意事项：

- 指数非常大，但答案只需要它们模 10⁹ + 7；
- 质数幂超过 n 时必须在溢出之前停止循环；
- Python 版本在 PyPy 上运行。

对 n 不超过 14，答案与 Fₙ 的直接分解一致；直到 10⁶，与一个独立的已通过实现一致。

## 优化解法

`1860_number_theory_optimized.java`. 保留模10^9+7 的素因子指数约数公式。Fibonacci 余数由 long[] 改成 int[]，两余数未约减之和也小于2^31。直接用 fib[n-multiple+1] 取权，去掉独立 long[] weight 副本。累计指数和答案乘积仍为 long，每个素数幂遍历后约减指数。筛素数和累加幂贡献不变。时间 O(n log log n)，空间 O(n)，每下标字节显著更少。输入一个数字字节记号，n=1 仍得一个约数。

与 `1860_number_theory.java` 相比：时间 0.187 s → 0.125 s；内存 18 412 KB → 8 368 KB。

新 C++、Go、Rust 保留质数幂指数求和，只存一个 uint32 Fibonacci 数组，权重 k 直接取 fib[n−k+1]，不再复制64位权重。两余数和小于2·MOD，可条件减法。奇数位筛约 n/16 字节，单独处理质数2。每质数累计至多 n 项，未取模 uint64 和小于 n·MOD≤10¹⁵，可最后取模；最终乘法也不溢出。乘质数前检查 power>n/p。时间 O(n log log n)、空间 O(n)，权重约4n字节，替代两个8n数组。保留基础版；Java/Python 复用符合标准的基础版。

已通过评测的基础实现 [1860_number_theory.java](1860_number_theory.java), [1860_number_theory.py](1860_number_theory.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1860_number_theory_optimized.py`. 模 Fibonacci 权重保存在一个紧凑无符号整数数组中，原地反转，避免第二份权重序列。此 Accepted 使用 PyPy 3.10，而非 CPython。 独立程序先刷新两个输出流，再调用 os._exit(0)，在完整答案写出后跳过解释器清理。这只改变进程结束方式，不改变数学算法；简单版本仍保留。

Accepted #11328686 (PyPy 3.10 x64): **0.218 s / 14116 KB**. 历史对照: `1860_number_theory.py` (PyPy 3.10 x64) — 0.171 s / 34140 KB (#11325600).

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。保留教学算法。复查的基础代码行使用其自身新精确源代码 Accepted 的指标与 ID；这些检查不算优化。

`1860_number_theory_optimized.java`：在该可比样本中，时间名次 3/16，内存名次 5/16。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1860_number_theory.cpp](1860_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log log n) | AC | 0.031 s | 15492 KB | 11325590 |
| [1860_number_theory.go](1860_number_theory.go) | Go 1.14 x64 | number_theory | O(n log log n) | AC | 0.046 s | 18860 KB | 11290853 |
| [1860_number_theory.java](1860_number_theory.java) | Java 1.8 | number_theory | O(n log log n) | AC | 0.187 s | 18412 KB | 11325560 |
| [1860_number_theory.py](1860_number_theory.py) | PyPy 3.10 x64 | number_theory | O(n log log n) | AC | 0.171 s | 34140 KB | 11325600 |
| [1860_number_theory.rs](1860_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log log n) | AC | 0.046 s | 16684 KB | 11325614 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1860_number_theory_optimized.cpp](1860_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(n log log n) | AC | 0.031 s | 3700 KB | 11315295 |
| [1860_number_theory_optimized.go](1860_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(n log log n) | AC | 0.031 s | 4800 KB | 11315297 |
| [1860_number_theory_optimized.rs](1860_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(n log log n) | AC | 0.046 s | 3888 KB | 11315298 |
| [1860_number_theory_optimized.java](1860_number_theory_optimized.java) | Java 1.8 | number_theory | O(n log log n) | AC | 0.125 s | 8368 KB | 11325040 |
| [1860_number_theory_optimized.py](1860_number_theory_optimized.py) | PyPy 3.10 x64 | number_theory | O(n log log n) | AC | 0.218 s | 14116 KB | 11328686 |
