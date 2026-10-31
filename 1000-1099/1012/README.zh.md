# 1012. 统计没有两个相邻零的 K 进制数（高精度版）

[Timus 1012](https://acm.timus.ru/problem.aspx?space=1&num=1012) · 难度 181 · dp

原题是[第 1009 题](../1009/README.zh.md)的加强版。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计 `K` 进制下的 `N` 位数（首位不为零）中，数字里没有两个连续零的个数。`2 ≤ K ≤ 10`，`N ≥ 2`，
`N + K ≤ 1800`。

时间限制：0.5 秒。内存限制：16 MB。

## 输入

`N` 和 `K`，各占一行。

## 输出

完整的个数。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
4
2
```

输出：

```
5
```

### 样例 2

输入：

```
3
10
```

输出：

```
891
```

## 题解

递推与[第 1009 题](../1009/README.zh.md)相同：按最后一位统计合法前缀，`zero` 以 `0` 结尾，`other`
以非零数字结尾：

- `zero' = other`；
- `other' = (zero + other) · (K - 1)`；

初值 `zero = 0`、`other = K - 1`，`N` 位之后答案为 `zero + other`。

变化的是规模：答案最多约 1 800 位十进制数字，因此需要高精度运算。只用到两种运算——
两个大数相加、大数乘小数——都与长度成线性。把大数存成以 `10^9` 为基的“数位”数组，低位在前：一位乘以
`K - 1` 再加进位不超过 64 位。共 `N` 步，每步 `O(L)`，`L` 为答案的段数：约 `1800 · 200` 次运算。

只保留当前两个值，内存为 `O(L)`；保存全部 `N` 个大数的表也放得下，但没有必要。

注意事项：

- 64 位整数大约在 20 位数字后溢出：简单版本的解法在这里是错的；
- 输出以 `10^9` 为基的各段时，除最高段外每段都要补前导零到 9 位。

## 优化解法

优化的 C++ 解法把 `zero` 和 `other` 存在两个静态数组中，每个有 201 段以 `10^9`
为基的数位；这已足够，因为答案小于 `K^N ≤ 10^N`，且 `N < 1800`。递推的一步在数位
上原地扫一遍完成：`zero` 的数位取 `other` 的数位，`other` 的数位变为
`(zero + other) · (K - 1)` 与进位之和对 `10^9` 取模，这个和本身小于
`18 · 10^9`，放得进 64 位。每一步都不再分配和扩展临时向量：
{1012_dp_optimized.cpp}。

优化的 Go 解法用两个固定大小、各有 201 段以 `10^9` 为基数位的数组代替
`math/big`；这已足够，因为答案小于 `K^N ≤ 10^N`，且 `N < 1800`。递推的一步在数位
上原地扫一遍完成，加法和乘以 `K - 1` 合并在一起：中间值小于 `18 · 10^9`，放得进
64 位。每一步都不再创建新的大整数，各段补零后通过带缓冲的输出打印：
{1012_dp_optimized.go}。

优化的 Java 解法用两个各有 201 段以 `10^9` 为基数位的 `long` 数组代替
`BigInteger`；这已足够，因为答案小于 `K^N ≤ 10^N`，且 `N < 1800`。递推的一步在数
位上原地扫一遍完成，加法和乘以 `K - 1` 合并在一起：中间值小于 `18 · 10^9`，放得
进 `long`。此外，两个数逐字节读取而不用 `Scanner`，各段手工补零：
{1012_dp_optimized.java}。

优化的 Rust 解法把 `zero` 和 `other` 存在两个固定大小的数组中，每个有 201 段以
`10^9` 为基的数位；这已足够，因为答案小于 `K^N ≤ 10^N`，且 `N < 1800`。递推的一
步在数位上原地扫一遍完成：中间值 `(zero + other) · (K - 1)` 加进位小于
`18 · 10^9`，放得进 `u64`。每次加法和乘法都不再分配新的向量，各段直接写入
`BufWriter`，不再拼成另一个字符串：{1012_dp_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1012_dp_optimized.cpp`: 时间降低 +0.00%; 内存降低 +58.21%; 基础版本: `1012_dp.cpp`.

- `1012_dp_optimized.go`: 时间降低 -106.67%; 内存降低 +48.83%; 基础版本: `1012_dp.go`.

- `1012_dp_optimized.java`: 时间降低 +25.60%; 内存降低 +89.02%; 基础版本: `1012_dp.java`.

- `1012_dp_optimized.rs`: 时间降低 +0.00%; 内存降低 +58.46%; 基础版本: `1012_dp.rs`.

## 各语言说明

- **Python**、**Go**（`math/big`）和 **Java**（`BigInteger`）提供大整数。
- **C++** 和 **Rust** 在以 `10^9` 为基的数位上实现这两种运算。

## 题解代码

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1012_dp.cpp](1012_dp.cpp) | G++ 13.2 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 268 KB | 11278066 |
| [1012_dp.go](1012_dp.go) | Go 1.14 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 2056 KB | 11278067 |
| [1012_dp.java](1012_dp.java) | Java 1.8 | dp | O(N·L), L = length of the answer | AC | 0.125 s | 3860 KB | 11278076 |
| [1012_dp.py](1012_dp.py) | Python 3.12 x64 | dp | O(N·L), L = length of the answer | AC | 0.062 s | 340 KB | 11278071 |
| [1012_dp.rs](1012_dp.rs) | Rust 1.75 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 520 KB | 11278084 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1012_dp_optimized.cpp](1012_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 112 KB | 11307305 |
| [1012_dp_optimized.go](1012_dp_optimized.go) \* | Go 1.14 x64 | dp | O(N·L), L = length of the answer | AC | 0.031 s | 1052 KB | 11307309 |
| [1012_dp_optimized.java](1012_dp_optimized.java) \* | Java 1.8 | dp | O(N·L), L = length of the answer | AC | 0.093 s | 424 KB | 11307307 |
| [1012_dp_optimized.rs](1012_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 216 KB | 11307310 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
