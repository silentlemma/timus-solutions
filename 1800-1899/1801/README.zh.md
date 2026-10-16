# 1801. 革命杯

[Timus 1801](https://acm.timus.ru/problem.aspx?space=1&num=1801) · 难度 4973 · graphs

原题作者 Magaz Asanov，出自 NEERC 2010 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

g·t 支球队分在 t 个档位中，每档 g 支，每支球队属于某个政党。把它们分成 g 个小组，每组 t 支，使每组恰好有每个档位的一支球队，且没有两支球队属于同一政党。输出任意一种分法，或者报告不存在。

## 输入

g 和 t（1 ≤ g, t ≤ 100），然后依次给出各档位，档位之间用空行分隔，每行是一个球队名和它的政党名。名字最多 10 个小写字母，球队名互不相同。

## 输出

"No"，或者 "Yes" 后跟 g 个小组，每组前有一个空行，每行一个球队名，共 t 行。

## 样例

### 样例 1

输入：

```
2 3
cavalry red
guard white

infantry red
guerilla green

czechs white
gunners latvia
```

输出：

```
Yes

cavalry
guerilla
czechs

guard
infantry
gunners
```

### 样例 2

输入：

```
2 2
cavalry red
guard white

czechs white
cossacks white
```

输出：

```
No
```

## 解法

建立二分多重图：一侧是档位，另一侧是政党，每支球队是它的档位与政党之间的一条边。一个小组就是一种颜色：用 g 种颜色给边染色，使任何顶点都不出现重复颜色。
每个档位恰好有 g 条边，所以它恰好看到每种颜色一次，而每个政党每种颜色至多看到一次。由 König 定理，二分图可以用等于其最大度数的颜色数染色，
所以答案为 "No" 当且仅当某个政党的球队多于 g 支。

染色逐边进行。对从档位 u 到政党 v 的边，取 u 处空闲的颜色 a 和 v 处空闲的颜色 b。若二者不同，就从 u 出发沿 b、a 交替的路径走。
在二分图中这条路径不会终止于 v，因为 v 没有颜色为 b 的边。沿路径交换 a 和 b 后，u 处的 b 被释放，新边染成 b。
路径中每个档位至多出现一次，所以至多有 2t + 1 条边。`O(g·t·(g + t))`。

第一个样例中两支红色球队 cavalry 和 infantry 被分到不同小组，两支白色球队 guard 和 czechs 也是如此。

注意事项：

- 只需检查政党的规模就能判断 "No"；
- 简单地贪心选颜色会卡住，需要沿交替路径重新染色；
- 输入中档位之间的空行最好按单词读取直接跳过。

检查器要求每支球队恰好出现一次、每个小组有每个档位的一支球队且组内政党互不相同。所有解答都在数百个小抽签以及 100 个档位的满抽签（政党紧凑、宽松和超额）上通过检查，
并且 "No" 的判断与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1801_graphs.cpp](1801_graphs.cpp) | G++ 13.2 x64 | graphs | O(g t (g + t)) | AC | 0.015 s | 5440 KB |
| [1801_graphs.go](1801_graphs.go) | Go 1.14 x64 | graphs | O(g t (g + t)) | AC | 0.046 s | 12424 KB |
| [1801_graphs.java](1801_graphs.java) | Java 1.8 | graphs | O(g t (g + t)) | AC | 0.140 s | 10672 KB |
| [1801_graphs.py](1801_graphs.py) | Python 3.12 x64 | graphs | O(g t (g + t)) | AC | 0.156 s | 13072 KB |
| [1801_graphs.rs](1801_graphs.rs) | Rust 1.75 x64 | graphs | O(g t (g + t)) | AC | 0.031 s | 9652 KB |
