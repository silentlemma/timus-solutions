# 1644. 一大堆核桃

[Timus 1644](https://acm.timus.ru/problem.aspx?space=1&num=1644) · 难度 100 · implementation

原题作者 Alexey Samsonov，出自 2008 年 10 月的乌拉尔国立大学中学生竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

鹦鹉做了 n 次实验，每次吃 3 到 9 个核桃，并记下自己是还饿还是吃饱了。饱足是单调的：吃得更多绝不会
更饿。已知十个核桃一定能吃饱，两个一定吃不饱。求一定能吃饱的最少核桃数，或指出记录互相矛盾。

## 输入

n（0 ≤ n ≤ 100），然后 n 行：核桃数以及 `hungry` 或 `satisfied`。

## 输出

一定能吃饱的最少核桃数，或 `Inconsistent`。

## 样例

### 样例 1

输入：

```
4
4 hungry
7 satisfied
5 hungry
8 satisfied
```

输出：

```
7
```

### 样例 2

输入：

```
2
6 hungry
5 satisfied
```

输出：

```
Inconsistent
```

## 解法

取“饿”的最大数量（从 2 开始）和“饱”的最小数量（从 10 开始）。当且仅当后者更大时，记录与一个单调
阈值相符；此时答案就是“饱”的最小数量，因为更少的数量从未被证明能吃饱。否则输出 `Inconsistent`。
`O(n)`。

易错点：

- 没有记录时答案是 10（测试 03），只有“饿”的记录时答案仍是 10（测试 04）；
- 同一数量既记为饿又记为饱就是矛盾（测试 06）。

在 180 组随机记录上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1644_implementation.cpp](1644_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 392 KB |
| [1644_implementation.go](1644_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1084 KB |
| [1644_implementation.java](1644_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1708 KB |
| [1644_implementation.py](1644_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 444 KB |
| [1644_implementation.rs](1644_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 220 KB |
