# 1206. 数字和可以相加的数对

[Timus 1206](https://acm.timus.ru/problem.aspx?space=1&num=1206) · 难度 124 · combinatorics

原题作者 Leonid Volkov，出自 2002 年 3 月乌拉尔国立大学团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

设 `S(N)` 为 `N` 的各位数字之和。对 `2 ≤ K ≤ 50`，统计满足
`S(A + B) = S(A) + S(B)` 的无前导零 `K` 位数有序对 `A`、`B` 的个数。

时间限制：1 秒。内存限制：64 MB。

## 输入

`K`。

## 输出

数对的个数。

## 样例

### 样例 1

输入：

```
2
```

输出：

```
1980
```

## 解法

加法中的每次进位都会把某一位上的 10 变成下一位上的 1，使数字和减少 9。所以等式
成立当且仅当没有任何进位，也就是每一位上两个数字之和不超过 9。此时各位互相独立。
最高位上两个数字都在 1 到 9 之间，共有 `8 + 7 + … + 1 = 36` 对；其余 `K − 1`
位上数字在 0 到 9 之间，每位有 `10 + 9 + … + 1 = 55` 对。答案是 `36 · 55^(K−1)`，
最多 87 位。用竖式乘法为 `O(K²)`。

注意事项：

- 答案在 `K = 12` 时就超出了 64 位；
- 最高位不能为 0，所以它的对数和其他位不同。

公式已在 `K = 2` 和 `K = 3` 时用枚举全部数对验证，并且每个 `K` 都与另一份独立解答
比对过。

## 优化解法

优化的 C++ 解法同样把十进制数字乘以 55，但用的是栈上 100 个元素的固定数组，而不
是不断增长的 `std::vector`：因为 `K ≤ 50`，答案 `36 · 55^(K−1)` 小于 `100^K`，最
多 100 位（实际最多 87 位）。不用 `<vector>`，程序里就完全没有容器代码：
{1206_combinatorics_optimized.cpp}。

优化的 Java 解法直接从 `System.in` 逐字节读入 `K`，而不是创建 `Scanner`，后者的
正则表达式和区域设置数据比求幂本身还费资源；答案仍用 `BigInteger` 计算：
{1206_combinatorics_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1206_combinatorics_optimized.cpp`: 时间降低 +0.00%; 内存降低 +46.81%; 基础版本: `1206_combinatorics.cpp`.

- `1206_combinatorics_optimized.java`: 时间降低 +10.71%; 内存降低 +74.37%; 基础版本: `1206_combinatorics.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1206_combinatorics.rs](1206_combinatorics.rs).

- Python 用自带的整数，Go 用 `math/big`，Java 用 `BigInteger`；C++ 和 Rust 把
  十进制数字数组乘以 55 共 `K − 1` 次。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics.cpp](1206_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 188 KB | 11283595 |
| [1206_combinatorics.go](1206_combinatorics.go) | Go 1.14 x64 | combinatorics | O(K²) | AC | 0.031 s | 1200 KB | 11283596 |
| [1206_combinatorics.java](1206_combinatorics.java) | Java 1.8 | combinatorics | O(K²) | AC | 0.140 s | 1748 KB | 11283601 |
| [1206_combinatorics.py](1206_combinatorics.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.109 s | 416 KB | 11283600 |
| [1206_combinatorics.rs](1206_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(K²) | AC | 0.015 s | 212 KB | 11283602 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics_optimized.cpp](1206_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 100 KB | 11304421 |
| [1206_combinatorics_optimized.java](1206_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O(K²) | AC | 0.125 s | 448 KB | 11304422 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
