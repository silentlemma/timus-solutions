# 1711. 代号

[Timus 1711](https://acm.timus.ru/problem.aspx?space=1&num=1711) · 难度 135 · greedy

原题作者 Alex Samsonov，由 Igor Chevdar 整理，出自 NEERC 2009 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 道题中每道都有三个候选代号，题目在题集中按代号的字典序排列。为每道题选一个代号，使题目按给定的顺序排列，
或者报告无法做到。

## 输入

n（1 ≤ n ≤ 16），然后 n 行，每行是一道题的三个代号：由小写字母组成，长度至多 20，所有代号互不相同。
最后一行是要求的顺序，即 1 … n 的一个排列。

## 输出

按要求的顺序输出所选的代号，每行一个，或者输出 IMPOSSIBLE。任何正确的选择都可以。

## 样例

### 样例 1

输入：

```
11
cipher grille kamkohob
names codenames codes
newtests rejudge timus
size volume summit
watchmen braineater twosides
solution random yesorno
keywords subversion commands
bosses shooting shaitan
game strategy playgame
mnemonic palindromes bestname
eligibility rectangle rules
2 1 7 10 9 6 11 3 8 4 5
```

输出：

```
codenames
grille
keywords
mnemonic
playgame
random
rectangle
rejudge
shaitan
volume
watchmen
```

### 样例 2

输入：

```
3
problems in the
first sample are
ordered not randomly
1 2 3
```

输出：

```
IMPOSSIBLE
```

## 解法

按要求的顺序依次处理，给每道题选它的代号中排在前一个所选代号之后的最小者；若没有这样的代号，答案为 IMPOSSIBLE。

这种贪心是安全的。假设存在某个正确的选择，逐题与贪心比较。由归纳法，贪心的代号永远不晚于正确的代号：
下一题的正确代号排在正确的前一个代号之后，因此也排在贪心的前一个代号之后，所以它是候选之一，
而贪心选出的不大于它。于是贪心过程永远不会卡住。`O(n)` 次短字符串比较。

注意事项：

- 代号按字符串比较，前缀排在前面："code" 在 "codenames" 之前；
- 顺序行按题集中的位置列出题号，而不是每道题的位置；
- 任何正确答案都可以，所以测试使用检查程序。

检查程序验证每个代号属于对应的题目，并且代号递增。在 600 个随机题集上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1711_greedy.cpp](1711_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 400 KB |
| [1711_greedy.go](1711_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.062 s | 1148 KB |
| [1711_greedy.java](1711_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.140 s | 516 KB |
| [1711_greedy.py](1711_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.093 s | 456 KB |
| [1711_greedy.rs](1711_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.046 s | 236 KB |
