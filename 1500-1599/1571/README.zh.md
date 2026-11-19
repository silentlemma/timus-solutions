# 1571. 翻译

[Timus 1571](https://acm.timus.ru/problem.aspx?space=1&num=1571) · 难度 451 · constructive

原题作者 Sergey Pupyrev，出自 2007 年 10 月 6 日第十二届乌拉尔国立大学程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N ≤ 100 个施工队各说一种语言。一名翻译可以懂任意两种语言。任意两个队都必须能交谈，而且不能有别的队听懂他们
的谈话。输出最少的翻译人数及各自的语言（格式为 `lang1-lang2`），或输出 `Impossible`。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是每个队的语言。

## 输出

翻译人数及其语言对，或 `Impossible`。任何最优的方案都被接受。

## 评测方式

仓库使用语义检查器，接受满足以下条件的任意输出。 检查器要求最少译员数，以及由最多十个小写字母命名的互异语言对。任意两个团队的语言之间，必须能经过其他团队均不使用的语言相连。Impossible 必须与预期可行性一致。

## 样例

### 样例 1

输入:

```
3
russian
french
german
```

输出:

```
3
russian-english
english-german
english-french
```

## 解法

如果两个队语言相同，那么只要还有第三个队，它就无法在第二个队听不懂的情况下与第一个队交谈；若只有这两个队，
就不需要翻译。否则设 k 种语言互不相同。一个队不需要翻译，两个队需要一名懂这两种语言的翻译。

当 k ≥ 3 时，经过另一个队语言的谈话会被那个队听到，所以任意两个队之间的翻译必须连成一条链，链的中间语言都
不是任何队的语言。如果翻译只用各队的语言，他们会在这 k 种语言上构成连通图，只有 k − 1 条边时就是一棵树，
其中某条链会经过第三种语言。所以需要 k 名翻译，而 k 名也够了：把每个队的语言与一种没人说的语言（例如
english）配对。若有队说 english，中间语言就用第一个空闲的一或两个字母的名字：输出中的语言也不能超过十个字母，而 100 个队占不满全部 702 个这样的名字。
C++ 为 `O(N log N)`；其他语言平均为 `O(N)`。

注意事项：

- 同一语言的两个队不需要翻译，但三个队中有重复语言就不可能（测试 03、05）；
- 某个队本身可能说 english，所以中间语言必须是所有队都不会说的语言（测试 06、08）；
- 其他答案也被接受，例如三个队时用三对直接翻译构成三角形，所以检查器检验保密性。

## 优化解法

`1571_constructive_optimized.java`. Java 保留简单版本所述的算法和数据结构。固定字节缓冲区与 FastInput 替代 Scanner 及其正则表达式、区域设置处理。整数记号直接解析；需要字符串时仍进行 UTF-8 解码，十进制记号仍显式转换为数值。仅在需要前瞻时保存一个记号，输出算法不变。这样减少通用解析开销；表中列出算法工作量，输入扫描与字节数成正比，并使用有界输入缓冲区。

与 `1571_constructive.java` 相比：时间 0.156 s → 0.078 s；内存 1712 KB → 668 KB。

`1571_constructive_optimized.py`. 保留重复语言分支及经无团队使用语言的最小星形构造。逐个生成一/二字母候选，不分配全部 702 个或导入 string。n<=100 保证可找到未用名。语言记号保留为字节，逐边输出并先 flush 文本计数以保持顺序。仍留全部切分输入及语言集合：O(I) 空间，非常量。名字有界、字母表固定下 O(n) 时间，保留简单字符串版。

与 `1571_constructive.py` 相比：时间 0.078 s → 0.125 s；内存 548 KB → 212 KB。

新的 C++、Go、Rust 版本排序最多 100 个名字的有界表；每个名字连同终止零占 11 字节。相邻相等项检测重复。至少三个不同团队时，标记已用的一、二字母名字，在 26+26² 个候选中选择空闲枢纽；100 个团队不可能全部占用。每个团队连接到无人使用的语言，保持原有私密翻译构造及最少翻译数，以有界存储替换集合、哈希表及临时名字列表。名字长度至多十，排序 O(N log N)，不是对哈希基础版的渐近改进。C++/Rust 使用 C runtime 输入输出，Go 使用标准句柄。保留简单文件；Java/Python 复用符合标准的基础版。

已通过评测的基础实现 [1571_constructive.java](1571_constructive.java), [1571_constructive.py](1571_constructive.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。保留教学算法。复查的基础代码行使用其自身新精确源代码 Accepted 的指标与 ID；这些检查不算优化。

`1571_constructive_optimized.java`：在该可比样本中，时间名次 1/18，内存名次 4/18。

`1571_constructive_optimized.py`：在该可比样本中，时间名次 18/18，内存名次 1/18。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1571_constructive.cpp](1571_constructive.cpp) | G++ 13.2 x64 | constructive | O(N log N) | AC | 0.015 s | 436 KB | 11287792 |
| [1571_constructive.go](1571_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 1144 KB | 11287793 |
| [1571_constructive.java](1571_constructive.java) \* | Java 1.8 | constructive | O(N) | AC | 0.156 s | 1712 KB | 11287796 |
| [1571_constructive.py](1571_constructive.py) \* | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 548 KB | 11287794 |
| [1571_constructive.rs](1571_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.015 s | 444 KB | 11325605 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1571_constructive_sorting.cpp](1571_constructive_sorting.cpp) | G++ 13.2 x64 | constructive, sorting | O(N log N) | AC | 0.015 s | 128 KB | 11315139 |
| [1571_constructive_sorting.go](1571_constructive_sorting.go) \* | Go 1.14 x64 | constructive, sorting | O(N log N) | AC | 0.015 s | 304 KB | 11315142 |
| [1571_constructive_sorting.rs](1571_constructive_sorting.rs) \* | Rust 1.75 x64 | constructive, sorting | O(N log N) | AC | 0.031 s | 48 KB | 11315152 |
| [1571_constructive_optimized.java](1571_constructive_optimized.java) \* | Java 1.8 | constructive | O(N) | AC | 0.078 s | 668 KB | 11324818 |
| [1571_constructive_optimized.py](1571_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(n) under bounded names; O(I) space | AC | 0.125 s | 212 KB | 11325488 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
