# 1740. 还是驯鹿好！

[Timus 1740](https://acm.timus.ru/problem.aspx?space=1&num=1740) · 难度 138 · math

原题作者 Sergey Pupyrev（由 Daniil Ayzenshteyn 准备），出自第十四届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

到投票站的路长 l 千米。驯鹿可以随意奔跑，只要任何一段长 k 千米的路恰好用 h 小时。求走完全程可能的最短和最长时间。

## 输入

整数 l、k 和 h（1 ≤ k ≤ l ≤ 1000，1 ≤ h ≤ 1000）。

## 输出

最短和最长时间，误差不超过 10⁻⁵。

## 样例

### 样例 1

输入：

```
30 10 1
```

输出：

```
3.00000000 3.00000000
```

## 解法

设 t(x) 为到达第 x 千米处的时间。任何一段 k 千米用时 h 小时，所以 t(x + k) = t(x) + h：t 每 k 千米增长 h，
再加上一个以 k 千米为周期重复的部分。设 l = nk + r，全程用时 nh + t(r)，而 t(r) 介于 t(0) = 0 和 t(k) = h 之间。
驯鹿可以在每段的前 r 千米几乎不花时间，或者几乎花掉全部时间，所以答案为 nh，以及当 r > 0 时为 (n + 1)h。`O(1)`。

样例中 30 千米是三段 10 千米，无论如何都是 3 小时。

注意事项：

- 当 k 整除 l 时两个答案相同；
- 时间是整数，代码输出八位小数。

## 优化解法

优化的 C++ 解法用 `scanf` 而不是 `std::cin` 读入三个数，程序因此完全不带
`iostream` 的那套机制；计算和输出都不变：{1740_math_optimized.cpp}。

优化的 Java 解法用 `StreamTokenizer` 而不是 `Scanner` 读入数字，并且完全不格式化
浮点数：两个答案都是不超过 1000 · 1000 = 10⁶ 的整数，所以它用 `int` 计算，再在每
个数后面接上 `.00000000`，而不是用 `%.8f` 调用 `printf`，后者的格式化器和区域设
置数据比程序其余部分还费资源：{1740_math_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1740_math_optimized.cpp`: 时间降低 +0.00%; 内存降低 +72.28%; 基础版本: `1740_math.cpp`.

- `1740_math_optimized.java`: 时间降低 +0.00%; 内存降低 +75.89%; 基础版本: `1740_math.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1740_math.go](1740_math.go).
- [1740_math.rs](1740_math.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1740_math.cpp](1740_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 404 KB | 11289483 |
| [1740_math.go](1740_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1092 KB | 11289484 |
| [1740_math.java](1740_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1792 KB | 11304069 |
| [1740_math.py](1740_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 404 KB | 11289486 |
| [1740_math.rs](1740_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 252 KB | 11304070 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1740_math_optimized.cpp](1740_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 112 KB | 11304455 |
| [1740_math_optimized.java](1740_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.140 s | 432 KB | 11304456 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
