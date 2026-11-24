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

## 优化解法

`1837_bfs_optimized.py`. 保留精确队友 BFS 及按姓排序输出。姓保留为 bytes，流式读队伍 token，用集合去重真实队友边；发现列表同时作 BFS 队列。合法队伍三人互异，不添加自边。断开者保留 undefined，无 Isenbaev 则不启动 BFS。有界姓名下图工作期望 O(V+E)，排序 O(V log V)；保留易读字符串版。

精确源代码 CPython 3.12 Accepted #11326689：0.078 s / 648 KB。2026-11-20 保存的当前语言族编译器组比较：时间排名 5/106，内存排名 31/106。低于 1024 KB，严格收录只看时间。

- `1837_bfs_optimized.py`: 0.078 s / 648 KB; 保留的教学基础版 `1837_bfs.py` (Python 3.12 x64): 0.093 s / 604 KB; 时间变化 -16.1%; 内存变化 +7.3%.

优化的 C++、Java 和 Rust 解法执行同样的广度优先搜索，但针对编号而不是名字。每个
名字第一次出现时得到一个编号，编号保存在有序映射中，以保证输出仍然有序；队友和距
离都是以这些编号为下标的普通数组，队列也是数组。C++ 用 `scanf` 把名字读入 21 字
节的缓冲区，Java 逐字节读取名字，并用 `int` 数组以链表形式保存队友，Rust 通过
`BufWriter` 输出。C++ 252 KB，而不是 552 KB，时间不变；Rust 264 KB，而不是
468 KB，时间不变；Java 0.109 s，而不是 0.171 s；656 KB，而不是 4192 KB。

优化的 Go 解法用 1 KB 缓冲的按词扫描器读取名字，而不是用 `fmt.Fscan`，并在哈希表
中给名字编号，因此图中存的是 `int` 而不是字符串，输出前再对名字排序：964 KB，而
不是 1420 KB，时间不变。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1837_bfs.cpp](1837_bfs.cpp) | G++ 13.2 x64 | bfs | O(n log n) | AC | 0.015 s | 552 KB | 11303519 |
| [1837_bfs.go](1837_bfs.go) | Go 1.14 x64 | bfs | O(n log n) | AC | 0.031 s | 1420 KB | 11290519 |
| [1837_bfs.java](1837_bfs.java) | Java 1.8 | bfs | O(n log n) | AC | 0.171 s | 4192 KB | 11290524 |
| [1837_bfs.py](1837_bfs.py) | Python 3.12 x64 | bfs | O(n log n) | AC | 0.093 s | 604 KB | 11303521 |
| [1837_bfs.rs](1837_bfs.rs) | Rust 1.75 x64 | bfs | O(n log n) | AC | 0.046 s | 468 KB | 11290528 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1837_bfs_optimized.cpp](1837_bfs_optimized.cpp) \* | G++ 13.2 x64 | bfs | O(n log n) | AC | 0.031 s | 252 KB | 11303641 |
| [1837_bfs_optimized.go](1837_bfs_optimized.go) | Go 1.14 x64 | bfs | O(n log n) | AC | 0.031 s | 964 KB | 11303796 |
| [1837_bfs_optimized.java](1837_bfs_optimized.java) | Java 1.8 | bfs | O(n log n) | AC | 0.109 s | 656 KB | 11303642 |
| [1837_bfs_optimized.rs](1837_bfs_optimized.rs) | Rust 1.75 x64 | bfs | O(n log n) | AC | 0.031 s | 264 KB | 11303643 |
| [1837_bfs_optimized.py](1837_bfs_optimized.py) | Python 3.12 x64 | bfs | O(n log n) | AC | 0.078 s | 648 KB | 11326689 |

\* 已通过评测；尚未达到单独排名目标：C++ 要求时间和内存均为前十或前 15%，其他语言类别要求两项均第一。此标记与收录条件分开，该版本仍可进一步优化。
