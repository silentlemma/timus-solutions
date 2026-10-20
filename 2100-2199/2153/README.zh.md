# 2153. 由不同职业组成的最大队伍以及哪种新人有帮助

[Timus 2153](https://acm.timus.ru/problem.aspx?space=1&num=2153) · 难度 960 · dp, bitmask

原题作者 Valentin Zuev，出自 2020 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

公会的 n 名成员每人拥有战士、法师、牧师、盗贼四种资质中的一个非空子集。一支队伍给不同的成员分配各自资质中不同的职业。求最大的队伍；若人数少于四人，列出这样的资质：雇用一个只有该资质的人能使最大队伍变大。时间限制 0.5 秒，内存限制 256 MB。

## 输入

n（1 ≤ n ≤ 15），然后是每名成员的资质，为 "WMCR" 的子序列。

## 输出

最大人数；若小于 4，再输出一行 "Looking for"，资质按 warrior、mage、cleric、rogue 的顺序给出。

## 样例

### 样例 1

输入：

```
1
W
```

输出：

```
1
Looking for mage cleric rogue
```

### 样例 2

输入：

```
2
M
CR
```

输出：

```
2
Looking for warrior cleric rogue
```

### 样例 3

输入：

```
4
WMCR
WMCR
WMCR
WMCR
```

输出：

```
4
```

### 样例 4

输入：

```
1
WMCR
```

输出：

```
1
Looking for warrior mage cleric rogue
```

## 解法

职业集合只有 16 种。对成员做动态规划，记录哪些职业集合能由不同的人填满：成员要么不参加，要么占用集合中一个空闲职业。在一名成员的这一步中按集合递减的顺序处理，可以防止同一成员占用两个职业。最大的可达集合就是最大队伍。

只有资质 r 的新人能使队伍变大，当且仅当存在某个最大集合不使用 r：这个集合加上新人更大；而若每个最大集合都用到 r，那么更大的队伍中会包含一个不含 r、大小为原最大值的可达集合，矛盾。所以招聘启事列出不在所有最大可达集合交集中的职业。工作量 O(16 · 4 · n)。

第二个样例中最大的队伍是 {法师, 牧师} 和 {法师, 盗贼}；它们的交集是 {法师}，所以需要战士、牧师和盗贼。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2153_dp_bitmask.cpp](2153_dp_bitmask.cpp) | G++ 13.2 x64 | dp, bitmask | O(64 n) | AC | 0.015 s | 448 KB |
| [2153_dp_bitmask.go](2153_dp_bitmask.go) | Go 1.14 x64 | dp, bitmask | O(64 n) | AC | 0.031 s | 1168 KB |
| [2153_dp_bitmask.java](2153_dp_bitmask.java) | Java 1.8 | dp, bitmask | O(64 n) | AC | 0.078 s | 392 KB |
| [2153_dp_bitmask.py](2153_dp_bitmask.py) | Python 3.12 x64 | dp, bitmask | O(64 n) | AC | 0.109 s | 640 KB |
| [2153_dp_bitmask.rs](2153_dp_bitmask.rs) | Rust 1.75 x64 | dp, bitmask | O(64 n) | AC | 0.046 s | 244 KB |
