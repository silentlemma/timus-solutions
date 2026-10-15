# 1636. 罚时

[Timus 1636](https://acm.timus.ru/problem.aspx?space=1&num=1636) · 难度 60 · implementation

原题作者 Alex Samsonov，出自第十三届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

QXX 和 ZZZ 两队都做出了全部十道题；QXX 以罚时 T1 胜过 ZZZ 的 T2。每次被拒的提交加 20 分钟。
给出 ZZZ 在每道题上被拒的次数，判断没有这些罚时 ZZZ 能否获胜。罚时相同时按队名排序，所以 ZZZ
仍会是第二。

## 输入

第一行为 T1 和 T2（250 ≤ T1 ≤ T2 ≤ 2400），然后是 ZZZ 在十道题上被拒的次数。

## 输出

若这些被拒的提交让 ZZZ 失去第一，输出 `Dirty debug :(`，否则输出 `No chance.`。

## 样例

### 样例 1

输入：

```
290 420
0 0 0 2 1 0 2 0 1 0
```

输出：

```
No chance.
```

### 样例 2

输入：

```
300 719
0 0 0 0 0 0 21 0 0 0
```

输出：

```
Dirty debug :(
```

## 解法

从 T2 中按每次被拒减去 20 分钟。只有严格少于 T1 时 ZZZ 才能获胜，因为平局时 QXX 按字母序在前。
`O(1)`。

易错点：

- 去掉罚时后相等仍然是输（测试 03），少一分钟就是赢（测试 04）；
- 答案末尾的句点和哭脸都是期望输出的一部分。

在 100 个随机测试上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1636_implementation.cpp](1636_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 120 KB |
| [1636_implementation.go](1636_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB |
| [1636_implementation.java](1636_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1600 KB |
| [1636_implementation.py](1636_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 428 KB |
| [1636_implementation.rs](1636_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 236 KB |
