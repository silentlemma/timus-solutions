# 1002. 用最少的单词拼出号码

[Timus 1002](https://acm.timus.ru/problem.aspx?space=1&num=1002) · 难度 226 · dp, hashing

原题出自 1999 年中欧信息学奥林匹克竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每个小写拉丁字母对应一个数字：

| 数字 | 字母 |
|------|------|
| 1 | i j |
| 2 | a b c |
| 3 | d e f |
| 4 | g h |
| 5 | k l |
| 6 | m n |
| 7 | p r s |
| 8 | t u v |
| 9 | w x y |
| 0 | o q z |

一个单词对应由其各字母的数字组成的字符串。给定一个号码（不超过 100 位的数字串）和一个
含 `n ≤ 50 000` 个单词的词典，求一个单词数最少的词典单词序列，使它们对应的数字串依次
拼接后恰好等于该号码。每个单词可以使用任意多次。

输入包含多组这样的测试，总大小不超过 300 KB。

时间限制：2 秒。内存限制：64 MB。

## 输入

各组测试依次给出。每组测试为：一行号码，一行 `n`，以及 `n` 行单词（每行一个，由 1 到 50 个
小写字母组成）。以一行 `-1` 结束输入。

## 输出

每组测试输出一行：最短序列中的单词，用单个空格分隔；若无法拼出号码，则输出
`No solution.`。

## 评测方式

接受任意一个最短序列：检查器会验证这些单词都在词典中、它们能拼出号码，并且不存在更短的
序列。

## 样例

### 样例 1

输入：

```
8733
3
use
e
tree
12
2
ab
cd
-1
```

输出：

```
tree
No solution.
```

### 样例 2

输入：

```
22
4
ac
ba
b
c
-1
```

输出：

```
ac
```

## 题解

对号码的前缀做动态规划：`best[i]` 表示拼出前 `i` 位所需的最少单词数，`best[0] = 0`。从每个
可达位置 `i` 出发，尝试所有对应数字串与从 `i` 开始的子串相同的单词，并记录最后一个单词以便
还原答案。

在每个位置尝试全部 `n` 个单词，每组测试的代价为 `O(100 · n · 50)`。更快的做法是把词典放进
“数字串 → 单词”的哈希表：单词长度不超过 50，所以每个位置只需查找长度为 1 到 50 的子串。
每组测试只需 `O(100 · 50)` 次查找，外加 `O(单词总长度)` 建表，在任何语言中都很快。

注意事项：

- 多个单词可能对应相同的数字串：保留其中任意一个即可；
- 一个单词可以使用多次；
- 无解时输出必须恰好是 `No solution.`。

## 各语言说明

- **C++**：`std::unordered_map<std::string, int>`；在 `sync_with_stdio(false)` 之后用 `cin` 读入。
- **Go**：`map[string]int`，`phone[i:i+l]` 是开销很小的子串。
- **Python**：哈希表用 `dict`，单词的数字串由 `str.translate` 得到；基于查找的版本很快，而在
  每个位置比较每个单词会太慢。
- **Java**：`HashMap<String, Integer>` 配合 `putIfAbsent`；用 `BufferedReader` 和
  `StringTokenizer` 读入。
- **Rust**：`HashMap<Vec<u8>, usize>`，用号码的字节切片进行查找。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1002_dp_hashing.cpp](1002_dp_hashing.cpp) | G++ 13.2 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.015 s | 2764 KB |
| [1002_dp_hashing.go](1002_dp_hashing.go) | Go 1.14 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.031 s | 3016 KB |
| [1002_dp_hashing.java](1002_dp_hashing.java) | Java 1.8 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.109 s | 7032 KB |
| [1002_dp_hashing.py](1002_dp_hashing.py) | Python 3.12 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.093 s | 5424 KB |
| [1002_dp_hashing.rs](1002_dp_hashing.rs) | Rust 1.75 x64 | dp, hashing | O(100 * 50) lookups per test + O(total word length) | AC | 0.031 s | 2540 KB |
