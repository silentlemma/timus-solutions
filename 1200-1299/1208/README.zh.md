# 1208. 没有共同队员的传奇队伍最多有几支

[Timus 1208](https://acm.timus.ru/problem.aspx?space=1&num=1208) · 难度 214 · bitmask

原题作者 Leonid Volkov，出自 2002 年 3 月乌拉尔国立大学团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 `K ≤ 18` 支三人传奇队伍，有些程序员曾在其中多支队伍里。一名程序员只能为一支
队伍参赛，所以要求出能同时参赛的最多队伍数，即没有程序员同时属于其中两支队伍。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

`K`，然后是每支队伍的三个名字，每个最多 20 个小写字母。

## 输出

能参赛的最多队伍数。

## 样例

### 样例 1

输入：

```
7
gerostratos scorpio shamgshamg
zaitsev silverberg cousteau
zaitsev petersen shamgshamg
clipper petersen shamgshamg
clipper bakirelli vasiliadi
silverberg atn dolly
knuth dijkstra bellman
```

输出：

```
4
```

## 解法

两支队伍有共同队员时就冲突，答案是彼此不冲突的最大队伍集合。对每支队伍记录一个
位掩码，表示与它冲突的队伍（包括它自己）。对于用掩码表示的队伍集合，看其中编号
最小的队伍：要么它不参赛，剩下去掉它的集合；要么它参赛，剩下去掉它以及所有与它
冲突的队伍的集合。所以

`best(S) = max(best(S 去掉 i), 1 + best(S 去掉 clash(i)))`，`i` 是 `S` 中编号最小
的队伍。

两个更小的集合对应的数也更小，所以可以按递增顺序为全部 `2^K` 个掩码填表。
`O(2^K + K²)`。

注意事项：

- 一支队伍与自己冲突，这样选它时就会把它去掉；
- 同一名程序员可能在许多队伍里，所以冲突不只发生在列表中相邻的队伍之间。

答案已在 200 个随机输入以及从 3 到 1000 名程序员中抽取的队伍上与另一份独立解答
比对。

## 各语言说明

- Python 用 `functools.lru_cache` 惰性地计算同一个递推，只访问实际会出现的集合；
  其他语言填满整张表。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1208_bitmask.cpp](1208_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^K + K²) | AC | 0.015 s | 976 KB |
| [1208_bitmask.go](1208_bitmask.go) | Go 1.14 x64 | bitmask | O(2^K + K²) | AC | 0.062 s | 3204 KB |
| [1208_bitmask.java](1208_bitmask.java) | Java 1.8 | bitmask | O(2^K + K²) | AC | 0.109 s | 2688 KB |
| [1208_bitmask.py](1208_bitmask.py) | Python 3.12 x64 | bitmask | O(2^K + K²) | AC | 0.078 s | 456 KB |
| [1208_bitmask.rs](1208_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^K + K²) | AC | 0.046 s | 684 KB |
