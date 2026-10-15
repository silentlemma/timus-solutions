# 1728. Team.GOV 的诅咒

[Timus 1728](https://acm.timus.ru/problem.aspx?space=1&num=1728) · 难度 526 · implementation

原题作者 Eugene Kurpilyansky（创意来自 Mikhail Rubinchik），出自 2009 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Efremov 和 Kantorov 从候选人名单中挑选第三名队员。队伍实力是队员评分之和。
如果选出的阵容曾在之前某次比赛中出场，Efremov 就不来；如果没有他的阵容也出场过，队伍被取消资格。
选出能让出场队伍最强的候选人，或者报告无论怎样选都会被取消资格。

## 输入

n（1 ≤ n ≤ 100）个以前的阵容，每个给出人数（1 到 3）和按字母序排列的姓氏；每个阵容都有 Kantorov，
每个三人阵容都有 Efremov。然后是 Efremov 和 Kantorov 的评分、m（1 ≤ m ≤ 100）以及 m 名候选人及其评分。
评分在 1 到 666 之间。

## 输出

`Win` 和一名使队伍最强的候选人，或者 `Fail`。任何最优候选人都可以。

## 样例

### 样例 1

输入：

```
6
3 Efremov Kantorov Rubinchik
2 Efremov Kantorov
3 Efremov Kantorov Kokovin
3 Burmistrov Efremov Kantorov
3 Efremov Kantorov Pervukhin
2 Kantorov Pervukhin
100 10
6
Fominykh 200
Komarov 34
Pervukhin 250
Golubev 23
Soboleva 50
Gein 50
```

输出：

```
Win
Fominykh
```

### 样例 2

输入：

```
2
3 Efremov Fominykh Kantorov
2 Fominykh Kantorov
99 666
1
Fominykh 100
```

输出：

```
Fail
```

## 解法

把以前的每个阵容存为姓氏集合。对每名候选人 c：如果 {Efremov, Kantorov, c} 是新的，三人都出场，实力为三个评分之和；
否则若 {Kantorov, c} 是新的，两人在没有 Efremov 的情况下出场；否则 c 不可用。
在剩下的候选人中取最强者，若没有则输出 `Fail`。`O(n + m)` 次集合查询。

样例 1 中 Fominykh 带来 100 + 10 + 200 = 310。Pervukhin 已与两人一起出场过，也与 Kantorov 单独出场过，所以那支队伍会被取消资格。

注意事项：

- 阵容按姓氏集合比较，而不是只看候选人：只与 Kantorov 一起出场过的候选人仍会让 Efremov 到场；
- Efremov 与 Kantorov 的两人阵容，或 Kantorov 单人阵容，永远不会与含候选人的阵容相同；
- 让 Efremov 不来的较强候选人，可能输给能让 Efremov 到场的较弱候选人。

检查程序重新计算每名候选人的实力，接受任何最优者。在 200 个随机数据上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1728_implementation.cpp](1728_implementation.cpp) | G++ 13.2 x64 | implementation | O(n + m) | AC | 0.031 s | 476 KB |
| [1728_implementation.go](1728_implementation.go) | Go 1.14 x64 | implementation | O(n + m) | AC | 0.031 s | 1156 KB |
| [1728_implementation.java](1728_implementation.java) | Java 1.8 | implementation | O(n + m) | AC | 0.140 s | 2172 KB |
| [1728_implementation.py](1728_implementation.py) | Python 3.12 x64 | implementation | O(n + m) | AC | 0.109 s | 548 KB |
| [1728_implementation.rs](1728_implementation.rs) | Rust 1.75 x64 | implementation | O(n + m) | AC | 0.046 s | 464 KB |
