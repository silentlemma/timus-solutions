# 2068. 拆分次数的奇偶性

[Timus 2068](https://acm.timus.ru/problem.aspx?space=1&num=2068) · 难度 108 · games

原题作者 Alexey Danilyuk，出自 2015 年乌拉尔地区程序设计团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 n 堆坚果，每堆的个数都是奇数。两人轮流操作；一次操作把某一堆分成三个非空的堆，且每堆的个数仍为奇数。无法操作的人输。Daenerys 先手，Stannis 后手。求双方都采取最优策略时的胜者。时间限制 1 秒，内存限制 64 MB。

## 输入

奇数 n（1 ≤ n ≤ 777），然后是 n 个奇数堆大小，范围 1 到 54321。

## 输出

若 Daenerys 获胜输出 `Daenerys`，否则输出 `Stannis`。

## 样例

### 样例 1

输入：

```
1
3
```

输出：

```
Daenerys
```

### 样例 2

输入：

```
3
1 1 1
```

输出：

```
Stannis
```

### 样例 3

输入：

```
5
777 313 465 99 1
```

输出：

```
Daenerys
```

## 解法

这里策略无关紧要。一次操作把一堆换成三堆，所以堆数恰好增加 2，而坚果总数不变。游戏恰好在每堆只剩一个坚果时结束：3 个及以上（奇数个）坚果的堆总能分成 1 + 1 + (a − 2)。此时堆数等于坚果数，因此总操作次数恒为 (S − n) / 2，即各堆 (aᵢ − 1) / 2 之和。

Daenerys 走第奇数步，所以她获胜当且仅当这个数是奇数。第三个样例中各堆给出 388 + 156 + 232 + 49 + 0 = 825 步，是奇数。时间 O(n)。

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [2068_games.cpp](2068_games.cpp).

总和不超过 777 · 27160，32 位整数即可容纳；C++、Java 和 Rust 中仍用 64 位保存，
Go 的 `int` 在 x64 上也是 64 位。

## 解答

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2068_games.cpp](2068_games.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.015 s | 124 KB | 11294416 |
| [2068_games.go](2068_games.go) | Go 1.14 x64 | games | O(n) | AC | 0.031 s | 1108 KB | 11294420 |
| [2068_games.java](2068_games.java) | Java 1.8 | games | O(n) | AC | 0.109 s | 480 KB | 11304044 |
| [2068_games.py](2068_games.py) | Python 3.12 x64 | games | O(n) | AC | 0.093 s | 388 KB | 11304045 |
| [2068_games.rs](2068_games.rs) | Rust 1.75 x64 | games | O(n) | AC | 0.015 s | 256 KB | 11304046 |
