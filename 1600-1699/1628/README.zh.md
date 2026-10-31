# 1628. 白色条纹

[Timus 1628](https://acm.timus.ru/problem.aspx?space=1&num=1628) · 难度 164 · implementation

原题作者 Alexander Ipatov，出自第十三届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

日历是一张 m × n 的表格：第 i 行是一周，第 j 列是一周中的某天。其中 k 个格子被涂黑
（倒霉的日子），其余为白色。线段是 1 × l 或 l × 1 的一排格子。求白色条纹的数量，即在
包含关系下极大的白色线段。

## 输入

第一行为 m、n、k（1 ≤ m, n ≤ 30000，0 ≤ k ≤ 60000）。接下来 k 行每行一个黑格 x y
（1 ≤ x ≤ m，1 ≤ y ≤ n），各格互不相同。

## 输出

白色条纹的数量。

## 样例

### 样例 1

输入：

```
3 5 4
1 1
1 5
2 2
3 3
```

输出：

```
8
```

### 样例 2

输入：

```
5 1 2
2 1
3 1
```

输出：

```
2
```

## 解法

每一行被黑格分成若干白色段，每一列也是如此。长度不小于 2 的段就是一条条纹。单个白格不同：
它在两个方向上都是 1 × 1 的线段，所以只计一次，而且只在它向哪边都不能延长时才计，即它在行
上和列上的邻格全是黑格或在表格之外。否则这个格子已经属于一条更长的条纹。

因此，行统计长度至少为 2 的段，再加上上下都被封住的单个白格；列只统计长度至少为 2 的段。
每行每列各自对黑格排序，用集合判断邻格是否为黑：C++ 用有序集合，其余用哈希集合。
C++：`O(m + n + (m + k) log(k + 1))`；其余：`O(m + n + k log k)`。

易错点：

- 单个白格不能按两个方向各算一次（测试 05）；
- 只有一行或一列时，每个白格在另一方向上都被边界封住（第二个样例）；
- m, n > 1 时，全白的表格有 m + n 条条纹，没有黑格的行和列同样要计入（测试 06）。

在 120 个随机日历和最大的日历上，答案与一个独立的已通过实现一致。

## 优化解法

优化的 C++ 解法用两个扁平的键数组代替每行每列一个 `vector` 以及数对的 `set`：键
`x · (n + 2) + y` 让黑格按行排列，键 `y · (m + 2) + x` 让黑格按列排列。排序后对
每个数组扫描一遍即可走完所有行或所有列；单个白格的上下两侧是否封闭，用在行数组中
二分查找其邻格的键来判断。由于 m, n ≤ 30000，键小于
`30000 · 30002 + 30001 < 2³¹`，放得进 `int`。数字从用 `fread` 反复填充的 4 KB 缓
冲区中手工解析：{1628_implementation_optimized.cpp}。

优化的 Go 解法用两个扁平的键切片代替每行每列一个切片以及格子的哈希集合：键
`x · (n + 2) + y` 让黑格按行排列，键 `y · (m + 2) + x` 让黑格按列排列。排序后对
每个切片扫描一遍即可走完所有行或所有列；单个白格的上下两侧是否封闭，用在行切片中
二分查找其邻格的键来判断。数字从 4 KB 缓冲区中手工解析，而不是用 `fmt.Fscan`：
{1628_implementation_optimized.go}。

优化的 Java 解法用两个扁平的 `int` 键数组代替每行每列一个数组以及 `Long` 键的
`HashSet`：键 `x · (n + 2) + y` 让黑格按行排列，键 `y · (m + 2) + x` 让黑格按列
排列。排序后对每个数组扫描一遍即可走完所有行或所有列；单个白格的上下两侧是否封
闭，用在行数组中二分查找其邻格的键来判断。由于 m, n ≤ 30000，键小于
`30000 · 30002 + 30001 < 2³¹`，放得进 `int`。数字按 4 KB 分块读入后手工解析：
{1628_implementation_optimized.java}。

优化的 Python 解法用两个扁平的整数键列表代替每行每列一个列表以及坐标元组的集合：
键 `x · (n + 2) + y` 让黑格按行排列，键 `y · (m + 2) + x` 让黑格按列排列。排序后
对每个列表扫描一遍即可走完所有行或所有列；单个白格的上下两侧是否封闭，用
`bisect_left` 在行列表中查找其邻格的键来判断。输入按 4 KB 分块读取，而不是一次读
完：{1628_implementation_optimized.py}。

优化的 Rust 解法用两个扁平的 `i32` 键向量代替每行每列一个向量以及格子的哈希集
合：键 `x · (n + 2) + y` 让黑格按行排列，键 `y · (m + 2) + x` 让黑格按列排列。排
序后对每个向量扫描一遍即可走完所有行或所有列；单个白格的上下两侧是否封闭，用在行
向量中二分查找其邻格的键来判断。由于 m, n ≤ 30000，键小于
`30000 · 30002 + 30001 < 2³¹`，放得进 `i32`。数字从 4 KB 缓冲区中手工解析，而不
是把整个输入读进 `String`：{1628_implementation_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1628_implementation_optimized.cpp`: 时间降低 +86.24%; 内存降低 +90.75%; 基础版本: `1628_implementation.cpp`.

- `1628_implementation_optimized.go`: 时间降低 +63.20%; 内存降低 +84.94%; 基础版本: `1628_implementation.go`.

- `1628_implementation_optimized.java`: 时间降低 -14.68%; 内存降低 +86.68%; 基础版本: `1628_implementation.java`.

- `1628_implementation_optimized.py`: 时间降低 -7.34%; 内存降低 +75.34%; 基础版本: `1628_implementation.py`.

- `1628_implementation_optimized.rs`: 时间降低 +0.00%; 内存降低 +92.97%; 基础版本: `1628_implementation.rs`.

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1628_implementation.cpp](1628_implementation.cpp) | G++ 13.2 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.109 s | 6528 KB | 11288406 |
| [1628_implementation.go](1628_implementation.go) | Go 1.14 x64 | implementation | O(m + n + k log k) | AC | 0.125 s | 13204 KB | 11288407 |
| [1628_implementation.java](1628_implementation.java) | Java 1.8 | implementation | O(m + n + k log k) | AC | 0.109 s | 10240 KB | 11288409 |
| [1628_implementation.py](1628_implementation.py) | Python 3.12 x64 | implementation | O(m + n + k log k) | AC | 0.218 s | 25760 KB | 11288408 |
| [1628_implementation.rs](1628_implementation.rs) | Rust 1.75 x64 | implementation | O(m + n + k log k) | AC | 0.031 s | 9440 KB | 11304016 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1628_implementation_optimized.cpp](1628_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.015 s | 604 KB | 11307222 |
| [1628_implementation_optimized.go](1628_implementation_optimized.go) | Go 1.14 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.046 s | 1988 KB | 11307224 |
| [1628_implementation_optimized.java](1628_implementation_optimized.java) | Java 1.8 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.125 s | 1364 KB | 11307223 |
| [1628_implementation_optimized.py](1628_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.234 s | 6352 KB | 11307226 |
| [1628_implementation_optimized.rs](1628_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.031 s | 664 KB | 11307225 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
