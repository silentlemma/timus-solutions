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

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1889_bruteforce.cpp](1889_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(n d(n) log n) | AC | 0.015 s | 532 KB |
| [1889_bruteforce.go](1889_bruteforce.go) | Go 1.14 x64 | bruteforce | O(n d(n)) | AC | 0.031 s | 1236 KB |
| [1889_bruteforce.java](1889_bruteforce.java) | Java 1.8 | bruteforce | O(n d(n)) | AC | 0.125 s | 684 KB |
| [1889_bruteforce.py](1889_bruteforce.py) | Python 3.12 x64 | bruteforce | O(n d(n)) | AC | 0.093 s | 476 KB |
| [1889_bruteforce.rs](1889_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(n d(n)) | AC | 0.015 s | 452 KB |
