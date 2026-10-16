# 1804. 机枪手队的淘汰赛

[Timus 1804](https://acm.timus.ru/problem.aspx?space=1&num=1804) · 难度 411 · implementation

原题作者 Alex Samsonov，出自 NEERC 2010 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

两队进行一场主场和一场客场比赛。总进球多者晋级；总进球相同时，在对方球场进球多者晋级；若仍相同则抽签决定。一场比赛中一队最多进 30 球。
给定第一场比赛，求机枪手队在第二场中为保有晋级机会至少需要进几球，以及进球最多为几个时对手仍有晋级机会。

## 输入

t（1 ≤ t ≤ 200），然后是 t 行形如 "The Machinegunners played where game, scored x goals, and conceded y goals." 的句子，其中 where 为 home 或 away，0 ≤ x, y ≤ 30。

## 输出

每行输出两个数。

## 样例

### 样例 1

输入：

```
2
The Machinegunners played home game, scored 28 goals, and conceded 0 goals.
The Machinegunners played home game, scored 1 goals, and conceded 1 goals.
```

输出：

```
0 1
1 29
```

## 解法

枚举第二场的所有比分：机枪手队进 g 球、对手进 o 球，共 31 × 31 种。比较两队的 (总进球, 客场进球) 二元组。
若机枪手队的不小于对手的，就可能晋级；若不大于，就可能被淘汰，所以完全相同时两种结果都可能。第一个可能晋级的 g 和最后一个可能被淘汰的 g 就是答案。
若第一场在主场，客场进球分别是机枪手队的 g 和对手的 y，否则是 x 和 o。`O(t)`，每行 961 对。

第一行中主场 28:0 之后，即使客场 0:28 也是完全相同，所以进 0 球仍有机会。进 1 球时 1:30 仍会输，而进 2 球时最坏的 2:30 也能靠客场进球获胜。

注意事项：

- 两项都相同时由抽签决定，因此既算晋级的机会也算被淘汰的机会；
- 第二场决定哪一方的客场进球，取决于第一场在哪里进行；
- 一场比赛的比分最多为 30。

在 600 个随机的第一场比赛以及两种场地上所有极端和接近的比分上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1804_implementation.cpp](1804_implementation.cpp) | G++ 13.2 x64 | implementation | O(t) | AC | 0.031 s | 388 KB |
| [1804_implementation.go](1804_implementation.go) | Go 1.14 x64 | implementation | O(t) | AC | 0.015 s | 1216 KB |
| [1804_implementation.java](1804_implementation.java) | Java 1.8 | implementation | O(t) | AC | 0.109 s | 2600 KB |
| [1804_implementation.py](1804_implementation.py) | Python 3.12 x64 | implementation | O(t) | AC | 0.156 s | 520 KB |
| [1804_implementation.rs](1804_implementation.rs) | Rust 1.75 x64 | implementation | O(t) | AC | 0.015 s | 268 KB |
