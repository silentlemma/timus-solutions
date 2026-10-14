# 1571. 翻译

[Timus 1571](https://acm.timus.ru/problem.aspx?space=1&num=1571) · 难度 451 · constructive

原题作者 Sergey Pupyrev，出自 2007 年 10 月 6 日第十二届乌拉尔国立大学程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N ≤ 100 个施工队各说一种语言。一名翻译可以懂任意两种语言。任意两个队都必须能交谈，而且不能有别的队听懂他们
的谈话。输出最少的翻译人数及各自的语言（格式为 `lang1-lang2`），或输出 `Impossible`。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是每个队的语言。

## 输出

翻译人数及其语言对，或 `Impossible`。任何最优的方案都被接受。

## 样例

### 样例 1

输入:

```
3
russian
french
german
```

输出:

```
3
russian-english
english-german
english-french
```

## 解法

如果两个队语言相同，那么只要还有第三个队，它就无法在第二个队听不懂的情况下与第一个队交谈；若只有这两个队，
就不需要翻译。否则设 k 种语言互不相同。一个队不需要翻译，两个队需要一名懂这两种语言的翻译。

当 k ≥ 3 时，经过另一个队语言的谈话会被那个队听到，所以任意两个队之间的翻译必须连成一条链，链的中间语言都
不是任何队的语言。如果翻译只用各队的语言，他们会在这 k 种语言上构成连通图，只有 k − 1 条边时就是一棵树，
其中某条链会经过第三种语言。所以需要 k 名翻译，而 k 名也够了：把每个队的语言与一种没人说的语言（例如
english）配对。若有队说 english，中间语言就用第一个空闲的一或两个字母的名字：输出中的语言也不能超过十个字母，而 100 个队占不满全部 702 个这样的名字。
`O(N)`。

注意事项：

- 同一语言的两个队不需要翻译，但三个队中有重复语言就不可能（测试 03、05）；
- 某个队本身可能说 english，而更长的自造中间语言名不被接受（测试 06、08）；
- 其他答案也被接受，例如三个队时用三对直接翻译构成三角形，所以检查器检验保密性。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1571_constructive.cpp](1571_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 436 KB |
| [1571_constructive.go](1571_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 1144 KB |
| [1571_constructive.java](1571_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.156 s | 1712 KB |
| [1571_constructive.py](1571_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 548 KB |
| [1571_constructive.rs](1571_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 456 KB |
