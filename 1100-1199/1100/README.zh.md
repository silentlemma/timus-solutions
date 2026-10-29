# 1100. 按冒泡排序结果排列的成绩表

[Timus 1100](https://acm.timus.ru/problem.aspx?space=1&num=1100) · 难度 44 · sorting

原题作者 Pavel Atnashev，出自 2001 年 5 月 Tetrahedron Team Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

`N` 支队伍（`1 < N ≤ 150 000`）以二元组给出：唯一编号 `ID`（`1 ≤ ID ≤ 10^7`）和解出的题数 `M`（`0 ≤ M ≤ 100`）。
旧软件用冒泡排序对它们排序：只要按 `M` 有 `A[i] < A[i+1]`，就交换这两个相邻元素。要快速输出同样的表。

时间限制：1 秒。内存限制：16 MB。

## 输入

`N`，然后 `N` 行，每行 `ID` 和 `M`。

## 输出

`N` 行 `ID` 和 `M`，顺序与冒泡排序的结果相同。

## 评测方式

按记号逐个比较输出；多余的空白不影响结果。

## 样例

### 样例 1

输入：

```
8
1 2
16 3
11 2
20 3
3 5
26 4
7 1
22 4
```

输出：

```
3 5
26 4
22 4
16 3
20 3
1 2
11 2
7 1
```

## 题解

冒泡排序只交换分数不同的相邻队伍，所以 `M` 相同的两支队伍永远不会互相超越：结果就是按 `M` 递减的稳定排序。
由于 `M` 只有 101 种取值，计数排序一次扫描即可完成：按输入顺序把每支队伍放进它分数对应的桶里，然后从 100 到 0
依次输出各个桶。`O(N)`。

注意事项：

- 不稳定的排序会打乱分数相同的队伍，答案就变了；
- 内存限制是 16 MB，所以队伍要紧凑地保存；在 Python 中逐行读取输入，并分块写出输出；
- 150 000 行输出需要缓冲写出。

答案在 300 支队伍以内与冒泡排序本身做了核对，更大的表与库中的稳定排序做了核对。

## 优化解法

优化解法（C++、Java、Rust）通过 8 KB 的缓冲区手工读写数字，而不用 `scanf` 和
`printf`、`StreamTokenizer` 和 `PrintWriter`，或 `parse` 和 `writeln!`：有
150 000 行时，大部分时间花在数字与文本的相互转换上。排序仍是同样的计数排序；
Java 把解题数存成字节，因为它不超过 100。C++：0.031 s，而不是 0.265 s，
内存几乎不变（1388 KB 对 1404 KB）。Java：0.109 s，而不是 0.218 s；
1736 KB，而不是 6844 KB。Rust：1688 KB，而不是 6528 KB，时间不变。

## 各语言说明

- Go 用 `bufio.Scanner` 按单词读取，而不是 `fmt.Scan`：输入最多有 150 000 行。
- Python 把编号放在 `array("i")` 类型的桶里，每个编号四个字节。
- Java 用按分数做前缀和的稳定计数排序代替列表。

## 题解代码

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1100_sorting.cpp](1100_sorting.cpp) | G++ 13.2 x64 | sorting | O(N) | AC | 0.265 s | 1404 KB | 11279152 |
| [1100_sorting.go](1100_sorting.go) | Go 1.14 x64 | sorting | O(N) | AC | 0.062 s | 6852 KB | 11303071 |
| [1100_sorting.java](1100_sorting.java) | Java 1.8 | sorting | O(N) | AC | 0.218 s | 6844 KB | 11279155 |
| [1100_sorting.py](1100_sorting.py) | Python 3.12 x64 | sorting | O(N) | AC | 0.234 s | 3308 KB | 11279154 |
| [1100_sorting.rs](1100_sorting.rs) | Rust 1.75 x64 | sorting | O(N) | AC | 0.062 s | 6528 KB | 11279156 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1100_sorting_optimized.cpp](1100_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(N) | AC | 0.031 s | 1388 KB | 11303548 |
| [1100_sorting_optimized.java](1100_sorting_optimized.java) | Java 1.8 | sorting | O(N) | AC | 0.109 s | 1736 KB | 11303549 |
| [1100_sorting_optimized.rs](1100_sorting_optimized.rs) | Rust 1.75 x64 | sorting | O(N) | AC | 0.046 s | 1688 KB | 11303550 |
