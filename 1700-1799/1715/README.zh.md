# 1715. Another Ball Killer

[Timus 1715](https://acm.timus.ru/problem.aspx?space=1&num=1715) · 难度 1010 · simulation

原题为民间流传的题目，由 Eugene Krokhalev 整理，出自 NEERC 2009 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n × m 的棋盘上放满五种颜色的球。一步操作移除一个图形——由两个或更多同色球组成、按边相连的一组——
移除 k 个球得 k(k − 1) 分。上方的球下落，变空的列使其右侧的列向左移。
懒惰的玩家选定一个主色并重复：只要存在其他颜色的图形，就移除其中最大的；然后移除主色中最大的图形（如果有）。
大小相同时，选包含最低球的图形，再看最低球中最靠左的。对棋盘上出现的每种颜色，输出以它为主色时玩家的得分。

## 输入

n 和 m（1 ≤ n, m ≤ 50），然后是从上到下的 n 行，由字母 B、G、R、W、Y 组成。

## 输出

按 B、G、R、W、Y 的顺序，对每种出现的颜色输出一行"颜色: 得分"。

## 样例

### 样例 1

输入：

```
3 6
WWWGBG
WBGGGB
GGGGBB
```

输出：

```
B: 74
G: 92
W: 74
```

## 解法

完全按描述进行游戏。一次搜索用广度优先遍历找出所需种类（主色或非主色）的所有图形，
对每个图形记录大小和它的最低球（最低一行中最左的那个），按大小、再按该球的行、再按其列选出最好的。
移除图形时清空其格子，然后把每一列向下压紧，并把非空列向左压紧。

每步至少移除两个球，所以一局至多 nm / 2 步；每步需要在棋盘上搜索一两次，因此一局耗时 `O((nm)²)`，
50 × 50 时为数百万次格子访问，最多进行五局。

注意事项：

- 平局规则针对的是一个球：在所有最大的图形中取最低的球，若同一行有多个则取最左的，
  而不是取最左球最低的图形；
- 每次移除之后，下一次主色操作之前要重新尝试非主色，因为下落的球可能形成新的图形；
- 没有图形的棋盘仍对每种出现的颜色输出 0（测试 02 和 03）；
- Python 解答提交到 PyPy：CPython 在随机的 50 × 50 棋盘上约需 2.5 秒。

在 300 个小型随机棋盘以及两种和五种颜色的大棋盘上，得分与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1715_simulation.cpp](1715_simulation.cpp) | G++ 13.2 x64 | simulation | O((nm)²) per colour | AC | 0.531 s | 560 KB |
| [1715_simulation.go](1715_simulation.go) | Go 1.14 x64 | simulation | O((nm)²) per colour | AC | 0.468 s | 7032 KB |
| [1715_simulation.java](1715_simulation.java) | Java 1.8 | simulation | O((nm)²) per colour | AC | 0.453 s | 5256 KB |
| [1715_simulation.py](1715_simulation.py) | PyPy 3.10 x64 | simulation | O((nm)²) per colour | AC | 1.812 s | 9088 KB |
| [1715_simulation.rs](1715_simulation.rs) | Rust 1.75 x64 | simulation | O((nm)²) per colour | AC | 0.906 s | 368 KB |
