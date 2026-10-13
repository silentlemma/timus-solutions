# 1455. 言论自由

[Timus 1455](https://acm.timus.ru/problem.aspx?space=1&num=1455) · 难度 2022 · shortest_paths

原题作者 Nikita Rybak、Ilya Grebnov 与 Dmitry Kovalioff，出自 Timus Top Coders: Second Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

词典中有 N 个不同的单词（1 ≤ N ≤ 100），每个由 1 到 100 个小写拉丁字母组成。改革
后，文本书写时不加分隔符。求一个不超过 20000 个字母、能以两种不同方式拆成词典单
词的文本；若不存在，输出 "NO"。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是 N 个单词。

## 输出

"NO"，或 "YES" 和文本。任何这样的文本都被接受。

## 样例

### 样例 1

输入:

```
5
ab
acb
bc
abac
babbc
```

输出:

```
YES
abacbabbc
```

文本 "abacbabbc" 既是 "abac" + "babbc"，也是 "ab" + "acb" + "ab" + "bc"。

## 解法

按 Sardinas–Patterson 判定的思路，把同一文本的两种拆分并排读。任何时刻，一种拆分
比另一种多出一段尾巴，而这段尾巴总是某个单词的后缀，所以状态至多 100 · 100 个。
搜索从每一对 u ≠ v、u 是 v 的前缀的单词出发，尾巴是 v 去掉 u 后的部分。从尾巴 t
出发，加到落后拆分上的单词 w 有三种情况：恰好与 t 一起结束，这就构成了有歧义的文
本；比 t 长且以 t 开头，于是另一种拆分落后 w 剩下的部分；是 t 的前缀，留下 t 剩下
的部分。

状态的代价是已写出文本的长度，只有落后的拆分超越时才会增长。在这些代价上运行
Dijkstra 算法能找到最短的有歧义文本，所以只要存在不超过限制的文本，找到的也不会
超过；文本沿着各段回溯到起始的单词对来重建。设 S 个状态、单词长 L，复杂度
`O(S · N · L log S)`。

注意事项：

- 单个单词、前缀码或后缀码没有有歧义的文本（测试 02、05、09、gen4、gen5）；
- 一种拆分可能连续领先许多步，所以搜索必须追踪尾巴，而不仅仅是单词对（测试 03、
  07）；
- 普通的广度优先搜索按步数而不是字母数计算，可能返回比需要更长的文本。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1455_shortest_paths.cpp](1455_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(S N L log S) | AC | 0.031 s | 3968 KB |
| [1455_shortest_paths.go](1455_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(S N L log S) | AC | 0.031 s | 3668 KB |
| [1455_shortest_paths.java](1455_shortest_paths.java) | Java 1.8 | shortest_paths | O(S N L log S) | AC | 0.156 s | 4448 KB |
| [1455_shortest_paths.py](1455_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(S N L log S) | AC | 0.218 s | 2884 KB |
| [1455_shortest_paths.rs](1455_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(S N L log S) | AC | 0.031 s | 2876 KB |
