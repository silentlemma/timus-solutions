# 1221. 内含白色菱形的最大黑色正方形

[Timus 1221](https://acm.timus.ru/problem.aspx?space=1&num=1221) · 难度 422 · implementation

原题作者 Nikita Shamgunov，出自第七届乌拉尔国立大学大学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一张 `N × N`（`N ≤ 100`）的方格纸被涂成黑色（1）和白色（0）。从中剪出一个边沿
网格线的最大正方形，它除了一个旋转 45 度、顶点触及各边中点的白色正方形之外全是
黑色。输出它的边长，或 `No solution`。输入包含多张纸，以 `0` 结束。

时间限制：1 秒。内存限制：64 MB。

## 输入

每张纸给出 `N` 和 `N` 行格子；最后是 `0`。

## 输出

对每张纸输出最大这类图形的边长或 `No solution`。

## 样例

### 样例 1

输入：

```
6
1 1 0 1 1 0
1 0 0 0 1 1
0 0 0 0 0 0
1 0 0 0 1 1
1 1 0 1 1 1
0 1 1 1 1 1
4
1 0 0 1
0 0 0 0
0 0 0 0
1 0 0 1
0
```

输出：

```
5
No solution
```

## 解法

白色菱形有一个中心格，并伸到每条边的中点，所以图形的边长为奇数 `2r + 1`，
`r ≥ 1`：相对中心偏移 `(d, e)` 的格子为白色当且仅当 `|d| + |e| ≤ r`。因此图形的
第 `d` 行依次是 `|d|` 个黑格、长 `2(r − |d|) + 1` 的白段和 `|d|` 个黑格；对每行
预先求黑格的前缀和，每行就能在常数时间内检查。

半径从大到小枚举，对每个半径枚举所有中心；找到的第一个图形就是答案。大多数候选
在三个单格上就被否决（中心和上顶点必须是白色，左上角必须是黑色），其余的通常在
检查的第一行就失败。最坏 `O(N⁴)`，实际远小于此。

注意事项：

- 单个白格不算图形：菱形需要在黑色正方形内部有空间，所以最小的图形是 3 × 3，
  正如样例中的第二张纸所示；
- 图形的边长只能是奇数；
- 多张纸依次给出，直到 `0`。

答案已在 300 个包含随机纸张、植入图形的纸张和单色纸张的文件上与另一份独立解答
比对。

## 各语言说明

- 所有语言都逐个数字读取格子，所以行内有无空格都可以。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1221_implementation.cpp](1221_implementation.cpp) | G++ 13.2 x64 | implementation | O(N⁴) | AC | 0.015 s | 316 KB |
| [1221_implementation.go](1221_implementation.go) | Go 1.14 x64 | implementation | O(N⁴) | AC | 0.001 s | 2116 KB |
| [1221_implementation.java](1221_implementation.java) | Java 1.8 | implementation | O(N⁴) | AC | 0.062 s | 936 KB |
| [1221_implementation.py](1221_implementation.py) | Python 3.12 x64 | implementation | O(N⁴) | AC | 0.140 s | 1908 KB |
| [1221_implementation.rs](1221_implementation.rs) | Rust 1.75 x64 | implementation | O(N⁴) | AC | 0.031 s | 500 KB |
