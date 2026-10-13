# 1377. 劳拉·克劳馥

[Timus 1377](https://acm.timus.ru/problem.aspx?space=1&num=1377) · 难度 296 · simulation

原题作者 Stanislav Vasiliev，出自 2005 年 4 月 19–24 日在叶卡捷琳堡举行的第九届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

墓地有 N 排、每排 M 座墓，2 ≤ N, M ≤ 100。Lara 每晚挖到一座墓下，从 (1, 1) 开始向东：下一座墓完好就一直向前，遇到墙
或已挖过的墓就右转。两座给定的墓里有宝藏，Lara 刚刚找到其中之一。输出再过多少个夜晚会找到另一个。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 M，然后是两座有宝藏的墓 (r₁, c₁) 和 (r₂, c₂)。

## 输出

两次发现之间相隔的夜晚数。

## 样例

### 样例 1

输入：

```
5 4
2 2
5 3
```

输出：

```
6
```

## 解法

地道就是与 [1364](../1364/README.zh.md) 相同的顺时针螺旋。把它整个挖出来，按被挖的夜晚给每座墓编号，并在墓地四周放
一圈“已挖”的格子代替墙。答案是两个编号之差的绝对值，因为哪个宝藏先被找到都有可能。`O(N · M)`。

注意事项：

- 宝藏可能以任意顺序给出（测试 03）；
- 100 × 100 墓地的第一座和最后一座墓相隔 9 999 个夜晚（测试 04）；
- 两列的墓地中，螺旋沿一列向下，再沿另一列向上（测试 07）。

## 各语言说明

- 五种解答挖的是同样的螺旋。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1377_simulation.cpp](1377_simulation.cpp) | G++ 13.2 x64 | simulation | O(N·M) | AC | 0.001 s | 256 KB |
| [1377_simulation.go](1377_simulation.go) | Go 1.14 x64 | simulation | O(N·M) | AC | 0.046 s | 1172 KB |
| [1377_simulation.java](1377_simulation.java) | Java 1.8 | simulation | O(N·M) | AC | 0.109 s | 1640 KB |
| [1377_simulation.py](1377_simulation.py) | Python 3.12 x64 | simulation | O(N·M) | AC | 0.093 s | 924 KB |
| [1377_simulation.rs](1377_simulation.rs) | Rust 1.75 x64 | simulation | O(N·M) | AC | 0.031 s | 272 KB |
