# 1711. 代号

[Timus 1711](https://acm.timus.ru/problem.aspx?space=1&num=1711) · 难度 135 · greedy

原题作者 Alex Samsonov，由 Igor Chevdar 整理，出自 NEERC 2009 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 道题中每道都有三个候选代号，题目在题集中按代号的字典序排列。为每道题选一个代号，使题目按给定的顺序排列，
或者报告无法做到。

## 输入

n（1 ≤ n ≤ 16），然后 n 行，每行是一道题的三个代号：由小写拉丁字母组成，长度至多
20，所有代号互不相同。最后一行是要求的顺序，即 1 … n 的一个排列。

## 输出

按要求的顺序输出所选的代号，每行一个，或者输出 IMPOSSIBLE。任何正确的选择都可以。

## 评测方式

仓库使用语义检查器，接受满足以下条件的任意输出。 仓库检查器仅在保存参考同为 IMPOSSIBLE 时接受它。否则要求恰好 n 个名字记号，各自属于给定顺序相应题目的选项，并严格递增。任意有效选择均可，不比较换行。

## 样例

### 样例 1

输入：

```
11
cipher grille kamkohob
names codenames codes
newtests rejudge timus
size volume summit
watchmen braineater twosides
solution random yesorno
keywords subversion commands
bosses shooting shaitan
game strategy playgame
mnemonic palindromes bestname
eligibility rectangle rules
2 1 7 10 9 6 11 3 8 4 5
```

输出：

```
codenames
grille
keywords
mnemonic
playgame
random
rectangle
rejudge
shaitan
volume
watchmen
```

### 样例 2

输入：

```
3
problems in the
first sample are
ordered not randomly
1 2 3
```

输出：

```
IMPOSSIBLE
```

## 已接受提交更新

更新的文件：[1711_greedy_parsing_optimized.rs](1711_greedy_parsing_optimized.rs)。解答表列出了与当前源文件完全对应的新 Accepted 结果。这些文件此前的比较测量和排名属于旧源文件版本，作为历史数据保留。缓存审计确认该题所有可用语言均有达标实现。保留教学版本以保持清晰；若同一源文件同时承担快速版本的角色，它也必须满足性能标准。

## 解法

按要求的顺序依次处理，给每道题选它的代号中排在前一个所选代号之后的最小者；若没有这样的代号，答案为 IMPOSSIBLE。

这种贪心是安全的。假设存在某个正确的选择，逐题与贪心比较。由归纳法，贪心的代号永远不晚于正确的代号：
下一题的正确代号排在正确的前一个代号之后，因此也排在贪心的前一个代号之后，所以它是候选之一，
而贪心选出的不大于它。于是贪心过程永远不会卡住。`O(n)` 次短字符串比较。

注意事项：

- 代号按字符串比较，前缀排在前面："code" 在 "codenames" 之前；
- 顺序行按题集中的位置列出题号，而不是每道题的位置；
- 任何正确答案都可以，所以测试使用检查程序。

检查程序验证每个代号属于对应的题目，并且代号递增。在 600 个随机题集上，答案与一个独立的已通过实现一致。

## 优化解法

`1711_greedy_optimized.java`. 保留每步选择最小可行名称的贪心规则。直接从现有 System.in 流读取 ASCII 字节，将每个项目的三个名称存入同一个扁平字节数组并另存长度，逐一检查候选，而不对 String 数组排序。比较公共前缀后再比较长度，正确处理一个名称是另一个名称前缀的情况。完整答案存入字节数组，用普通 System.out.write 并刷新输出；后续无解时丢弃部分答案。输入共 B 字节、名称长度 L<=20 时，时间 O(B+nL)，额外空间 O(nL)。完全相同的源文件再运行三次，分别得到 (0.125 s, 384 KB)、(0.093 s, 340 KB)、(0.125 s, 336 KB)。表格采用真实的第二次提交，相对保留的 Java 基础版本，时间减少 33.57%，内存减少 34.11%。这里明确展示测量波动，不把第二次的 0.093 s 与第三次的 336 KB 拼接。

与 `1711_greedy.java` 相比：时间 0.140 s → 0.093 s；内存 516 KB → 340 KB。

`1711_greedy_optimized.py`. 保留贪心：在三个名字中取严格大于前名的最小者。直接扫描三个字节串，不排序或建立过滤列表；直接消费顺序记号，不另建整数 ID 表。用一个 bytearray 存答案，后续失败时整体改为 IMPOSSIBLE，不输出部分答案。名字为小写 ASCII，L<=20，字节顺序即字典序。B 输入字节下时间 O(B+nL)、空间 O(B+nL)，非常数空间。刷新后 os._exit(0)。实测0.093降至0.062秒，但内存492增至776KB；按时间收益收录，不声称节省内存。

与 `1711_greedy.py` 相比：时间 0.093 s → 0.062 s；内存 492 KB → 776 KB。

优化的 C++ 解法用 `scanf` 读入一个 16 × 3 个名字、每个 21 字节的固定数组
（n ≤ 16，名字最多 20 个字母再加结尾的零，足够放下），而不是通过 `iostream`
读入由 `std::string` 组成的二维向量。它不对每道题的三个名字排序，而是用 `strcmp`
逐个比较，找出排在上一个选择之后的最小名字，只记下所选名字的指针，最后用 `puts`
输出：{1711_greedy_optimized.cpp}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1711_greedy_optimized.cpp`: 时间降低 +51.61%; 内存降低 +74.75%; 基础版本: `1711_greedy.cpp`.

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1711_greedy_optimized.go`. 保留原有算法和边界处理，用数字及词元转换和可复用输出缓冲区替代 fmt。整个输入保存在字节缓冲区中，以存储输入的空间换取较少的通用输入输出开销。

Accepted #11328588 (Go 1.14 x64): **0.031 s / 976 KB**. 历史对照: `1711_greedy.go` (Go 1.14 x64) — 0.062 s / 1148 KB (#11289207).


`1711_greedy_parsing_optimized.rs`. 按最多16条记录、每条三个且每名至多20字节使用固定栈存储。以有界字节词元读名，保留严格大于前名的最小字典序选择，一次写出有界答案；输入、名称和答案均无需堆分配。

此精确源码有独立 Accepted，并满足统一的[排名标准](../../RATING_CRITERIA.md)。下述时间与内存来自同一次提交，重复测量可能因评测计时而不同。保留已有简单版本和不同的优化版本。

Accepted #11329353 (Rust 1.75 x64): **0.015 s / 60 KB**.

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1711_greedy_optimized.py`：在该可比样本中，时间名次 1/21，内存名次 20/21。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1711_greedy.cpp](1711_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.031 s | 396 KB | 11304067 |
| [1711_greedy.go](1711_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.062 s | 1148 KB | 11289207 |
| [1711_greedy.java](1711_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.140 s | 516 KB | 11289209 |
| [1711_greedy.py](1711_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.093 s | 492 KB | 11304068 |
| [1711_greedy.rs](1711_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.046 s | 236 KB | 11289213 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1711_greedy_optimized.cpp](1711_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 100 KB | 11304441 |
| [1711_greedy_optimized.py](1711_greedy_optimized.py) | Python 3.12 x64 | greedy | O(B+nL) | AC | 0.062 s | 776 KB | 11325459 |
| [1711_greedy_optimized.java](1711_greedy_optimized.java) | Java 1.8 | greedy | O(B+nL) | AC | 0.093 s | 340 KB | 11325999 |
| [1711_greedy_optimized.go](1711_greedy_optimized.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 976 KB | 11328588 |
| [1711_greedy_parsing_optimized.rs](1711_greedy_parsing_optimized.rs) | Rust 1.75 x64 | greedy, parsing | O(n) | AC | 0.015 s | 56 KB | 11330236 |
