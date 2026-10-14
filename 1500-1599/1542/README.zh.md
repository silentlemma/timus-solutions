# 1542. 自动补全

[Timus 1542](https://acm.timus.ru/problem.aspx?space=1&num=1542) · 难度 624 · sorting

原题作者 Den Raskovalov，出自 2007 年 4 月 21 日在叶卡捷琳堡举行的第十一届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

词典中有 N 个不同的单词（N ≤ 10⁵，每个至多 15 个小写字母）及其频率（不超过 10⁶）。对 M ≤
15000 个输入的前缀，各列出至多十个以其开头的单词，频率高的在前，频率相同则按字母顺序。

时间限制：2 秒。内存限制：64 MB。

## 输入

N，然后 N 行，每行一个单词及其频率，然后是 M 和 M 个前缀，每行一个。

## 输出

每个前缀的补全结果，每行一个；相邻前缀的列表之间用空行分隔。

## 样例

### 样例 1

输入:

```
5
kare 10
kanojo 20
karetachi 1
korosu 7
sakura 3
3
k
ka
kar
```

输出:

```
kanojo
kare
korosu
karetachi

kanojo
kare
karetachi

kare
karetachi
```

## 解法

先把单词按频率降序、再按字母顺序排序一次。把每个不同的查询放进哈希表，对应一个空列表。然
后依次处理排好序的单词：对单词的至多 15 个前缀中属于查询的那些，若其列表还不满十个就把单词
追加进去。由于单词已按要求的顺序到来，每个列表最终恰好就是答案。总时间为 `O(N log N + 15·N + M)`，
重复的查询共用同一个列表。

注意事项：

- 没有单词的前缀在输出中仍占一个位置：一个空块，开头或结尾也一样（测试 02）；
- 频率相同时按字母顺序，所以 a 在 ab 之前（测试 03）；
- 查询可能恰好等于某个单词，也可能比所有单词都长（测试 05）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1542_sorting.cpp](1542_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N + 15 N + M) | AC | 0.187 s | 11212 KB |
| [1542_sorting.go](1542_sorting.go) | Go 1.14 x64 | sorting | O(N log N + 15 N + M) | AC | 0.203 s | 11304 KB |
| [1542_sorting.java](1542_sorting.java) | Java 1.8 | sorting | O(N log N + 15 N + M) | AC | 0.468 s | 36636 KB |
| [1542_sorting.py](1542_sorting.py) | Python 3.12 x64 | sorting | O(N log N + 15 N + M) | AC | 0.593 s | 32604 KB |
| [1542_sorting.rs](1542_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N + 15 N + M) | AC | 0.093 s | 15136 KB |
