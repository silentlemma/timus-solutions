# 2018. 限制连续段长度的序列计数

[Timus 2018](https://acm.timus.ru/problem.aspx?space=1&num=2018) · 难度 102 · dp, prefix_sums

原题作者 Olga Soboleva（由 Alex Samsonov 整理），出自 NEERC 2014 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计由 1、2 构成的长度为 `n` 的序列。连续的 1 至多有 `a` 个，连续的 2
至多有 `b` 个。某个位置不同就视为不同序列。答案对 `1,000,000,007` 取模。
约束为 `1 ≤ a,b ≤ 300`、`max(a,b)+1 ≤ n ≤ 50,000`。
时间限制 2 秒，内存限制 64 MB。

## 输入

唯一一行包含 `n a b`。

## 输出

输出合法序列数量对 `1,000,000,007` 取模的结果。

## 评测方式

按记号逐个比较输出。

## 样例

```
3 2 1
```

```
4
```

## 解法

设 one[i] 为长度 i、以一串 1 结尾的合法序列数，two[i] 为以一串 2 结尾的序列数。
以 r 个 1（1 ≤ r ≤ a）结尾的序列，就是一个长度 i − r、以 2 结尾的序列后面接上这一
串；空序列在两边各算一次，one[0] = two[0] = 1。因此

- one[i] = two[i − 1] + two[i − 2] + … + two[max(0, i − a)]，
- two[i] = one[i − 1] + … + one[max(0, i − b)]，

答案是 one[n] + two[n] 对 10⁹ + 7 取模。每个和都是同一数组两个前缀和之差，所以每个
长度只需 `O(1)`，总共 `O(n)`。

在样例 n = 3、a = 2、b = 1 中，合法的序列是 112、121、211 和 212：22 中 2 的连续段
长于 b，111 中 1 的连续段长于 a。

注意事项：

- 空序列在每个和中只算一次，且从不算作答案；
- 两个前缀和之差对 10⁹ + 7 取模后可能为负。

## 优化解法

优化的 Java 解法只保存这些和还需要的值：two 的最后 a + 1 个值和 one 的最后 b + 1
个值，放在环形缓冲区中，同时维护两个窗口和，每个长度把窗口移动一步，而不是用前缀
和相减。它还手工解析这三个数，而不是使用 `Scanner`：0.093 s，而不是 0.125 s；
408 KB，而不是 3140 KB。

## 各语言说明

- Python 的 `%` 本来就给出非负余数；C++、Go 和 Java 先加上模数再取余，Rust 使用
  `rem_euclid`。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2018_dp_prefix_sums.cpp](2018_dp_prefix_sums.cpp) | G++ 13.2 x64 | dp, prefix_sums | O(n) | AC | 0.015 s | 1368 KB | 11303350 |
| [2018_dp_prefix_sums.go](2018_dp_prefix_sums.go) | Go 1.14 x64 | dp, prefix_sums | O(n) | AC | 0.031 s | 2688 KB | 11303351 |
| [2018_dp_prefix_sums.java](2018_dp_prefix_sums.java) | Java 1.8 | dp, prefix_sums | O(n) | AC | 0.125 s | 3140 KB | 11303352 |
| [2018_dp_prefix_sums.py](2018_dp_prefix_sums.py) | Python 3.12 x64 | dp, prefix_sums | O(n) | AC | 0.156 s | 8624 KB | 11303354 |
| [2018_dp_prefix_sums.rs](2018_dp_prefix_sums.rs) | Rust 1.75 x64 | dp, prefix_sums | O(n) | AC | 0.015 s | 1648 KB | 11303355 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2018_dp_prefix_sums_optimized.java](2018_dp_prefix_sums_optimized.java) | Java 1.8 | dp, prefix_sums | O(n) | AC | 0.093 s | 408 KB | 11303659 |
