# 2159. 遵守词序规则的最短且字典序最小的作文

[Timus 2159](https://acm.timus.ru/problem.aspx?space=1&num=2159) · 难度 1303 · graphs, greedy

原题作者 Valentin Zuev，出自 2021 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

作文是用单个空格分隔的单词序列。它必须包含 n 个关键词，k 条规则 (a, b) 中的每一条要求：只要出现 a，之后某处就必须出现 b。输出满足所有要求的最短作文，最短的有多个时输出字典序最小的（空格小于所有字母）；若不存在则输出 −1。时间限制 2 秒，内存限制 256 MB。

## 输入

n 和 k（1 ≤ n, k ≤ 10⁵），n 个互不相同的关键词，然后是 k 条互不相同的规则；所有单词总长度不超过 2 · 10⁶。每个单词都是由小写拉丁字母组成的非空序列。

## 输出

作文，或者 −1。

## 样例

### 样例 1

输入：

```
2 3
atan
tan
atan ate
atan tabular
zzz atan
```

输出：

```
atan ate tabular tan
```

### 样例 2

输入：

```
1 3
a
a b
b c
c a
```

输出：

```
-1
```

## 解法

必须出现的单词是关键词以及沿规则从它们可达的所有单词，一次搜索即可求出。只要可行，每个单词写一次就够了，所以最短作文的单词集合和长度都是固定的。一个单词必须排在它的规则在这些单词中指向的所有单词之前；重复一个单词没有帮助，因为它最后一次出现时的规则仍须在之后满足。所以作文存在当且仅当这些单词不构成环，此时作文就是它们的一个拓扑序。

所有这样的顺序长度相同，所以最小的那个可以贪心构造：用优先队列实现的 Kahn 算法每次写下当前可用的最小单词。直接比较单词是正确的，因为单词后接空格比任何以它开头的更长单词都小，空格是最小的字符。

设 L 为输入中所有单词的总长度，V 为输入中不同单词的数量，W 为最长单词的长度。在哈希表操作的期望成本下，时间复杂度为 O(L + k + V W log(V + 1))，空间复杂度为 O(L + V + k)。每次堆操作可比较 O(log(V + 1)) 对单词，每次比较可扫描 O(W) 个字符。

易错点：n 只统计关键词，规则还可能引入其他必需单词（测试 gen6，`heap 6`）。堆比较可能反复扫描较长的公共前缀（测试 gen10，`prefix 10`），所以不能将这部分成本仅计入 L 一次。特别是，当两个长单词与一条短单词链同时等待时，即使只有三个关键词，也可能在链的每一步都比较这两个长单词。

第一个样例中 "zzz" 不必出现，必需的单词 atan、ate、tabular、tan 在写下 atan 之后按字母顺序排列。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2159_graphs_greedy.cpp](2159_graphs_greedy.cpp) | G++ 13.2 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.156 s | 19804 KB |
| [2159_graphs_greedy.go](2159_graphs_greedy.go) | Go 1.14 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.203 s | 28672 KB |
| [2159_graphs_greedy.java](2159_graphs_greedy.java) | Java 1.8 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.515 s | 31516 KB |
| [2159_graphs_greedy.py](2159_graphs_greedy.py) | Python 3.12 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.625 s | 53616 KB |
| [2159_graphs_greedy.rs](2159_graphs_greedy.rs) | Rust 1.75 x64 | graphs, greedy | O(L + k + V W log(V + 1)) | AC | 0.140 s | 24824 KB |
