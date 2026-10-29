# 1126. 每个由 M 个连续读数组成的窗口的最大值

[Timus 1126](https://acm.timus.ru/problem.aspx?space=1&num=1126) · 难度 92 · two_pointers

原题作者 Alexander Mironenko，出自 2001 年 10 月 21 日第六届乌拉尔国立大学大学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定窗口宽度 `M`（`2 ≤ M ≤ 14000`）和以 `-1` 结尾的 `N` 个读数（`M ≤ N ≤ 25000`，每个在 0 到 100000 之间），依次输出读数
`1..M`、`2..M+1`……直到最后一个完整窗口的最大值。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

`M`，然后每行一个读数，最后是 `-1`。

## 输出

`N − M + 1` 个窗口最大值，每行一个。

## 评测方式

输出按记号逐个比较；多余的空白字符无关紧要。

## 样例

### 样例 1

输入：

```
3
10
11
10
0
0
0
1
2
3
2
-1
```

输出：

```
11
11
10
0
1
2
3
3
```

## 解法

维护一个双端队列，存放下标，其对应的值从队头到队尾递减。新读数先从队尾移除所有值不大于它的下标——只要新读数还在窗口中，它们就不可能增大最大值；然后把它加到队尾。队头在离开窗口时出队。队头始终是当前窗口的最大值。每个下标最多进出各一次，所以整个扫描是
`O(N)`；对每个窗口重新计算则要 `O(N·M)`，最多约 1.56 亿步。

注意事项：

- 读数以 `-1` 结束，而不是给出个数；
- 相等的读数可以从队尾全部移除，只留最新的那个，它最后离开窗口；
- `M = N` 时只有一个窗口。

答案经过验证：在所有测试上与直接计算每个窗口最大值的程序比对。

## 优化解法

优化解法（C++、Java）不保存读数：每个读数一读入就连同下标一起进入双端
队列，窗口满时立即输出最大值。C++ 用 `getchar` 读取；Java 手工解析字节缓冲区，
用 `M` 个单元的环形缓冲区存放双端队列（窗口里不会超过这么多），并通过字节
缓冲区输出数字。C++：224 KB，而不是 776 KB，时间不变。Java：0.109 s，而不是
0.156 s；624 KB，而不是 2332 KB。

优化的 Python 和 Rust 解法同样不保存读数，只保存窗口。Python 用两个 `array` 组成
的环形缓冲区保存窗口，而不是用双端队列，并按每批 256 行输出答案：668 KB，而不是
3448 KB，时间不变。Rust 从 4 KB 缓冲区手工解析数字，而不是把整个输入读成字符串，
并且每个答案一算出就通过缓冲输出写出：332 KB，而不是 1192 KB，时间不变。

## 各语言说明

- 在简单解法中，Go 和 Java 用带移动队头的数组实现队列；C++、Rust 和 Python 使用
  库中的双端队列。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1126_two_pointers.cpp](1126_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 776 KB | 11279323 |
| [1126_two_pointers.go](1126_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N) | AC | 0.062 s | 2896 KB | 11279328 |
| [1126_two_pointers.java](1126_two_pointers.java) | Java 1.8 | two_pointers | O(N) | AC | 0.156 s | 2332 KB | 11279331 |
| [1126_two_pointers.py](1126_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N) | AC | 0.140 s | 3448 KB | 11279329 |
| [1126_two_pointers.rs](1126_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.046 s | 1192 KB | 11279332 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1126_two_pointers_optimized.cpp](1126_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 224 KB | 11303561 |
| [1126_two_pointers_optimized.java](1126_two_pointers_optimized.java) | Java 1.8 | two_pointers | O(N) | AC | 0.109 s | 624 KB | 11303563 |
| [1126_two_pointers_optimized.py](1126_two_pointers_optimized.py) \* | Python 3.12 x64 | two_pointers | O(N) | AC | 0.125 s | 668 KB | 11303710 |
| [1126_two_pointers_optimized.rs](1126_two_pointers_optimized.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.031 s | 332 KB | 11303711 |

\* 未进入当前评测机上该语言解法的前 10 名或前 15%，可能还能进一步优化。
