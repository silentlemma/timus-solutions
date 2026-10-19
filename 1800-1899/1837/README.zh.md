# 1837. 伊森巴耶夫数

[Timus 1837](https://acm.timus.ru/problem.aspx?space=1&num=1837) · 难度 60 · bfs

原题为民间流传的题目，出自 2011 年 4 月第十五届乌拉尔竞技编程公开锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

伊森巴耶夫数对 Vladislav Isenbaev 本人为 0，对 Isenbaev 的队友为 1，对队友的队友中没和 Isenbaev 同队过的人为 2，依此类推。
给出各支队伍，输出每名选手的数；若没有通往 Isenbaev 的队伍链，则输出 "undefined"。

## 输入

n（1 ≤ n ≤ 100），然后是 n 支队伍，每支三个姓氏（一个大写字母后接小写字母，至多 20 个字母）。Isenbaev 的姓氏是 "Isenbaev"。

## 输出

每名选手及其数，按姓氏排序。

## 样例

### 样例 1

输入：

```
7
Isenbaev Oparin Toropov
Ayzenshteyn Oparin Samsonov
Ayzenshteyn Chevdar Samsonov
Fominykh Isenbaev Oparin
Dublennykh Fominykh Ivankov
Burmistrov Dublennykh Kurpilyanskiy
Cormen Leiserson Rivest
```

输出：

```
Ayzenshteyn 2
Burmistrov 3
Chevdar 3
Cormen undefined
Dublennykh 2
Fominykh 1
Isenbaev 0
Ivankov 2
Kurpilyanskiy 3
Leiserson undefined
Oparin 1
Rivest undefined
Samsonov 2
Toropov 1
```

## 解法

在图中把同一支队伍的每两名成员连起来。所求的数就是到 Isenbaev 的距离，用广度优先搜索求出；搜索到不了的选手为 undefined。按排序后的顺序输出姓名。
选手至多 300 人，任何方法都很快。排序需要 `O(n log n)`。

在样例中 Oparin 与 Isenbaev 同队（1），Ayzenshteyn 与 Oparin 同队（2），Chevdar 与 Ayzenshteyn 同队（3），而 Cormen 的队伍是孤立的。

注意事项：

- 输入中可能没有 Isenbaev，此时所有人都是 undefined；
- 同一支队伍可能出现两次；
- 姓名按普通字符串比较，都以大写字母开头。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1837_bfs.cpp](1837_bfs.cpp) | G++ 13.2 x64 | bfs | O(n log n) | AC | 0.015 s | 552 KB |
| [1837_bfs.go](1837_bfs.go) | Go 1.14 x64 | bfs | O(n log n) | AC | 0.031 s | 1420 KB |
| [1837_bfs.java](1837_bfs.java) | Java 1.8 | bfs | O(n log n) | AC | 0.171 s | 4192 KB |
| [1837_bfs.py](1837_bfs.py) | Python 3.12 x64 | bfs | O(n log n) | AC | 0.093 s | 560 KB |
| [1837_bfs.rs](1837_bfs.rs) | Rust 1.75 x64 | bfs | O(n log n) | AC | 0.046 s | 468 KB |
