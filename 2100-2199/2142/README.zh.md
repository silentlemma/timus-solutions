# 2142. 用双色地支付红色、蓝色和任意法力

[Timus 2142](https://acm.timus.ru/problem.aspx?space=1&num=2142) · 难度 127 · greedy

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

易错点（测试 02，即第二个样例）：能满足两种颜色的需求还不够。红色需要 6 − 5 = 1 块双色地，但总共 16 块地要付 17 点法力。

## 优化解法

优化的 Java 解法直接从 `System.in` 逐字节读入六个数，而不是创建 `Scanner`；对只
做两次比较的程序来说，`Scanner` 的正则表达式和区域设置数据才是主要开销。和可达
3 · 10⁹，所以仍用 `long` 计算：{2142_greedy_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `2142_greedy_optimized.java`: 时间降低 +12.80%; 内存降低 +76.67%; 基础版本: `2142_greedy.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [2142_greedy.cpp](2142_greedy.cpp).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2142_greedy.cpp](2142_greedy.cpp) | G++ 13.2 x64 | greedy | O(1) | AC | 0.015 s | 124 KB | 11294928 |
| [2142_greedy.go](2142_greedy.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 1088 KB | 11294929 |
| [2142_greedy.java](2142_greedy.java) | Java 1.8 | greedy | O(1) | AC | 0.125 s | 1560 KB | 11304055 |
| [2142_greedy.py](2142_greedy.py) | Python 3.12 x64 | greedy | O(1) | AC | 0.078 s | 416 KB | 11294930 |
| [2142_greedy.rs](2142_greedy.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.046 s | 228 KB | 11304056 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2142_greedy_optimized.java](2142_greedy_optimized.java) \* | Java 1.8 | greedy | O(1) | AC | 0.109 s | 364 KB | 11304424 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
