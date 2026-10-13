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

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1427_greedy.cpp](1427_greedy.cpp) | G++ 13.2 x64 | greedy | O(L) | AC | 0.031 s | 924 KB |
| [1427_greedy.go](1427_greedy.go) | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 3196 KB |
| [1427_greedy.java](1427_greedy.java) | Java 1.8 | greedy | O(L) | AC | 0.093 s | 1612 KB |
| [1427_greedy.py](1427_greedy.py) | Python 3.12 x64 | greedy | O(L) | AC | 0.093 s | 4392 KB |
| [1427_greedy.rs](1427_greedy.rs) | Rust 1.75 x64 | greedy | O(L) | AC | 0.031 s | 1252 KB |
