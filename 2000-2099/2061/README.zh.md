# 2061. 统计富二进制词

[Timus 2061](https://acm.timus.ru/problem.aspx?space=1&num=2061) · 难度 3178 · strings, bruteforce

原题作者 Mikhail Rubinchik，出自 2015 年 7 月 11 日回文专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

长度为 n 的词如果恰好含有 n 个不同的非空回文子串，就称为富词。对 1 到 n 的每个长度 i，统计二字母表上长度为 i 的富词个数。时间限制 1 秒，内存限制 64 MB。

## 输入

一个整数 n，1 ≤ n ≤ 61。

## 输出

n 行：长度为 1, 2, …, n 的富二进制词的个数。

## 评测方式

按记号逐个比较输出。

## 样例

### 样例 1

输入：

```
4
```

输出：

```
2
4
8
16
```

## 解法

输入只有 61 种可能，而答案增长到约 3·10¹²，不可能在一秒内逐个列出这些词。所以答案事先离线算好一次，程序只从表中输出前 n 个。真正有意思的是这张表如何计算。

在词后添加一个字母最多带来一个新的不同回文：新回文必然是后缀；若两个后缀 `U` 和 `V`（`|U| > |V|`）都是新的，那么 `V` 作为回文 `U` 的回文后缀也是它的前缀，因而早已出现过。因此长度为 L 的词至多有 L 个不同回文，恰好 L 个当且仅当每个字母都带来了一个新回文。于是富词的每个前缀都是富词，富词构成一棵树，其中每个词都是某个富词加一个字母。

用深度优先搜索遍历这棵树。对当前词维护回文树：每个不同的回文一个结点，后缀链接指向最长的真回文后缀，转移为 `c: P → cPc`。尝试字母 c 时，从最长回文后缀沿后缀链接走，直到它前面的字母等于 c；找到的回文两端加上 c 就是新的最长回文后缀。若该结点已存在，加上 c 的词不是富词，剪掉这个分支；否则创建结点并继续深入，回溯时再删除结点和转移。每一步至多 O(L)，深度不超过 61，所需内存极少。

交换两个字母把富词变为富词，所以搜索从字母 0 开始，所有计数再乘二。以 0 开头、长度为 20 的词把工作分成相互独立的部分，供多个线程处理。整个搜索约访问 5·10¹² 个词，在 22 个线程上约需一个半小时。对长度不超过 60 的所有情形，结果都与 OEIS 中的序列 A216264 一致。[2061_strings_bruteforce_table.py](2061_strings_bruteforce_table.py) 是同一搜索的 Python 版本：算完全部 61 个长度太慢，但几秒内就能核对前面的数值。

样例中长度为 4 的 16 个词都是富词；第一批非富词出现在长度 8，例如 00101100。

## 各语言说明

最大的计数 2 966 632 985 826 需要 64 位整数。每个程序都把表存为常量，并输出其前 n 项。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2061_strings_bruteforce.cpp](2061_strings_bruteforce.cpp) | G++ 13.2 x64 | strings, bruteforce | O(n) | AC | 0.001 s | 132 KB |
| [2061_strings_bruteforce.go](2061_strings_bruteforce.go) | Go 1.14 x64 | strings, bruteforce | O(n) | AC | 0.001 s | 1048 KB |
| [2061_strings_bruteforce.java](2061_strings_bruteforce.java) | Java 1.8 | strings, bruteforce | O(n) | AC | 0.046 s | 1524 KB |
| [2061_strings_bruteforce.py](2061_strings_bruteforce.py) | Python 3.12 x64 | strings, bruteforce | O(n) | AC | 0.046 s | 400 KB |
| [2061_strings_bruteforce.rs](2061_strings_bruteforce.rs) | Rust 1.75 x64 | strings, bruteforce | O(n) | AC | 0.015 s | 208 KB |
