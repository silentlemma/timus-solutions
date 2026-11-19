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

## 评测方式

仓库测试比较完整输出文本，仅忽略末尾空白。应保留有意义的空格、换行、大小写及标点。

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

`1206_combinatorics_optimized.py`. 保留精确公式 36*55^(K-1) 及 Python 任意精度整数。基础版本的 ** 和这里的 pow 都已使用整数幂，不声称采用新的计数算法。按朴素位运算并计入十进制转换，保守上界为 O(K²) 时间、O(K) 位答案存储。新实现读取单个输入记号，去掉函数包装和常规清理。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1206_combinatorics.py` 相比：时间 0.109 s → 0.14 s；内存 416 KB → 252 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1206_combinatorics_optimized.py`：在该可比样本中，时间名次 65/76，内存名次 2/76。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

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
| [1206_combinatorics_optimized.py](1206_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(K²) | AC | 0.14 s | 252 KB | 11324911 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
