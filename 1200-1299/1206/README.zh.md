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
4
```

输出：

```
5989500
```

## 解法

加法中的每次进位都会把某一位上的 10 变成下一位上的 1，使数字和减少 9。所以等式
成立当且仅当没有任何进位，也就是每一位上两个数字之和不超过 9。此时各位互相独立。
最高位上两个数字都在 1 到 9 之间，共有 `8 + 7 + … + 1 = 36` 对；其余 `K − 1`
位上数字在 0 到 9 之间，每位有 `10 + 9 + … + 1 = 55` 对。答案是 `36 · 55^(K−1)`，
最多 87 位。用竖式乘法为 `O(K²)`。

答案需要 O(K) 十进制位或相差常数倍的二进制位。基础 C++/Rust 保留动态十进制向量，Rust 另建 O(K) 输出 String；Go/Java/Python 保存任意精度整数及十进制输出，活值/输出 O(K)，另计算术工作区和输入缓冲。普通算术 O(K²) 是保守计算/转换模型，不声称内置幂做 K 次重复乘法。优化 Java 分配恰好 2K 数位及 O(K) 答案字节；优化 C++ 为 K ≤ 50 固定预留栈上 100 项。36·55^(K−1) < 100^K 证明至多 2K 位，K=2、K=3 时取等。

注意事项：

- 答案在 `K = 12` 时就超出了 64 位；
- 最高位不能为 0，所以它的对数和其他位不同。

公式已在 `K = 2` 和 `K = 3` 时用枚举全部数对验证，并且每个 `K` 都与另一份独立解答
比对过。

## 优化解法

`1206_combinatorics_optimized.java`. 保留无进位计数公式 36*55^(K-1)。K<=50 时显式保存最多 100 个十进制数位，运行时乘 55 共 K-1 次，再直接输出字节。只改变算术表示，不改计数论证，也不保存预计算答案。保守上界为 O(K²) 数位操作和 O(K) 空间，避免 BigInteger 初始化；保留简单 BigInteger 公式。

历史精确源码 Java 1.8 Accepted #11327341 为 0.109 s / 308 KB；2026-11-20 保存比较为时间 14/141、内存 1/141。低于 1024 KB 按统一时间标准通过，无独立第一名或标记。较早 #11304422 为独立历史指标对 0.125 s / 448 KB。本次仅把容量注释从少于 2K 改成至多 2K，其他可执行文本相同。

- `1206_combinatorics_optimized.java`: 0.109 s / 308 KB; 保留教学基础版 `1206_combinatorics.java`: 0.14 s / 1748 KB.

`1206_combinatorics_optimized.py` 选定精确源码 CPython 3.12 Accepted #11327017 为 0.078 s / 612 KB；2026-11-20 保存排名为时间 2/76、内存 60/76。低于 1024 KB 只凭时间通过。相对当前基础 #11283600 的 0.109 s / 416 KB，时间减少 28.44%，内存增加 47.12%，两项均无 30% 改善。历史 PyPy 3.10 #11324911 是独立指标对 0.140 s / 252 KB，后文省内存比较指该运行，不是选定 CPython 行。

优化的 C++ 解法同样把十进制数字乘以 55，但用的是栈上 100 个元素的固定数组，而不
是不断增长的 `std::vector`：因为 `K ≤ 50`，答案 `36 · 55^(K−1)` 小于 `100^K`，最
多 100 位（实际最多 87 位）。不用 `<vector>`，程序里就完全没有容器代码：
{1206_combinatorics_optimized.cpp}。

### 实测改进

这些是成对 Accepted 运行的历史差异，不是普遍 30% 改进准入规则。基础源码保留；负降低比例表示开销增加，当前准入由统一排名政策决定。

- `1206_combinatorics_optimized.cpp`: 时间降低 +0.00%; 内存降低 +46.81%; 基础版本: `1206_combinatorics.cpp`.

`1206_combinatorics_optimized.py`. 保留精确公式 36*55^(K-1) 及 Python 任意精度整数。基础版本的 ** 和这里的 pow 都已使用整数幂，不声称采用新的计数算法。按朴素位运算并计入十进制转换，保守上界为 O(K²) 时间、O(K) 位答案存储。新实现读取单个输入记号，去掉函数包装和常规清理。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。历史 PyPy Accepted 显示省内存；选定当前 CPython Accepted 则用更多内存换取更低的记录时间。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1206_combinatorics.py` 相比：时间 0.109 s → 0.14 s；内存 416 KB → 252 KB。

## 各语言说明

采用统一[排名标准](../../RATING_CRITERIA.md)及源码绑定缓存。两份 C++、Go、Rust 和收据绑定的优化 Java/Python 通过数值标准。基础 Java/Python 未过，仍教学保留且不标星。低于 1024 KB 只计时间；1200 KB 的 Go 需两项，对精确版本两个对手比较。Rust 使用唯一对手参照。无独立第一名、30% 改进准入，也不以旧 PyPy 名次替代当前覆盖。

上述源码修订均已取得各自的 Accepted。解答表列出与最终源码对应的提交编号及同次运行的时间和内存；较早的观察对应此前的修订。所有有教学价值的简单实现均保留。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics.cpp](1206_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 188 KB | 11283595 |
| [1206_combinatorics.go](1206_combinatorics.go) | Go 1.14 x64 | combinatorics | O(K²) | AC | 0.031 s | 1200 KB | 11283596 |
| [1206_combinatorics.java](1206_combinatorics.java) | Java 1.8 | combinatorics | O(K²) | AC | 0.14 s | 1748 KB | 11283601 |
| [1206_combinatorics.py](1206_combinatorics.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.109 s | 416 KB | 11283600 |
| [1206_combinatorics.rs](1206_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(K²) | AC | 0.015 s | 212 KB | 11283602 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics_optimized.cpp](1206_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 100 KB | 11304421 |
| [1206_combinatorics_optimized.java](1206_combinatorics_optimized.java) | Java 1.8 | combinatorics | O(K²) time; O(K) space | AC | 0.078 s | 356 KB | 11331216 |
| [1206_combinatorics_optimized.py](1206_combinatorics_optimized.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.078 s | 612 KB | 11327017 |
