# 1280. 拓扑排序

[Timus 1280](https://acm.timus.ru/problem.aspx?space=1&num=1280) · 难度 140 · graphs

原题作者 Sergey Volchenkov、Vladimir Pinaev 和 Michael Kopachev，出自 2003 年 10 月 15–16 日在雷宾斯克举行的 ACM ICPC 2003–2004 俄罗斯中部赛区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 1 ≤ N ≤ 1000 门课程和 0 ≤ M ≤ 100 000 条规则“s u”：课程 s 必须在课程 u 之
前学习。给定的全部 N 门课程的顺序是否与每条规则都一致？

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 M，M 条规则，然后是 N 门课程的顺序。课程编号为 1 到 N。

## 输出

`YES` 或 `NO`。

## 样例

### 样例 1

输入：

```
5 6
1 3
1 4
3 5
5 2
4 2
1 2
1 3 4 5 2
```

输出：

```
YES
```

### 样例 2

输入：

```
5 6
1 3
1 4
3 5
5 2
4 2
1 2
1 2 4 5 3
```

输出：

```
NO
```

## 解法

无需排序：记下每门课程在给定顺序中的位置，检查每条规则是否都向前，即 s 排在 u 之前。
如果规则中有环，那么在任何顺序下环上总有一条规则是向后的，所以检查本身就会给出 `NO`，
正符合题意。`O(N + M)`。

注意事项：

- 只要违反一条规则就应输出 `NO`；测试 02 的顺序违反了三条规则：3 → 5、5 → 2 和 4 → 2；
- 规则可能从一门课程指向它自己，没有任何顺序能满足（测试 04）；
- 规则可能重复（测试 07）；
- 没有规则时任何顺序都正确（测试 06）。

## 优化解法

优化的 C++ 解法从 4 KB 缓冲区中手工解析数字，而不是用 `scanf`，并把规则存成位矩
阵，每门课程一行 `std::bitset`，而不是两个可存 100 000 条规则的 `int` 数组。
`N ≤ 1000` 时矩阵约占 125 KB，重复的规则落在同一位上。随后检查所有 `N²` 对课程，
至多一百万个位：{1280_graphs_optimized.cpp}。

优化的 Go 解法从 `bufio.Reader` 中逐字节解析数字，而不是用 `fmt.Fscan`，并把规则
的两端存放在两个 `uint16` 切片中，足以容纳不超过 1000 的课程编号，而不是大四倍的
`int` 切片：{1280_graphs_optimized.go}。

优化的 Java 解法从 4 KB 缓冲区中手工解析数字，而不是用 `StreamTokenizer`，并把规
则存成 `long` 数组中的位矩阵，共 `N` 行、每行 `⌈N / 64⌉` 个字，`N ≤ 1000` 时约
125 KB，而不是两个可存 100 000 条规则的 `int` 数组。随后检查所有 `N²` 对课程：
{1280_graphs_optimized.java}。

优化的 Python 解法按 8 KB 分块读入，逐块转换其中的词，而不是一次切分整个输入，并
把规则的两端存放在无符号 16 位数的 `array("H")` 中，足以容纳不超过 1000 的课程编
号，而不是元组列表：{1280_graphs_optimized.py}。

优化的 Rust 解法从 4 KB 缓冲区中手工解析数字，而不是把整个输入读进 `String`，并
把规则存成 `(u16, u16)` 对，足以容纳不超过 1000 的课程编号，而不是大四倍的
`(usize, usize)` 对：{1280_graphs_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1280_graphs_optimized.cpp`: 时间降低 +86.24%; 内存降低 +76.23%; 基础版本: `1280_graphs.cpp`.

- `1280_graphs_optimized.go`: 时间降低 +75.20%; 内存降低 +61.24%; 基础版本: `1280_graphs.go`.

- `1280_graphs_optimized.java`: 时间降低 +0.00%; 内存降低 +57.10%; 基础版本: `1280_graphs.java`.

- `1280_graphs_optimized.py`: 时间降低 +0.00%; 内存降低 +92.63%; 基础版本: `1280_graphs.py`.

- `1280_graphs_optimized.rs`: 时间降低 +0.00%; 内存降低 +84.16%; 基础版本: `1280_graphs.rs`.

## 各语言说明

- 所有语言都把位置存在数组里，并用它检查每条规则。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1280_graphs.cpp](1280_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.109 s | 976 KB | 11284403 |
| [1280_graphs.go](1280_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.125 s | 3416 KB | 11284414 |
| [1280_graphs.java](1280_graphs.java) | Java 1.8 | graphs | O(N + M) | AC | 0.140 s | 1324 KB | 11284421 |
| [1280_graphs.py](1280_graphs.py) | Python 3.12 x64 | graphs | O(N + M) | AC | 0.171 s | 24372 KB | 11284417 |
| [1280_graphs.rs](1280_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.015 s | 3688 KB | 11284425 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1280_graphs_optimized.cpp](1280_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(N² + M) | AC | 0.015 s | 232 KB | 11304469 |
| [1280_graphs_optimized.go](1280_graphs_optimized.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.031 s | 1324 KB | 11304470 |
| [1280_graphs_optimized.java](1280_graphs_optimized.java) \* | Java 1.8 | graphs | O(N² + M) | AC | 0.140 s | 568 KB | 11304471 |
| [1280_graphs_optimized.py](1280_graphs_optimized.py) \* | Python 3.12 x64 | graphs | O(N + M) | AC | 0.171 s | 1796 KB | 11304472 |
| [1280_graphs_optimized.rs](1280_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.015 s | 584 KB | 11304473 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
