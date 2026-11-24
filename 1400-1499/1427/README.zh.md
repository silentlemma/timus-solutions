# 1427. 短信

[Timus 1427](https://acm.timus.ru/problem.aspx?space=1&num=1427) · 难度 364 · greedy

原题作者 Dmitry Kovalioff、Nikita Rybak 与 Ilya Grebnov，出自 Timus Top Coders: First Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一段最多 100 000 个字符的文本（拉丁字母、空格、数字和标点 . , ; : ! ? - "）被切
成连续的若干条短信。只含字母和空格的短信最长可达 M 个字符，其他短信最长只有 N 个
（1 ≤ N ≤ M ≤ 10 000）。求短信的最少条数。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

N 和 M，然后单独一行是文本。

## 输出

短信的最少条数。

## 评测方式

仓库测试比较完整输出文本，仅忽略末尾空白。应保留有意义的空格、换行、大小写及标点。

## 样例

### 样例 1

输入:

```
10 15
On the 11-th of February, 2006 the contest "Timus Top Coders: First Challenge" is held!
```

输出:

```
8
```

## 解法

设 run(i) 为从位置 i 开始连续的字母和空格的个数。从 i 开始的短信可以在
i + max(N, min(M, run(i))) 之前的任何位置结束。这个最远终点随 i 增大不会后退（i + N
和字母段的终点都只增不减），在这种单调可达的情况下，每次都发送尽量长的短信的贪心
是最优的：任何其他方案在每一步都不会走得更远。字母段的长度从文本末尾往前计算。
`O(L)`。

注意事项：

- 文本可能以空格开头，所以第二行必须整行读入，而不能先跳过空白（测试 04）；
- 数字不算字母（测试 03、06）；
- 只有当字母段长于 N 时，长短信才有用（测试 05）。

## 优化解法

`1427_greedy_optimized.cpp`. 保留流式最长消息贪心规则及 ASCII 字母/空格分类。4 KiB fread 缓冲替代每字节一次带锁输入调用。只丢弃首行剩余内容与末尾 CR/LF，保留文本首尾空格及标点。当前长度和普通文本标志仍决定何时开始新消息。时间 O(L)，辅助存储固定，不保存完整文本。

精确源代码 Accepted #11326989：0.015 s / 88 KB。2026-11-20 保存的 G++ 13.2 样本：时间排名 1/67，内存排名 1/67。教学源代码保留。

`1427_greedy_optimized.py`. 保留最远可达贪心计消息数及 Unicode isalpha 语义。不预计算长 L 的后缀连续段数组，只扫描当前消息消耗的字母/空格至最大长度。扫描过的字符在下一轮前都已消耗，因此总扫描 O(L)。UTF-8 文本行仍保存：O(L) 输入空间、O(1) 附加状态。仅去掉 CR/LF，保留有意义的空格和标点。

与 `1427_greedy.py` 相比：时间 0.093 s → 0.14 s；内存 4392 KB → 1 852 KB。

C++ 和 Go 边读取文本边延长当前消息，只记录长度以及已有字符是否全为字母或空格。若下一个字符会超出相应限制，就结束当前消息，让该字符开始下一条。这仍是每次取最长消息的贪心规则，时间 O(L)，额外空间 O(1)。

保留的已接受基础实现 [1427_greedy.go](1427_greedy.go), [1427_greedy.java](1427_greedy.java), [1427_greedy.rs](1427_greedy.rs) 在保存的比较中满足严格快速版本收录：所需指标前十名或前 15%。直接复用，不创建相同副本；其他教学源代码保留。星号表示单独的语言排名目标。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1427_greedy_implementation_optimized.go`. 读取补充缓冲缩至 8192 字节，后缀连续长度改用 uint32。ReadString 仍读取完整合法长度的行及前导空格，贪心跳转规则不变。 词元转换及数值输出按实际类型专门化，移除未使用的通用分支，保留算法和注释。

Accepted #11329094 (Go 1.14 x64): **0.015 s / 1668 KB**. 历史对照: `1427_greedy.go` (Go 1.14 x64) — 0.031 s / 3196 KB (#11286186).

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1427_greedy_implementation_parsing_optimized.rs`. 有界后缀连续段长度改用 32 位，替代机器字长整数。保留按行读取及原匹配算法。 采用有界原生读取及完整原生写出、Windows 二进制描述符和 C 入口。纯数字输入直接从字节转为有符号整数，不分配词元；依赖行边界的输入保留完整行。

Accepted #11329172 (Rust 1.75 x64): **0.015 s / 708 KB**. 历史对照: `1427_greedy.rs` (Rust 1.75 x64) — 0.031 s / 1252 KB (#11286189).

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1427_greedy_optimized.py`：在该可比样本中，时间名次 4/11，内存名次 5/11。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1427_greedy.cpp](1427_greedy.cpp) | G++ 13.2 x64 | greedy | O(L) | AC | 0.031 s | 924 KB | 11286185 |
| [1427_greedy.go](1427_greedy.go) | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 3196 KB | 11286186 |
| [1427_greedy.java](1427_greedy.java) | Java 1.8 | greedy | O(L) | AC | 0.093 s | 1612 KB | 11286188 |
| [1427_greedy.py](1427_greedy.py) | Python 3.12 x64 | greedy | O(L) | AC | 0.093 s | 4392 KB | 11286187 |
| [1427_greedy.rs](1427_greedy.rs) | Rust 1.75 x64 | greedy | O(L) | AC | 0.031 s | 1252 KB | 11286189 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1427_greedy_optimized.cpp](1427_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(L) | AC | 0.015 s | 88 KB | 11326989 |
| [1427_greedy_optimized.go](1427_greedy_optimized.go) | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 912 KB | 11310457 |
| [1427_greedy_optimized.py](1427_greedy_optimized.py) | PyPy 3.10 x64 | greedy | O(L) time; O(L) input space | AC | 0.14 s | 1852 KB | 11325485 |
| [1427_greedy_implementation_optimized.go](1427_greedy_implementation_optimized.go) | Go 1.14 x64 | greedy, implementation | O(L) | AC | 0.015 s | 1668 KB | 11329094 |
| [1427_greedy_implementation_parsing_optimized.rs](1427_greedy_implementation_parsing_optimized.rs) | Rust 1.75 x64 | greedy, implementation, parsing | O(L) | AC | 0.015 s | 708 KB | 11329172 |
