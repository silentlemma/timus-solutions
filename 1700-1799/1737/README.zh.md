# 1737. 助记符与回文 3

[Timus 1737](https://acm.timus.ru/problem.aspx?space=1&num=1737) · 难度 254 · strings

原题作者 Alexander Ipatov，出自第十四届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

按字母序列出由字母 a、b、c 组成、长度为 n、且不含长度至少为 2 的回文子串的所有单词。若它们总长度超过 100 000 个字母，输出 `TOO LONG`。

## 输入

n（1 ≤ n ≤ 20 000）。

## 输出

每行一个单词，或者 `TOO LONG`。

## 样例

### 样例 1

输入：

```
2
```

输出：

```
ab
ac
ba
bc
ca
cb
```

## 解法

长度至少为 2 的回文中间必有长度为 2 或 3 的回文，所以只需相邻字母不同、相隔一个的字母也不同。
于是任意连续三个字母都是 a、b、c 的某种排列，每个字母都重复三位之前的字母：单词是 a、b、c 六种排列之一的重复。
因此 n = 1 时有三个单词，更大的 n 都有六个；当 6n > 100 000，即从 n = 16 667 起，答案是 `TOO LONG`。`O(n)`。

注意事项：

- n = 1 时六种排列只给出三个不同的单词；
- 限制针对总长度，而不是单词个数。

对 n 不超过 9，列表与逐一检查所有由 a、b、c 组成的单词的结果一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1737_strings.cpp](1737_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 252 KB |
| [1737_strings.go](1737_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1448 KB |
| [1737_strings.java](1737_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 3052 KB |
| [1737_strings.py](1737_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.125 s | 1132 KB |
| [1737_strings.rs](1737_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 328 KB |
