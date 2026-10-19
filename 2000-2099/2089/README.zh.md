# 2089. 选出胜者使任何队伍不赢两次

[Timus 2089](https://acm.timus.ru/problem.aspx?space=1&num=2089) · 难度 949 · graphs, greedy

原题作者 Alexander Ipatov（由 Egor Shchelkonogov 整理）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

k 支队伍进行 n 场对局；每支队伍参加一到三场。为每场对局在其两支队伍中选出胜者，使任何队伍不赢两场，或说明这不可能。任何正确的选择都可接受。时间限制 2 秒，内存限制 256 MB。

## 输入

n 和 k（1 ≤ n ≤ 10⁵，2 ≤ k ≤ 10⁵），然后是 n 场对局。

## 输出

`Yes` 和按顺序的各场胜者，或 `No`。

## 评测方式

检查器只在期望输出为 `No` 时接受它，否则检查每个胜者都参加了该场对局并且只赢一次。

## 样例

### 样例 1

输入：

```
3 4
1 2
2 3
1 4
```

输出：

```
Yes
1
2
4
```

### 样例 2

输入：

```
6 4
1 2
1 3
1 4
2 3
2 4
3 4
```

输出：

```
No
```

## 解法

队伍是顶点，对局是边；选胜者就是把每条边指向它的一个端点，使每个顶点至多收到一条边。边数多于顶点数的连通部分做不到，边数不超过顶点数的部分可以：它是树，或者树加一条边，恰好有一个环。

构造时不断剥去叶子。只剩一场未决对局的队伍赢下它；这不会有任何坏处，因为这支队伍没有别的用处，而对局另一方的未决对局少了一场，可能随之成为叶子。没有叶子时，剩下的每支队伍有零场或至少两场未决对局。若某队仍有三场，它所在部分边太多，答案为 No。否则剩下的对局构成不相交的环，沿每个环走一圈，把每场对局交给它通向的队伍，于是环上每支队伍恰好赢一场。度数至多为三，整体 O(n + k)。

第二个样例中四支队伍进行六场对局，多于它们能赢的场数，所以答案为 No。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2089_graphs_greedy.cpp](2089_graphs_greedy.cpp) | G++ 13.2 x64 | graphs, greedy | O(n + k) | AC | 0.234 s | 6492 KB |
| [2089_graphs_greedy.go](2089_graphs_greedy.go) | Go 1.14 x64 | graphs, greedy | O(n + k) | AC | 0.109 s | 13268 KB |
| [2089_graphs_greedy.java](2089_graphs_greedy.java) | Java 1.8 | graphs, greedy | O(n + k) | AC | 0.250 s | 20632 KB |
| [2089_graphs_greedy.py](2089_graphs_greedy.py) | Python 3.12 x64 | graphs, greedy | O(n + k) | AC | 0.578 s | 51484 KB |
| [2089_graphs_greedy.rs](2089_graphs_greedy.rs) | Rust 1.75 x64 | graphs, greedy | O(n + k) | AC | 0.093 s | 13104 KB |
