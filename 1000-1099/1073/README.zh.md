# 1073. 总价恰为 N 的最少正方形地块数

[Timus 1073](https://acm.timus.ru/problem.aspx?space=1&num=1073) · 难度 140 · number_theory

原题作者 Stanislav Vasiliev，出自 2001 年 2 月 Ural State University Personal Contest Online（Students Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

边长为 `a` 的正方形地块价格为 `a²`。要恰好花掉 `N`（`1 ≤ N ≤ 60000`）并买尽可能少的地块，也就是把 `N`
写成个数最少的正整数平方之和。输出需要多少块地。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`。

## 输出

最少的平方数个数。

## 评测方式

按记号逐个比较输出；多余的空白不影响结果。

## 样例

### 样例 1

输入：

```
344
```

输出：

```
3
```

## 题解

答案不会超过 4：由拉格朗日四平方和定理，每个正整数都是四个平方数之和。其余情况很容易区分。

- 若 `N` 是完全平方数，答案为 1。
- 若对某个 `1 ≤ a < √N`，`N − a²` 是完全平方数，答案为 2；最多检查 244 次。
- 若 `N = 4^a (8b + 7)`，答案为 4：由勒让德三平方和定理，恰好是这些数不能表示为三个平方数之和。能被 4
  整除时就一直除以 4，再看除以 8 的余数。
- 其他情况答案为 3。

`O(√N)`。

对所有金额做动态规划 `best[v] = 1 + min best[v − a²]`，复杂度 `O(N√N)`，约 1000 万步，在编译型语言中也能
通过，但在 Python 中很慢，而上面的定理让它变得不必要。

注意事项：

- 因子 `4^a` 很重要：28 = 4 · 7 也需要四个平方数，所以只检查 `N mod 8 = 7` 是不够的；
- 浮点数平方根要先取整再平方回去，这样像 `6.9999…` 这样的结果不会漏掉完全平方数。

公式与动态规划的结果对 60000 以内的每个 `N` 都做了核对。

## 优化解法

优化的 Java 解法用 `System.in.read` 逐字节读入唯一的数，而不是创建 `Scanner`，这
样 JVM 不必加载扫描器及其正则表达式；判断过程不变：
{1073_number_theory_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1073_number_theory_optimized.java`: 时间降低 -14.68%; 内存降低 +77.94%; 基础版本: `1073_number_theory.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1073_number_theory.cpp](1073_number_theory.cpp).
- [1073_number_theory.go](1073_number_theory.go).
- [1073_number_theory.rs](1073_number_theory.rs).

- Python 使用精确的 `math.isqrt`；其他语言对浮点平方根取整，对这么小的数是精确的。

## 题解代码

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1073_number_theory.cpp](1073_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(√N) | AC | 0.015 s | 132 KB | 11278937 |
| [1073_number_theory.go](1073_number_theory.go) | Go 1.14 x64 | number_theory | O(√N) | AC | 0.031 s | 1076 KB | 11278938 |
| [1073_number_theory.java](1073_number_theory.java) | Java 1.8 | number_theory | O(√N) | AC | 0.109 s | 1596 KB | 11278942 |
| [1073_number_theory.py](1073_number_theory.py) | Python 3.12 x64 | number_theory | O(√N) | AC | 0.078 s | 440 KB | 11278940 |
| [1073_number_theory.rs](1073_number_theory.rs) | Rust 1.75 x64 | number_theory | O(√N) | AC | 0.015 s | 228 KB | 11278944 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1073_number_theory_optimized.java](1073_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(√N) | AC | 0.125 s | 352 KB | 11304462 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
