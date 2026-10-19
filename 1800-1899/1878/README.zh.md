# 1878. Rubinchik 魔方

[Timus 1878](https://acm.timus.ru/problem.aspx?space=1&num=1878) · 难度 219 · implementation

原题作者 Denis Mukhametianov，出自 2011 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个玩具由四层套在同一根轴上的透明 4 × 4 板组成。每层有四个彩色小方格，四种颜色各一个，位置使得该层转四分之一圈时每个方格都移到下一个象限。从上方看，各层填满 4 × 4 网格。当每个 2 × 2 象限都是单一颜色时玩具复原。一步是把某一层向任一方向转 90°。给出俯视图，求复原所需的最少步数。

## 输入

四行，每行四个 1 到 4 的颜色：俯视图。

## 输出

最少步数。

## 样例

### 样例 1

输入：

```
2 1 2 3
1 1 2 2
4 4 3 3
1 4 3 4
```

输出：

```
1
```

## 解法

每层恰好有一个颜色 1 的方格，它所在的象限就表示该层的朝向。按转动时方格经过的顺序给象限编号（左上、右上、右下、左下）。当四个颜色 1 的方格都在同一象限 t 时玩具复原。方格在象限 p 的层需要 min(d, 4 − d) 步，其中 d = (p − t) mod 4。枚举四个 t，取代价最小者。`O(1)`。

样例中三个颜色 1 的方格在左上象限，一个在左下象限，相差四分之一圈：一步。

注意事项：

- 复原状态中颜色 1 可以在任意象限：整个玩具可能整体转了一下；
- 相差半圈的层无论往哪边转都要两步；
- 象限必须按环形编号而不是按行编号，否则距离会算错。

在 240 个由复原状态转动各层得到的随机状态上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1878_implementation.cpp](1878_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 128 KB |
| [1878_implementation.go](1878_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1084 KB |
| [1878_implementation.java](1878_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1668 KB |
| [1878_implementation.py](1878_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 420 KB |
| [1878_implementation.rs](1878_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 212 KB |
