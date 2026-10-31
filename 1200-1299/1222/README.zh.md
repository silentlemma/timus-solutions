# 1222. 给定和的数的最大乘积

[Timus 1222](https://acm.timus.ru/problem.aspx?space=1&num=1222) · 难度 144 · math

原题为民间流传的题目，由 Leonid Volkov 提供，出自第七届乌拉尔国立大学大学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一群鹰总共有 `1 ≤ N ≤ 3000` 个头，这群鹰的智商等于各只鹰头数的乘积。求可能的
最大智商，也就是和为 `N` 的若干正整数的最大乘积。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`。

## 输出

最大的乘积。

## 样例

### 样例 1

输入：

```
5
```

输出：

```
6
```

## 解法

大于等于 4 的部分可以拆成 2 和剩余部分而不降低乘积，大于等于 5 的部分这样拆还会
增大乘积（`k > 4` 时 `2(k − 2) > k`），而 1 只会浪费一个头。所以最优拆分只含 2、
3 和 4，而 4 和 2 + 2 一样。三个 2 不如两个 3（`8 < 9`），所以 2 最多两个。于是：
`N` 能被 3 整除时全用 3；余数为 2 时再加一个 2；余数为 1 时用两个 2（或一个 4）
代替一个 3。`N` 不超过 3 时一只鹰最好。乘积最多 478 位。反复乘以 3 共需 `O(N²)`
次数字运算。

注意事项：

- `N = 1` 得 1，`N = 4` 得 4；
- 余数 1 不能作为因子 1 留下；
- 答案远远超出 64 位。

答案已对每个不超过 59 的 `N` 用枚举所有拆分的方法验证，并在所有测试上与另一份
独立解答比对。

## 优化解法

优化的 C++ 解法对一个固定的、有 1000 位十进制数字的全局数组做乘法，而不是用随乘
积增长的 `std::vector`，因此程序不需要动态内存；当 `N ≤ 3000` 时乘积至多
478 位：{1222_math_optimized.cpp}。

优化的 Java 解法用 `System.in.read` 逐字节读入唯一的数，而不是创建 `Scanner`，这
样 JVM 不必加载扫描器及其正则表达式；`BigInteger` 求幂的部分不变：
{1222_math_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1222_math_optimized.cpp`: 时间降低 +0.00%; 内存降低 +45.83%; 基础版本: `1222_math.cpp`.

- `1222_math_optimized.java`: 时间降低 -34.41%; 内存降低 +71.66%; 基础版本: `1222_math.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1222_math.go](1222_math.go).
- [1222_math.rs](1222_math.rs).

- Python 用自带的整数，Go 用 `math/big`，Java 用 `BigInteger`；C++ 和 Rust 把
  十进制数字数组反复乘以 3。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math.cpp](1222_math.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.015 s | 192 KB | 11283695 |
| [1222_math.go](1222_math.go) | Go 1.14 x64 | math | O(N²) | AC | 0.015 s | 1184 KB | 11283696 |
| [1222_math.java](1222_math.java) | Java 1.8 | math | O(N²) | AC | 0.093 s | 1708 KB | 11283698 |
| [1222_math.py](1222_math.py) | Python 3.12 x64 | math | O(N²) | AC | 0.078 s | 396 KB | 11283697 |
| [1222_math.rs](1222_math.rs) | Rust 1.75 x64 | math | O(N²) | AC | 0.031 s | 208 KB | 11283699 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math_optimized.cpp](1222_math_optimized.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.001 s | 104 KB | 11304484 |
| [1222_math_optimized.java](1222_math_optimized.java) \* | Java 1.8 | math | O(N²) | AC | 0.125 s | 484 KB | 11304486 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
