# 1269. 脏话过滤

[Timus 1269](https://acm.timus.ru/problem.aspx?space=1&num=1269) · 难度 847 · strings

原题作者 Pavel Atnashev，出自 2003 年 10 月 25 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给出 n ≤ 10 000 个禁用词（可含除 0、10、13 以外的任意字节，每个不超过 10 000，总共不超过
100 KB）和一段 m 行的文本（不超过 900 KB），求禁用词第一次作为子串出现的位置：行号以及
该词第一个字符在行中的位置。如果没有，输出 `Passed`。内存限制只有 8 MB。

时间限制：1 秒。内存限制：8 MB。

## 输入

n，然后每行一个词共 n 个，然后 m，然后文本的 m 行。

## 输出

行号和位置，或 `Passed`。

## 样例

### 样例 1

输入：

```
5
dear
sweetie
angel
dream
baby
8
Had I the heavens' embroidered cloths, 
Enwrought with golden and silver light, 
The blue and the dim and the dark cloths 
Of night and light and the half-light, 
I would spread the cloths under your feet: 
But I, being poor, have only my dreams; 
I have spread my dreams under your feet; 
Tread softly because you tread on my dreams.
```

输出：

```
6 33
```

## 解法

用这些词建立 Aho–Corasick 自动机。每个节点保存在此结束的最长单词的长度，包括沿失配链接
能到达的单词。把每一行送入自动机。读完第 i 个字节后，在此结束的最长单词从
i − longest + 1 开始，这是所有在 i 结束的单词中最早的起点。一行的答案是整行中这种起点的
最小值，第一个有匹配的行给出答案。

100 000 个节点时，每个节点 256 个孩子的表放不进 8 MB。所以先用“孩子—兄弟”链表建字典树，
再按广度优先顺序重新编号，使每个节点的孩子编号连续。这样查找孩子只需扫描一段很短的
字节（`memchr`、`bytes.IndexByte`、`bytearray.find`），失配链接也按同一顺序计算，链接
指向的节点总是更早出现。W 为单词字节数、T 为文本字节数、每个节点至多 σ = 255 个孩子时
为 `O(W + T · σ)`，实际中 σ 很小。

注意事项：

- 要的是最早的起点，而不是最早的终点：在 `xabcdefx` 中，从 2 开始的 `abcdef` 早于从 4
  开始的 `cd`（测试 02）；
- 单词可能含有空格、制表符和标点，所以不能把行切成记号（测试 03、07）；
- 沿失配链接得到的更长单词可能比在节点本身结束的单词起点更早，所以要保存最大长度，
  而不是任意一个；
- 行可能为空，一行也可能占据几乎整个文本（测试 06、gen7）。

在 60 个生成的数据上，与在每一行中逐个查找每个单词的结果比较过。

## 各语言说明

- 所有语言都在一维数组中建立同样的重新编号的字典树，并逐行读取文本。
- Java 直接从输入字节建立字典树，并且不保存文本的各行而是逐字节扫描：单词和各行的字符串放不
  进 8 MB。Python 读字节，并把数组放在 `array` 和 `bytearray` 中，以满足内存限制。
- Python 解答在评测的第 13 个测试上超时，保留并标记为 TLE：它通过了这里的全部测试，
  但不声称能在评测的每个测试上及时完成。PyPy 也不行，它的运行环境本身就需要超过
  允许的 8 MB。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1269_strings.cpp](1269_strings.cpp) | G++ 13.2 x64 | strings | O(W + T · σ) | AC | 0.062 s | 5952 KB |
| [1269_strings.go](1269_strings.go) | Go 1.14 x64 | strings | O(W + T · σ) | AC | 0.046 s | 6640 KB |
| [1269_strings.java](1269_strings.java) | Java 1.8 | strings | O(W + T · σ) | AC | 0.234 s | 3524 KB |
| [1269_strings.py](1269_strings.py) | Python 3.12 x64 | strings | O(W + T · σ) | TLE (test 13) | 1.015 s | 3564 KB |
| [1269_strings.rs](1269_strings.rs) | Rust 1.75 x64 | strings | O(W + T · σ) | AC | 0.125 s | 6048 KB |
