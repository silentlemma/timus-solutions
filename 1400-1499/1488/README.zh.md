# 1488. ACM 扑克

[Timus 1488](https://acm.timus.ru/problem.aspx?space=1&num=1488) · 难度 1536 · implementation

原题作者 Vladimir Yakovlev，出自 2006 年 10 月 7 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

两名玩家各发三张牌。Dima 可以偷偷用袖中的两张牌换掉自己的一张或两张牌，但不会拿
出与 Sasha 某张牌相同的牌，也不会让自己手里出现两张相同的牌。牌型从大到小：三张
3、同花顺、三条、顺子、同花、对子、高牌。牌型相同或双方都没有对子时，从最大的点
数开始依次比较；对子先比对子的点数，再比单张。A 最大，A-2-3 和 K-A-2 不算顺子。
对每局游戏，若 Dima 能赢则输出 "Dima"；若只能打平则输出 "Artyom"（平局时钱归发牌
人）；否则输出 "Sasha"。

时间限制：1 秒。内存限制：64 MB。

## 输入

各局游戏以空行分隔：Sasha 的三张牌、Dima 的三张牌和袖中的两张牌，写法如 10H 或
QS。

## 输出

每局一个名字。

## 样例

### 样例 1

输入:

```
4C AC 2C
4S KD 6H
5C KH

JS 8H JC
8C 8D 10H
8H 10H

10D 8D 9D
3D 3C 3H
AH AS

2C 3D 4H
2D 3H 4S
AH AH
```

输出:

```
Dima
Sasha
Dima
Artyom
```

## 解法

Dima 至多有十种手牌可选：原手牌；三张牌中的任意一张换成任意一张袖中牌；保留一张
原牌并用上两张袖中牌。先去掉与 Sasha 的牌相同的袖中牌，有两张相同牌的手牌直接跳
过。

给每手牌一个与牌力同序的键：牌型编号，再跟上用于决胜的点数。点数从大到小；对子
则先是对子的点数，再是单张的点数。三张 3 不需要别的信息。若某个键大于 Sasha 的键
则 Dima 赢，若有相等的则平局，否则输。每局 `O(1)`。

注意事项：

- A-2-3 和 K-A-2 不是顺子，Q-K-A 是（测试 02）；
- 袖中可能有 Sasha 的牌、Dima 自己某张牌的副本或两张相同的牌，它们都不能以被禁止
  的方式使用（测试 01、02、gen3）；
- 三张 3 甚至大于最大的同花顺（测试 01、02）；
- 键相等就是平局，即使花色不同（测试 02、gen2）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1488_implementation.cpp](1488_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) per game | AC | 0.001 s | 428 KB |
| [1488_implementation.go](1488_implementation.go) | Go 1.14 x64 | implementation | O(1) per game | AC | 0.031 s | 5896 KB |
| [1488_implementation.java](1488_implementation.java) | Java 1.8 | implementation | O(1) per game | AC | 0.156 s | 6824 KB |
| [1488_implementation.py](1488_implementation.py) | Python 3.12 x64 | implementation | O(1) per game | AC | 0.203 s | 2232 KB |
| [1488_implementation.rs](1488_implementation.rs) | Rust 1.75 x64 | implementation | O(1) per game | AC | 0.015 s | 1256 KB |
