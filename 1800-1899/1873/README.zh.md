# 1873. GOV 编年史

[Timus 1873](https://acm.timus.ru/problem.aspx?space=1&num=1873) · 难度 366 · implementation

原题作者 Mikhail Rubinchik，出自 2011 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

题面按比赛逐场讲述了 Alarm 队（后来的 Team.GOV）的漫长历史，以及阵容的每次变化。队员编号为 0 到 13。给出队员编号，输出该队员代表这支队伍参加了多少场比赛。最后一次乌拉尔锦标赛的热身赛不计入。

## 输入

队员编号，0 到 13。

## 输出

该队员代表队伍参加的比赛场数。

## 样例

### 样例 1

输入：

```
1
```

输出：

```
21
```

### 样例 2

输入：

```
11
```

输出：

```
0
```

## 解法

所有工作都在于仔细阅读故事；程序只是查表。按顺序的比赛及阵容：

| 比赛 | 队员 |
| --- | --- |
| Alarm：校赛、四分之一决赛、半决赛、乌拉尔、鞑靼斯坦 | 0, 1, 2 |
| 2008 年秋季校赛 | 1, 2 |
| 四分之一决赛 | 1, 2, 3 |
| 半决赛 | 1, 2, 4 |
| 乌拉尔锦标赛选拔赛 | 1, 2, 5 |
| 乌拉尔锦标赛 | 1, 5 |
| 四分之一决赛、校赛、半决赛 | 1, 2, 6 |
| 代际之战 | 1, 6, 7 |
| 乌拉尔锦标赛选拔赛 | 5, 6 |
| 乌拉尔锦标赛 | 1, 5, 6 |
| 校赛、四分之一决赛、全西伯利亚竞赛、半决赛 | 1, 8, 9 |
| 最后一次乌拉尔锦标赛 | 1, 3, 10 |
| SWERC | 1, 12, 13 |

相加得到 0 到 13 号队员的比赛场数：5, 21, 12, 2, 1, 4, 6, 1, 4, 4, 1, 0, 1, 1。`O(1)`。

注意事项：

- 11 号队员只参加了热身赛，所以答案为 0；
- 有些比赛只有两人参加：2008 年校赛缺 3 号，一次乌拉尔锦标赛缺 2 号，一次选拔赛缺 1 号；
- 故事结尾的 SWERC 也要算。

对全部十四名队员，表格与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1873_implementation.cpp](1873_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 128 KB |
| [1873_implementation.go](1873_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1072 KB |
| [1873_implementation.java](1873_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1584 KB |
| [1873_implementation.py](1873_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 388 KB |
| [1873_implementation.rs](1873_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 240 KB |
