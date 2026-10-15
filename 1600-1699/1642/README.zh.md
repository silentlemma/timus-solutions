# 1642. 一维迷宫

[Timus 1642](https://acm.timus.ru/problem.aspx?space=1&num=1642) · 难度 96 · implementation

原题作者 Daniil Ayzenshteyn，出自 2008 年 10 月的乌拉尔国立大学中学生竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个人站在直线上的 0 点，线上有障碍物，出口在 x。此人朝选定的方向走，一到出口就离开，遇到障碍物
就掉头。对两种初始方向——向前（坐标增大）和向后——分别求离开前走过的距离，或指出出口无法到达。

## 输入

n 和 x（0 ≤ n ≤ 100），然后是 n 个互不相同的障碍物坐标。所有坐标都不为零、绝对值不超过 1000，
出口处没有障碍物。无论朝哪个方向走，都会遇到出口或障碍物。

## 输出

两个距离，先给向前的，或者输出 `Impossible`。

## 样例

### 样例 1

输入：

```
3 -2
-10 -4 2
```

输出：

```
6 2
```

### 样例 2

输入：

```
3 -2
10 -1 2
```

输出：

```
Impossible
```

## 解法

只有最近的障碍物有用：left 为小于 0 的最大者，right 为大于 0 的最小者。人会在它们之间永远来回，
所以当且仅当 left < x < right 时出口可达，否则输出 `Impossible`。此时两个方向上的路线要么直达，
要么绕一次：

- x > 0：向前为 x；向后走到 left 再回来，为 2 · |left| + x；
- x < 0：向前走到 right 再回来，为 2 · right + |x|；向后为 |x|。

绕路所需的障碍物由题目保证存在。`O(n)`。

易错点：

- 起点与出口之间的障碍物会挡住两个方向，所以一个答案管两个方向（第二个样例、测试 06）；
- 出口那一侧可能完全没有障碍物。

在 300 条随机直线上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1642_implementation.cpp](1642_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB |
| [1642_implementation.go](1642_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1076 KB |
| [1642_implementation.java](1642_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1688 KB |
| [1642_implementation.py](1642_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 504 KB |
| [1642_implementation.rs](1642_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.062 s | 228 KB |
