# 1889. 机场广播

[Timus 1889](https://acm.timus.ru/problem.aspx?space=1&num=1889) · 难度 308 · bruteforce

原题作者 Denis Dublennykh，出自 NEERC 2011 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Igor 听到了一段广播的 n 句话，知道其中一些句子的语言，其余是 "unknown"。广播用几种语言播报，每种语言至多一次，每种语言的句数相同。广播可能用了几种语言？按递增顺序列出所有可能，若一种也没有则输出 "Igor is wrong."。

## 输入

n（2 ≤ n ≤ 1000），然后是 n 行，每行为语言名（4 到 20 个小写字母）或 "unknown"；至少有一句是已知的。

## 输出

按递增顺序列出所有可能的语言数，或者 "Igor is wrong."。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
6
english
unknown
unknown
unknown
german
unknown
```

输出：

```
2 3 6
```

### 样例 2

输入：

```
4
english
french
unknown
english
```

输出：

```
Igor is wrong.
```

### 样例 3

输入：

```
3
zulu
zulu
zulu
```

输出：

```
1
```

## 解法

如果广播用了 k 种语言，那么 k 整除 n，句子分成 k 个连续的块，每块 n/k 句，每块一种语言。对每个约数 k 检查两件事：块中已知的句子必须属于同一种语言；任何语言都不能出现在两个不同的块中。没有已知句子的块可以是任意新语言。使用哈希集合时，期望时间为 `O(n·d(n))`；C++ 使用有序集合，时间为 `O(n·d(n)·log n)`。

第一个样例中如果只有一块，它会同时包含英语和德语，所以 1 不行。k = 2 时两块为 "english ? ?" 和 "? german ?"；k = 3 时是三对，英语在第一对、德语在第三对；而 6 在这里总是可行：答案为 2 3 6。

注意事项：

- 同一种语言出现在两个块中就使 k 不成立，如第三个样例中的 3 种语言；
- 全是未知句子的块是允许的；
- 输出的句子是带句点的 "Igor is wrong."。

在 125 段随机广播上，答案与一个独立的已通过实现一致。

## 优化解法

`1889_bruteforce_optimized.java`. 仍只检查 n 的约数 k，扫描每块是否一致。已知语言一次映射为正整数 ID，unknown 为零。以代际标记 int 数组防止同一已知语言跨块出现，替代每约数新建 HashSet 和反复比较字符串。每块仍最多一个已知 ID，未知块可分配不同未用语言。按 k 递增输出，保留精确失败句。tau(n) 个约数、名字至多20字符时，期望 O(n·tau(n)) 时间、O(n) 空间；哈希是期望代价，不是最坏保证。仍为同一枚举算法，数据更紧凑，输入缓冲256字节。

与 `1889_bruteforce.java` 相比：时间 0.125 s → 0.109 s；内存 684 KB → 708 KB。

Go 将已知短语压缩为连续语言组，保存名称及首尾短语编号。开放寻址表拒绝在其他已知语言之后再次出现的语言。对 n 的每个因数，检查每组均位于同一块内，且不同组使用不同块。d(n) 表示 n 的因数个数。最坏情况下哈希冲突会使分组构建耗时达到平方级。输入输出使用固定字节缓冲区；即使哈希冲突，也在 20 字节数组中精确比较名称。

已通过评测的基础实现 [1889_bruteforce.cpp](1889_bruteforce.cpp), [1889_bruteforce.java](1889_bruteforce.java), [1889_bruteforce.py](1889_bruteforce.py), [1889_bruteforce.rs](1889_bruteforce.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1889_trees_parsing_optimized.rs`. 用精确有序树替代随机哈希为语言编号，保留因子枚举和轮次标记分块验证。

Accepted #11329230 (Rust 1.75 x64): **0.015 s / 136 KB**. 历史对照: `1889_bruteforce.rs` (Rust 1.75 x64) — 0.046 s / 448 KB (#11325666).

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。保留教学算法。复查的基础代码行使用其自身新精确源代码 Accepted 的指标与 ID；这些检查不算优化。

`1889_bruteforce_optimized.java`：在该可比样本中，时间名次 6/22，内存名次 1/22。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1889_bruteforce.cpp](1889_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(n d(n) log n) | AC | 0.001 s | 512 KB | 11325660 |
| [1889_bruteforce.go](1889_bruteforce.go) | Go 1.14 x64 | bruteforce | O(n d(n)) | AC | 0.031 s | 1236 KB | 11291120 |
| [1889_bruteforce.java](1889_bruteforce.java) | Java 1.8 | bruteforce | O(n d(n)) | AC | 0.125 s | 684 KB | 11291124 |
| [1889_bruteforce.py](1889_bruteforce.py) | Python 3.12 x64 | bruteforce | O(n d(n)) | AC | 0.078 s | 528 KB | 11325663 |
| [1889_bruteforce.rs](1889_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(n d(n)) | AC | 0.046 s | 448 KB | 11325666 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1889_bruteforce_optimized.go](1889_bruteforce_optimized.go) | Go 1.14 x64 | bruteforce | O(n² + n d(n)) worst case | AC | 0.031 s | 792 KB | 11311147 |
| [1889_bruteforce_optimized.java](1889_bruteforce_optimized.java) | Java 1.8 | bruteforce | O(n tau(n)) expected | AC | 0.109 s | 708 KB | 11325437 |
| [1889_trees_parsing_optimized.rs](1889_trees_parsing_optimized.rs) | Rust 1.75 x64 | trees, parsing | O(n log n + n d(n)) time; O(n) space | AC | 0.015 s | 136 KB | 11329230 |
