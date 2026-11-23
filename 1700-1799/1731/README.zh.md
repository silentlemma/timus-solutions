# 1731. 莳萝

[Timus 1731](https://acm.timus.ru/problem.aspx?space=1&num=1731) · 难度 106 · constructive

原题作者 Eugene Kurpilyansky（由 Sofia Tekhazheva 准备），出自 2009 年乌拉尔地区程序设计团队竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

为 n 箱第一种莳萝和 m 箱第二种莳萝选定质量——互不相同、不超过 10⁹ 的正整数——使得无法给两位邻居各送一箱每种莳萝且总质量相等。

## 输入

n 和 m（2 ≤ n, m ≤ 50）。

## 输出

一行 n 个第一种的质量，下一行 m 个第二种的质量。任何符合要求的质量都可以。

## 评测方式

仓库使用语义检查器，接受满足以下条件的任意输出。 仓库检查器要求恰好两行，分别有 n 和 m 个整数质量。全部 n+m 个质量须互异且在 [1,10^9] 内，全部 n*m 个跨组和也须互异。构造总存在，不接受失败信息。

## 样例

### 样例 1

输入：

```
2 3
```

输出：

```
1 2
5 10 12
```

## 解法

两份礼物 a + b 和 a′ + b′ 没有共同的箱子；而有共同箱子的两个和本来就不同，因为所有质量互不相同。
所以条件就是全部 n·m 个和 a_i + b_j 互不相同。

取 a_i = i（i = 1..n），b_j = (j + 1)·n + 1（j = 0..m − 1）。于是 a_i + b_j = (j + 1)·n + 1 + i，
由于 i 取遍 1..n，这个和同时确定 i 和 j，就像 n 进制数确定末位和其余部分一样。所有质量互不相同，最大不到 3000。`O(n + m)`。

对样例得到 1 2 和 3 5 7，各和为 4、6、8、5、7、9。

注意事项：

- 答案总是存在，所以永远不输出 "It is a lie!"；
- 第二种不能与第一种的质量重复，所以从大于 n 开始。

检查程序验证数量、范围、互不相同以及所有和都不同。

## 优化解法

优化的 C++ 解法用 `scanf` 而不是 `std::cin` 读取 n 和 m，因此程序完全不引入
`iostream`；质量的输出方式不变：{1731_constructive_optimized.cpp}。

优化的 Java 解法直接从 `System.in` 逐位读取 n 和 m，而不是创建 `Scanner`——后者的
初始化比程序其余部分都费时；输出的构造方式不变：
{1731_constructive_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1731_constructive_optimized.cpp`: 时间降低 +0.00%; 内存降低 +67.02%; 基础版本: `1731_constructive.cpp`.

- `1731_constructive_optimized.java`: 时间降低 +45.61%; 内存降低 +76.20%; 基础版本: `1731_constructive.java`.

`1731_constructive_optimized.py`. 保留第一类质量 1..n，第二类 j*n+1（j=1..m）。第一组均小于第二组；相邻第二类质量对应的和占据互不相交的 n 值区间，因此礼物总质量各不相同。n,m<=50 时最大质量为 2501。以 O(n+m) 次有界数字操作输出所需两行。 仍构造并连接每行输出，首行使用 map(str,range(...))。拼接字符串的峰值空间仍为 O(n+m)，并非常数空间流式输出。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1731_constructive.py` 相比：时间 0.093 s → 0.125 s；内存 416 KB → 208 KB。

`1731_constructive_optimized.rs`. 保留第一类质量 1..n，第二类 j*n+1（j=1..m）。第一组均小于第二组；相邻第二类质量对应的和占据互不相交的 n 值区间，因此礼物总质量各不相同。n,m<=50 时最大质量为 2501。以 O(n+m) 次有界数字操作输出所需两行。 生成一个质量即输出，去掉两个 Vec<String> 集合及整行拼接。额外状态 O(1)。 Rust 版本通过 C 运行库读写，不保留解码后的输入 String，也不构造格式化的输出 String。保留简单版本及其 Accepted。

与 `1731_constructive.rs` 相比：时间 0.046 s → 0.031 s；内存 220 KB → 56 KB。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1731_constructive_optimized.go`. 保留原有算法和边界处理，用数字及词元转换和可复用输出缓冲区替代 fmt。整个输入保存在字节缓冲区中，以存储输入的空间换取较少的通用输入输出开销。

Accepted #11328592 (Go 1.14 x64): **0.031 s / 972 KB**. 历史对照: `1731_constructive.go` (Go 1.14 x64) — 0.046 s / 1104 KB (#11289416).

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1731_constructive_optimized.py`：在该可比样本中，时间名次 24/40，内存名次 1/40。

`1731_constructive_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1731_constructive.cpp](1731_constructive.cpp) | G++ 13.2 x64 | constructive | O(n + m) | AC | 0.015 s | 376 KB | 11304041 |
| [1731_constructive.go](1731_constructive.go) | Go 1.14 x64 | constructive | O(n + m) | AC | 0.046 s | 1104 KB | 11289416 |
| [1731_constructive.java](1731_constructive.java) | Java 1.8 | constructive | O(n + m) | AC | 0.171 s | 1580 KB | 11289419 |
| [1731_constructive.py](1731_constructive.py) | Python 3.12 x64 | constructive | O(n + m) | AC | 0.093 s | 416 KB | 11289417 |
| [1731_constructive.rs](1731_constructive.rs) | Rust 1.75 x64 | constructive | O(n + m) | AC | 0.046 s | 220 KB | 11304042 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1731_constructive_optimized.cpp](1731_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(n + m) | AC | 0.015 s | 124 KB | 11304262 |
| [1731_constructive_optimized.java](1731_constructive_optimized.java) | Java 1.8 | constructive | O(n + m) | AC | 0.093 s | 376 KB | 11304040 |
| [1731_constructive_optimized.py](1731_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(n+m) | AC | 0.125 s | 208 KB | 11325001 |
| [1731_constructive_optimized.rs](1731_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(n+m) | AC | 0.031 s | 56 KB | 11325108 |
| [1731_constructive_optimized.go](1731_constructive_optimized.go) | Go 1.14 x64 | constructive | O(n + m) | AC | 0.031 s | 972 KB | 11328592 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
