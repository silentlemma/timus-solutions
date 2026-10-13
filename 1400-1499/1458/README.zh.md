# 1458. 军事演习

[Timus 1458](https://acm.timus.ru/problem.aspx?space=1&num=1458) · 难度 1221 · constructive

原题作者 Dmitry Kovalioff、Nikita Rybak 与 Ilya Grebnov，感谢 Sergey Sofronov 提供构思，出自 Timus Top Coders: Second Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N × N 的阅兵场（N 为偶数，2 ≤ N ≤ 1000）每个格子里站着一名士兵，处于 W 或 B 两种
姿势之一。口令“格子 (i, j)”让第 i 行或第 j 列的所有士兵（共 2N − 1 人）换成另一种
姿势。求最短的口令序列，使执行后所有士兵姿势相同，哪一种都可以。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后 N 行，每行 N 个字母 W 或 B。

## 输出

口令数，然后是各口令的格子。任何最短的序列都被接受。

## 样例

### 样例 1

输入:

```
4
WBWB
BWWW
WWBW
WBWB
```

输出:

```
2
2 3
3 1
```

## 解法

口令可以交换顺序，重复的口令互相抵消，所以解就是一个格子集合。若对第 a 行和第 b
列的所有格子都下口令，(a, b) 的士兵换 2N − 1 次，该行或该列的其他士兵各换 N 次，
其余士兵各换 2 次；N 为偶数时只有 (a, b) 改变。因此可以单独切换任何一名士兵；要让
所有人变成 W，就要切换所有姿势为 B 的士兵：把这些士兵的“十字”叠加，格子 (i, j) 在第 i
行、第 j 列和格子本身中 B 的总数为奇数时要下口令。既然每名士兵都能单独切换，
2^(N²) 个格子集合就能得到全部 2^(N²) 种局面，没有两个集合效果相同，所以每个目标
只有这一个集合。

要让所有人变成 B，恰好需要其余的格子，因为全体格子的集合会切换所有人。所以取两个
集合中较小的那个：k 或 N² − k 条口令。`O(N²)`。

注意事项：

- 所有人已经姿势相同（无论哪一种）时不需要口令（测试 02、03）；
- N ≥ 4 时，只有一名士兵不同时需要由 2N − 1 条口令组成的十字（测试 07、gen2）；
- 多达五十万条口令必须快速输出（gen1、gen3、gen4）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1458_constructive.cpp](1458_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.218 s | 5236 KB |
| [1458_constructive.go](1458_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.078 s | 15380 KB |
| [1458_constructive.java](1458_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.218 s | 25812 KB |
| [1458_constructive.py](1458_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.453 s | 42840 KB |
| [1458_constructive.rs](1458_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.062 s | 7264 KB |
