# 1866. 诗的音步

[Timus 1866](https://acm.timus.ru/problem.aspx?space=1&num=1866) · 难度 752 · parsing

原题作者 Alex Samsonov，出自 2011 年乌拉尔联邦大学开放团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

音步是一组音节，其中一个重读。扬抑格（trochee）和抑扬格（iamb）的音步有两个音节，分别重读第一和第二个；扬抑抑格（dactyl）、抑扬抑格（amphibrach）和抑抑扬格（anapaest）的音步有三个音节，分别重读第一、第二和第三个。诗的每一行由同一种音步连成，最后一个音步可以不完整。单词的音节用连字符连接，重读音节写在方括号里。求出诗的格律，或者输出 "not a poem"。

## 输入

n（2 ≤ n ≤ 100），然后是 n 行，每行不超过 50 个字符且至少有四个音节，只含拉丁字母、空格、连字符和方括号。

## 输出

"trochee"、"iamb"、"dactyl"、"amphibrach"、"anapaest" 或 "not a poem"。

## 样例

### 样例 1

输入：

```
4
My [un]-cle [high] i-[deals] ins-[pire] him
But [when] past [jo]-king [he] fell [sick]
he [real]-ly [forced] one [to] ad-[mire] him
and [ne]-ver [played] a [shrew]-der [trick]
```

输出：

```
iamb
```

## 解法

把每一行按空格和连字符切成音节，标出含有方括号的音节。音步有 k 个音节、重读在第 p 位的格律适合一行，当且仅当第 i 个音节（从 0 开始）恰在 i mod k = p − 1 时重读。不完整的最后一个音步不影响判断，因为只有音步内部的位置才重要。答案是适合所有行的第一个格律；每行至少四个音节时，任意两种格律给出的标记都不同，所以检查顺序无关紧要。总共 L 个字符时为 `O(L)`。

样例中每一行都重读第 2、4、6、8 个音节，这就是抑扬格。

注意事项：

- 每个音节都必须吻合，非重读音节也一样：重读位置上的非重读音节会破坏格律；
- 单词之间可能有多个空格，所以要跳过空片段；
- "not a poem" 是三个单词，输出必须一字不差。

在 300 首随机诗上答案与一个独立的已通过实现一致，其中 120 首在一个音节或一行上被破坏。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1866_parsing.cpp](1866_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 432 KB |
| [1866_parsing.go](1866_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.031 s | 1156 KB |
| [1866_parsing.java](1866_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.125 s | 1132 KB |
| [1866_parsing.py](1866_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.078 s | 480 KB |
| [1866_parsing.rs](1866_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.046 s | 240 KB |
