# 1298. 马

[Timus 1298](https://acm.timus.ru/problem.aspx?space=1&num=1298) · 难度 234 · backtracking

原题为民间流传的题目（由 Den Raskovalov 准备），出自 2004 年 3 月 13 日第九届中学生公开团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

在 N × N 的棋盘上（1 ≤ N ≤ 8）找一条马的周游路线：由马步组成、恰好经过每个格子一次的路径。按顺序
输出各格（列用字母，行用数字）；若不存在周游，输出 `IMPOSSIBLE`。

时间限制：1 秒。内存限制：64 MB。

## 输入

数 N。

## 输出

N² 个格子，每行一个，或 `IMPOSSIBLE`。

## 评测方式

任何正确的周游都会被接受。检查程序读入 N² 个格子，确认它们互不相同、都在棋盘内，并且每个格子与前
一个相差一个马步。不存在周游时，输出必须恰好是 `IMPOSSIBLE`。

## 样例

### 样例 1

输入：

```
3
```

输出：

```
IMPOSSIBLE
```

### 样例 2

输入：

```
5
```

输出：

```
a1
c2
e1
d3
e5
c4
d2
e4
c5
a4
b2
d1
e3
d5
b4
a2
c1
e2
c3
b1
a3
b5
d4
b3
a5
```

## 解法

深度优先搜索一格一格地构造路径，走投无路时撤销一步，并依次尝试所有起点。单靠这种搜索在 8 × 8 棋盘
上可能非常慢，所以下一格按 Warnsdorff 规则的顺序尝试：先走下一步可去的空格最少的格子。这样死路很少
出现，而且出现得很晚。

按这个顺序，N 为 5 到 8 时搜索完全不需要回退：从 a1 出发恰好用 N² 次调用就找到周游。N = 2、3、4 时
没有周游，搜索通过尝试所有起点来证明这一点，N = 4 时需要 29 976 次调用。N = 1 就是单独的格子 a1。
规则排在后面的分支仍然会被尝试，所以答案是精确的，而不是启发式的猜测。

注意事项：

- N = 1 的周游只有一个格子 a1（测试 03）；
- 4 × 4 棋盘比 3 × 3 大，却没有周游（测试 05）；
- 周游不必是闭合的：最后一格不需要能一步回到第一格。

## 各语言说明

- 五种语言都用同样的稳定顺序处理相等的情况，因此输出相同的周游。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1298_backtracking.cpp](1298_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.015 s | 216 KB |
| [1298_backtracking.go](1298_backtracking.go) | Go 1.14 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.015 s | 4468 KB |
| [1298_backtracking.java](1298_backtracking.java) | Java 1.8 | backtracking | O(N^2) for N >= 5 | AC | 0.156 s | 7116 KB |
| [1298_backtracking.py](1298_backtracking.py) | Python 3.12 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.171 s | 544 KB |
| [1298_backtracking.rs](1298_backtracking.rs) | Rust 1.75 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.015 s | 244 KB |
