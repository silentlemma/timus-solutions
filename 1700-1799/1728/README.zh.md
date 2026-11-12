# 1728. Team.GOV 的诅咒

[Timus 1728](https://acm.timus.ru/problem.aspx?space=1&num=1728) · 难度 524 · implementation

原题作者 Eugene Kurpilyansky（创意来自 Mikhail Rubinchik），出自 2009 年乌拉尔地区团体程序设计竞赛。

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

更简单的 C++/Go/Rust 只用两组第三人姓氏。历史队伍必有 Kantorov，三人队还必有 Efremov，因此第三姓氏唯一决定相关二人/三人组。三人记录入 full，二人入 pairs；单独 Kantorov 及 Efremov/Kantorov 二人组与候选无关。不在 full 则强度 re+rk+r；在 full 不在 pairs 则 rk+r；都在则取消资格，选择任一最高分候选。全姓氏比较且区分大小写。期望时间 O((n+m)L)、L≤50，集合空间 O(nL)。原通用方法排序最多三个姓氏作完整队伍键，先查三人，重复则去掉 Efremov 再查二人。保留原五种 Accepted，Java/Python 仍以此为基础版。

## 优化解法

Go 快速版使用相同的两个姓氏集合、标准句柄、固定输入输出缓冲区以及 50 字节单词缓冲区。 Rust 快速版通过 C 标准输入读取姓氏，在一张固定大小的开放寻址表中存储两种队伍标志。哈希冲突时比较完整姓氏。 C++ 的姓氏集合实现也覆盖快速版本。Java 和 Python 复用已达标的原程序。旧 C++、Go 和 Rust 的完整队伍实现列在其他已通过方法中。星号表示快速源码尚未达到该语言的排名目标。

已通过评测的基础实现 [1728_implementation.java](1728_implementation.java), [1728_implementation.py](1728_implementation.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

C++ 的 unordered_set 持有姓氏字符串。Go 扫描单词并用两个映射，姓氏最长 50 字符。Rust 用 O((n+m)L) 空间保留输入并借用其中的姓氏切片。哈希复杂度为期望值。原 Java/Python 保留完整规范队伍，其实际 Accepted 编译器/解释器及指标不变。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1728_hashing.cpp](1728_hashing.cpp) | G++ 13.2 x64 | hashing | O((n + m)L) | AC | 0.015 s | 204 KB | 11315520 |
| [1728_hashing.go](1728_hashing.go) | Go 1.14 x64 | hashing | O((n + m)L) | AC | 0.031 s | 952 KB | 11315664 |
| [1728_implementation.java](1728_implementation.java) \* | Java 1.8 | implementation | O(n + m) | AC | 0.140 s | 2172 KB | 11289394 |
| [1728_implementation.py](1728_implementation.py) \* | Python 3.12 x64 | implementation | O(n + m) | AC | 0.109 s | 548 KB | 11289392 |
| [1728_hashing.rs](1728_hashing.rs) | Rust 1.75 x64 | hashing | O((n + m)L) | AC | 0.031 s | 420 KB | 11315666 |

### 其他 Accepted 实现

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1728_implementation.cpp](1728_implementation.cpp) | G++ 13.2 x64 | implementation | O((n + m) log n) | AC | 0.031 s | 476 KB | 11289389 |
| [1728_implementation.go](1728_implementation.go) | Go 1.14 x64 | implementation | O(n + m) | AC | 0.031 s | 1156 KB | 11289390 |
| [1728_implementation.rs](1728_implementation.rs) | Rust 1.75 x64 | implementation | O(n + m) | AC | 0.046 s | 464 KB | 11289397 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1728_hashing_optimized.go](1728_hashing_optimized.go) \* | Go 1.14 x64 | hashing | O((n + m)L) | AC | 0.031 s | 320 KB | 11315884 |
| [1728_hashing_optimized.rs](1728_hashing_optimized.rs) \* | Rust 1.75 x64 | hashing | O((n + m)L) | AC | 0.031 s | 60 KB | 11315888 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
