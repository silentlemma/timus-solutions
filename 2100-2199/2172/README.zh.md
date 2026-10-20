# 2172. 安排所有赞助商出现所需的最少题目数

[Timus 2172](https://acm.timus.ru/problem.aspx?space=1&num=2172) · 难度 761 · greedy, constructive

原题作者 Valentin Zuev，出自 2022 年乌拉尔团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

赞助商 i 希望恰好出现在 sᵢ 道不同的题目中，而每道题提到的不同赞助商不能超过 K 个。求最少的题目数 M，并给出列出每道题赞助商的方案。任何合法方案都可接受。时间限制 1 秒，内存限制 256 MB。

## 输入

N 和 K（1 ≤ N, K ≤ 1000），然后是 s₁ … s_N（1 ≤ sᵢ ≤ 1000），总和不超过 10⁵。

## 输出

M，然后对每道题给出其赞助商个数和编号。

## 评测方式

检查器核对 M，并验证方案满足所有愿望和限制。

## 样例

### 样例 1

输入：

```
5 2
1 1 1 1 1
```

输出：

```
3
1 5
2 2 3
2 4 1
```

## 解法

两个下界很明显：愿望最大的赞助商需要那么多道不同的题，而 S = Σ sᵢ 次提及至少需要 ⌈S / K⌉ 道题。所以 M ≥ max(max sᵢ, ⌈S / K⌉)，而且这么多就够了。

把所有提及按赞助商依次排成一行，再轮流分给各道题：第 t 次提及分给第 t mod M 道题。同一赞助商的提及是连续的且至多 M 次，所以落在不同的题目中。每道题至多得到 ⌈S / M⌉ ≤ K 次提及。工作量 O(S)。

样例中五个各有一个愿望的赞助商需要 ⌈5 / 2⌉ = 3 道题。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2172_greedy_constructive.cpp](2172_greedy_constructive.cpp) | G++ 13.2 x64 | greedy, constructive | O(S) | AC | 0.062 s | 3732 KB |
| [2172_greedy_constructive.go](2172_greedy_constructive.go) | Go 1.14 x64 | greedy, constructive | O(S) | AC | 0.031 s | 4724 KB |
| [2172_greedy_constructive.java](2172_greedy_constructive.java) | Java 1.8 | greedy, constructive | O(S) | AC | 0.156 s | 17408 KB |
| [2172_greedy_constructive.py](2172_greedy_constructive.py) | Python 3.12 x64 | greedy, constructive | O(S) | AC | 0.187 s | 18848 KB |
| [2172_greedy_constructive.rs](2172_greedy_constructive.rs) | Rust 1.75 x64 | greedy, constructive | O(S) | AC | 0.046 s | 8796 KB |
