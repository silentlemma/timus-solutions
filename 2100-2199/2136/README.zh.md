# 2136. 阻止矩形沿烟囱滑下的最少砖块

[Timus 2136](https://acm.timus.ru/problem.aspx?space=1&num=2136) · 难度 2229 · two_pointers

原题作者 Nikita Sivukhin，出自 “迟到总比不到好”专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

烟囱是一个 h 行、宽 w 的网格。第 i 行左边有 lᵢ 块砖、右边有 rᵢ 块砖，它们之间的空格构成一个非空区间。一个 a × b 的矩形从烟囱上方出发，每次移动一格，不能与砖重叠，想从下方出去。添加最少的砖块（每行仍保留非空的空闲区间），使矩形无法通过。时间限制 1 秒，内存限制 256 MB。

## 输入

h 和 w（1 ≤ h ≤ 10⁵，3 ≤ w ≤ 10⁹），然后是 a 和 b（1 ≤ a ≤ 10⁹，2 ≤ b ≤ 10⁹），再然后是各行的 lᵢ, rᵢ，满足 lᵢ, rᵢ ≥ 1 且 lᵢ + rᵢ < w。

## 输出

最少的砖块数。

## 样例

### 样例 1

输入：

```
7 5
1 2
2 1
1 1
1 1
1 1
2 1
1 1
1 1
```

输出：

```
1
```

## 解法

当矩形覆盖固定的 a 行时，它可以在这些行的公共空闲部分内左右自由滑动。从第 i … i + a − 1 行向下一步到第 i + 1 … i + a 行时列不变，所以这些列在 i … i + a 这 a + 1 行中都必须空闲。设 L 和 R 为这样一个 a + 1 行窗口中左侧和右侧砖数的最大值，这一步可行当且仅当 L + R + b ≤ w。烟囱上方和下方的行是空的，所以靠近顶部的窗口更短；矩形能通过当且仅当每个窗口都允许它的那一步。

要阻止它，必须让某个窗口满足 L + R ≥ w − b + 1。在一行中加砖每次使 L 或 R 增加一，又因为 b ≥ 2，每行都还保留空格，所以答案是 max(0, w − b + 1 − 各窗口 (L + R) 的最大值)。用两个求最大值的单调双端队列扫描所有 a + 1 行的窗口，O(h)。

样例中前两行构成的窗口 L + R = 3，而 w − b + 1 = 4，所以在这两行之一再加一块砖就能堵住通路。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2136_two_pointers.cpp](2136_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(h) | AC | 0.046 s | 444 KB |
| [2136_two_pointers.go](2136_two_pointers.go) | Go 1.14 x64 | two_pointers | O(h) | AC | 0.031 s | 6324 KB |
| [2136_two_pointers.java](2136_two_pointers.java) | Java 1.8 | two_pointers | O(h) | AC | 0.140 s | 2188 KB |
| [2136_two_pointers.py](2136_two_pointers.py) | PyPy 3.10 x64 | two_pointers | O(h) | AC | 0.250 s | 18588 KB |
| [2136_two_pointers.rs](2136_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(h) | AC | 0.046 s | 3176 KB |
