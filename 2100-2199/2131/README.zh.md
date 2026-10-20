# 2131. 随时间变化：含于所有标记名称而不含于其他名称的最短子串

[Timus 2131](https://acm.timus.ru/problem.aspx?space=1&num=2131) · 难度 5575 · suffix_structures

原题作者 Mikhail Rubinchik（由 Alexander Kulkov 整理），出自 “迟到总比不到好”专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

队名逐个出现在排行榜上；其中一些带有 "+"，表示是教练的队伍，第一个名称是被标记的最喜爱的队伍。每出现一个新名称后，求一个最短的字符串，它出现在当前所有被标记的名称中，且不出现在当前任何未标记的名称中，并以它在最喜爱队名中的一次出现的位置 l … r 输出；最短的有多个时取 l 最小的，若不存在则输出 "−1 −1"。时间限制 2 秒，内存限制 256 MB。

## 输入

n，然后是按出现顺序给出的 n 个互不相同的名称，由小写字母和 "_" 组成，被标记的名称后面有 "+"；总长度不超过 2 · 10⁵。

## 输出

每个名称出现后的 l 和 r，或者 −1 −1。

## 样例

### 样例 1

输入：

```
6
mit_kotiki+
sjtu_koty+
itmo_first
msu_koshki
mipt_alot
spbsu_kot
```

输出：

```
0 0
2 2
4 4
5 6
4 6
-1 -1
```

## 解法

每个候选都是最喜爱队名的子串。一个子串从一开始就合法，直到以下两个时刻之一：出现第一个包含它的未标记名称，或者出现第一个不包含它的标记名称。所以每个子串都有一个失效时刻，名称 t 出现后的答案就是失效时刻晚于 t 的最优子串。

把所有名称一起建成后缀自动机，子串被分成若干状态，同一状态中的字符串恰好出现在相同的名称里。对每个状态沿后缀链接子树汇总：

- 在最喜爱队名中最早的结束位置（如果出现在那里）；
- 第一个包含它的未标记名称；
- 包含它的标记名称集合（小集合并入大集合），以及集合中缺失的最小编号，这个编号向根方向只会增大。

一个状态的最优字符串是其中最短的那个，长度比其后缀链接的长度大一，结束于最喜爱队名中最早的位置。把它记在该状态的失效时刻下，再按时刻取后缀最小值，即可读出每个时刻的答案。总长度为 S 时工作量 O(S log S)，主要花在集合合并上。

样例中第一个答案是一个字母 "m"，即最喜爱队名的开头；"itmo_first" 出现后，最短的选择变成位置 4 上的 "k"，之后是 "ot" 和 "kot"；"spbsu_kot" 出现后就没有可行的字符串了。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2131_suffix_structures.cpp](2131_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(S log S) | AC | 0.343 s | 80288 KB |
| [2131_suffix_structures.go](2131_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(S log S) | AC | 0.328 s | 110800 KB |
| [2131_suffix_structures.java](2131_suffix_structures.java) | Java 1.8 | suffix_structures | O(S log S) | AC | 0.421 s | 93620 KB |
| [2131_suffix_structures.py](2131_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(S log S) | AC | 1.609 s | 148908 KB |
| [2131_suffix_structures.rs](2131_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(S log S) | AC | 0.218 s | 73324 KB |
