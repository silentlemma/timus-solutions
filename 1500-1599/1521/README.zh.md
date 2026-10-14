# 1521. 军事演习 2

[Timus 1521](https://acm.timus.ru/problem.aspx?space=1&num=1521) · 难度 121 · fenwick

原题作者 Ilya Grebnov、Nikita Rybak 与 Dmitry Kovalioff，出自 Timus Top Coders: Third Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

编号 1 到 N 的 N 名士兵（1 ≤ N ≤ 100000）围成一圈行进。每一轮有一名士兵离开：先是第
K 名（1 ≤ K ≤ N），之后每次是上一个离开者前方第 K 位的士兵，只数仍在行进的人。按离
开的顺序输出士兵编号。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 K。

## 输出

按离开顺序排列的士兵编号。

## 样例

### 样例 1

输入:

```
5 3
```

输出:

```
3 1 5 2 4
```

## 解法

把仍在行进的士兵沿圈依次编为 0, 1, …。若上一个离开者在其中排第 r，那么下一个排第
(r + K − 1) mod（剩余人数），因为离开者的位置由紧跟其后的士兵补上。树状数组中每个仍在行
进的士兵记 1；按 2 的幂下降可在 `O(log N)` 内找到给定排名的士兵，删除则是单点修改。
总计 `O(N log N)`。

注意事项：

- 从普通列表中删除每轮要 `O(N)`，总计 `O(N²)`，对 100000 名士兵太慢（gen1）；
- K = 1 时士兵按顺序离开（测试 03、gen5）；
- K = N 时最后一名士兵先离开（测试 04、gen4）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1521_fenwick.cpp](1521_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(N log N) | AC | 0.031 s | 2136 KB |
| [1521_fenwick.go](1521_fenwick.go) | Go 1.14 x64 | fenwick | O(N log N) | AC | 0.062 s | 2460 KB |
| [1521_fenwick.java](1521_fenwick.java) | Java 1.8 | fenwick | O(N log N) | AC | 0.171 s | 5016 KB |
| [1521_fenwick.py](1521_fenwick.py) | Python 3.12 x64 | fenwick | O(N log N) | AC | 0.640 s | 12028 KB |
| [1521_fenwick.rs](1521_fenwick.rs) | Rust 1.75 x64 | fenwick | O(N log N) | AC | 0.031 s | 2512 KB |
