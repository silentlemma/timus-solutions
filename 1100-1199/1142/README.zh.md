# 1142. 统计 N 个对象允许并列的排序方式数

[Timus 1142](https://acm.timus.ru/problem.aspx?space=1&num=1142) · 难度 155 · combinatorics

原题来自 Timus，未注明作者和出处。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

`N` 个可比较的对象中任意两个之间满足 `a = b`、`a < b`、`b < a` 之一。
统计在这种意义下（允许相等）排列 `N` 个对象的不同方式数：三个对象有 13
种，从 `a = b = c` 到 `c < b < a`。对若干个 2 到 10 之间的 `N` 作答；输入以
`-1` 结束。

时间限制：1 秒。内存限制：64 MB。

## 输入

若干个 `N`，每行一个，最后是 `-1`。

## 输出

每个 `N` 对应的数目，每行一个。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
2
3
-1
```

输出：

```
3
13
```

## 解法

允许并列的排序就是一列由相等对象组成的组，各组严格递增。看第一组：它是
任意一个含 `k` 个对象的非空集合，有 `C(n, k)` 种选法，剩下的 `n − k` 个对象
自己构成一个允许并列的排序。所以令 `a(0) = 1`，

`a(n) = Σ_{k=1..n} C(n, k)·a(n − k)`。

这就是有序贝尔数（Fubini 数）1, 1, 3, 13, 75, 541, …；需要的最大值
`a(10) = 102247563` 在 32 位范围内。用帕斯卡三角形一次建好表，每个询问只需
查表。建表 `O(10²)`。

注意事项：

- 输入没有给出个数，要读到 `-1` 为止；
- 同一个 `N` 可能被询问多次。

这些值已与独立的公式 `a(n) = Σ k!·S(n, k)`（第二类斯特林数）比对，`n ≤ 6`
时还与列举全部排序的结果比对。

## 优化解法

`1142_combinatorics_optimized.go`. 递推及完整 11×11 Pascal 矩阵不变。预计算 L=10 的有序划分数，流式处理 Q 个查询直到负数或 EOF。本 Go 版只改输入输出开销，不改组合算法或表存储。 以 Go 1.14 syscall.Read/Write 使用有界 256 字节输入及 64 字节输出缓冲，重试 EINTR、部分写入并处理零字节 EOF，移除 fmt/bufio/os.File 初始化开销。Linux 测试和 Windows 交叉构建验证功能及构建；下列配对内存指标来自我们精确源在 Windows 评测的 Accepted。保留清晰教学源。

与 `1142_combinatorics.go` 相比：时间 0.001 s → 0.015 s；内存 1084 KB → 272 KB。

`1142_combinatorics_optimized.py`. 保留弱序递推，但用 choose*(n-k+1)//k 逐个生成 C(n,k)，不存杨辉三角。仅留 L+1 个答案，L=10，预处理 O(L²)。Python 仍保存切分输入和收集的输出，因此总空间为 O(L+I+O)，I,O 为输入输出大小。首个负查询终止处理。 Accepted 行标明实际评测运行时及成对时间/内存。先 flush 输出，再以 os._exit(0) 跳过解释器清理；实测内存收益属于该运行时，不代表渐近加速。

与 `1142_combinatorics.py` 相比：时间 0.031 s → 0.125 s；内存 436 KB → 220 KB。

`1142_combinatorics_optimized.rs`. 保留弱序递推，逐个生成二项式系数，去掉 11×11 杨辉矩阵。仅存十一项 u64，流式读查询至负数或 EOF，通过 C 运行时输出字节，不留整段输入/输出字符串。L=10、Q 个查询下时间 O(L²+Q)、辅助空间 O(L)，保留简单表版。

与 `1142_combinatorics.rs` 相比：时间 0.001 s → 0.001 s；内存 220 KB → 44 KB。

`1142_combinatorics_optimized.java`. 保留有序划分递推。使用 1 KB 字节缓冲区读取整数，只保留 ways[0..L]，其中 L=10；逐项乘除生成二项式系数，不保存 Pascal 矩阵。移除 StreamTokenizer、BufferedReader 和 PrintWriter。答案累积在 StringBuilder 中，遇到负数询问或 EOF 后统一输出。Q 个询问的时间为 O(L²+Q)，空间为 O(L+Q)，包含输出缓冲；输出空间不是常数。基础版本保留。

精确源代码的 Accepted #11326631：0.046 s / 336 KB。2026-11-20 保存的 Java 1.8 样本中，时间排名 3/44，内存排名 2/44。星号仍表示单独的语言排名目标。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1142_combinatorics_optimized.java`: 时间降低 +50.54%; 内存降低 +79.05%; 基础版本: `1142_combinatorics.java`.

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1142_combinatorics_optimized.py`：在该可比样本中，时间名次 25/26，内存名次 2/26。

`1142_combinatorics_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1142_combinatorics.cpp](1142_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(1) per query | AC | 0.001 s | 128 KB | 11279451 |
| [1142_combinatorics.go](1142_combinatorics.go) | Go 1.14 x64 | combinatorics | O(1) per query | AC | 0.001 s | 1084 KB | 11279453 |
| [1142_combinatorics.java](1142_combinatorics.java) | Java 1.8 | combinatorics | O(1) per query | AC | 0.093 s | 1604 KB | 11279455 |
| [1142_combinatorics.py](1142_combinatorics.py) | Python 3.12 x64 | combinatorics | O(1) per query | AC | 0.031 s | 436 KB | 11279454 |
| [1142_combinatorics.rs](1142_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(1) per query | AC | 0.001 s | 220 KB | 11279457 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1142_combinatorics_optimized.java](1142_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O(L²+Q) time; O(L+Q) space | AC | 0.046 s | 336 KB | 11326631 |
| [1142_combinatorics_optimized.py](1142_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(L²+I+O) time; O(L+I+O) space | AC | 0.125 s | 220 KB | 11325472 |
| [1142_combinatorics_optimized.rs](1142_combinatorics_optimized.rs) \* | Rust 1.75 x64 | combinatorics | O(L²+Q) time; O(L) space | AC | 0.001 s | 44 KB | 11325499 |
| [1142_combinatorics_optimized.go](1142_combinatorics_optimized.go) \* | Go 1.14 x64 | combinatorics | O(L²+Q) time; O(L²) space | AC | 0.015 s | 272 KB | 11325652 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
