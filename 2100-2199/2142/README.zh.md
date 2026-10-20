# 2142. 用双色地支付红色、蓝色和任意法力

[Timus 2142](https://acm.timus.ru/problem.aspx?space=1&num=2142) · 难度 125 · greedy

原题作者 Valentin Zuev，出自 2019 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 A 块红色地、B 块蓝色地和 C 块双色地；每块地产生一点法力，双色地可以选择产生红色或蓝色。一个法术需要 X 点红色法力、Y 点蓝色法力，以及另外 Z 点任意颜色的法力。判断这些地是否足够。时间限制 1 秒，内存限制 256 MB。

## 输入

A、B、C，然后是 X、Y、Z，都在 0 到 10⁹ 之间。

## 输出

能支付法术时输出 "It is a kind of magic"，否则输出 "There are no miracles in life"。

## 样例

### 样例 1

输入：

```
3 3 1
2 2 1
```

输出：

```
It is a kind of magic
```

### 样例 2

输入：

```
5 6 5
6 5 6
```

输出：

```
There are no miracles in life
```

## 解法

红色地应当先支付红色法力，蓝色地先支付蓝色法力，因为任意颜色的部分用什么地都能付。它们付不起的部分 max(0, X − A) + max(0, Y − B) 必须由双色地来付。此后剩下的每块地，不论种类，都能支付 Z 点任意颜色法力，所以第二个条件是 A + B + C ≥ X + Y + Z。两者合起来是充要条件。和可达 3 · 10⁹，超出 32 位整数。

第二个样例中红色需要 6 − 5 = 1 块双色地，但总共 16 块地要付 17 点法力。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2142_greedy.cpp](2142_greedy.cpp) | G++ 13.2 x64 | greedy | O(1) | AC | 0.015 s | 124 KB |
| [2142_greedy.go](2142_greedy.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 1088 KB |
| [2142_greedy.java](2142_greedy.java) | Java 1.8 | greedy | O(1) | AC | 0.109 s | 1620 KB |
| [2142_greedy.py](2142_greedy.py) | Python 3.12 x64 | greedy | O(1) | AC | 0.078 s | 416 KB |
| [2142_greedy.rs](2142_greedy.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.031 s | 228 KB |
