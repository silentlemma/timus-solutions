# 1613. 献给统计爱好者

[Timus 1613](https://acm.timus.ru/problem.aspx?space=1&num=1613) · 难度 141 · binary_search

原题作者 Alexander Ipatov，出自 2008 年 3 月 29 日第十二届乌拉尔竞技编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 个城市（1 ≤ n ≤ 69 999）各自运送了一定数量的乘客，都在 1 到 10⁹ − 1 之间。
对 q 个查询（1 ≤ q ≤ 69 999）`l r x` 中的每一个，回答编号在 l 到 r 之间的城市
中是否有恰好运送 x 人的。输出 q 个字符组成的字符串，`1` 表示是，`0` 表示否。

时间限制：1 秒。内存限制：64 MB。

## 输入

n、n 个数、q，然后是 q 行 `l r x`，其中 1 ≤ l ≤ r ≤ n，1 ≤ x < 10⁹。

## 输出

答案字符串。

## 样例

### 样例 1

输入:

```
5
1234567 666666 3141593 666666 4343434
5
1 5 3141593
1 5 578202
2 4 666666
4 4 7135610
1 1 1234567
```

输出:

```
10101
```

## 解法

把 (数量, 城市编号) 对排序。数量为 x 的城市于是连成一块，按编号排列。
对每个查询，二分查找第一个不小于 (x, l) 的对：若它的数量等于 x 且城市
编号不超过 r，答案为是。`O((n + q) log n)`。

易错点：

- 答案是一个没有分隔符的字符串；
- 城市必须在 l 或之后找到，而不只是在某处数量为 x（测试 04）。

## 优化解法

优化的 C++ 解法从 4 KB 缓冲区中手工解析数字，而不是用 `scanf`，并把每一对打包成
一个 `uint64_t`：乘客数小于 10⁹ < 2³⁰，放在城市编号所占的 17 位之上，因为
`n ≤ 69 999 < 2¹⁷`。这些键存放在固定数组中，按普通整数排序；一次查询就是对
`(x << 17) + l` 做一次 `lower_bound`，再与 `(x << 17) + r` 比较；每个答案用
`putchar` 直接输出，而不是先放进 `std::string`：
{1613_binary_search_optimized.cpp}。

优化的 Go 解法从 `bufio.Reader` 中逐字节解析数字，而不是用带 1 MB 缓冲区的
`bufio.Scanner` 加 `strconv.Atoi`，并用一个存放打包对的 `uint64` 切片代替乘客
数、城市和顺序的四个 `int` 切片：乘客数小于 10⁹ < 2³⁰，放在城市编号所占的 17 位
之上，因为 `n ≤ 69 999 < 2¹⁷`。一次查询就是对 `(x << 17) + l` 做一次
`sort.Search`，再与 `(x << 17) + r` 比较；答案直接写入 `bufio.Writer`：
{1613_binary_search_optimized.go}。

优化的 Java 解法从 64 KB 缓冲区中手工解析数字，而不是用 `StreamTokenizer`，并把
每一对打包成一个 `long`，乘客数放在城市编号所占的 17 位之上
（`n ≤ 69 999 < 2¹⁷`）。对普通 `long` 数组排序既不需要每个城市一个 `int[]` 对
象，也不需要比较器；一次查询就是对 `(x << 17) | l` 做一次
`Arrays.binarySearch`：{1613_binary_search_optimized.java}。

优化的 Python 解法按 8 KB 分块读入，逐块转换其中的词，而不是一次切分整个输入。它
把每一对打包成一个整数，乘客数放在城市编号所占的 17 位之上
（`n ≤ 69 999 < 2¹⁷`），这样排好序的列表里是普通整数而不是元组；答案收集在
`bytearray` 中，而不是字符串列表：{1613_binary_search_optimized.py}。

优化的 Rust 解法从 4 KB 缓冲区中手工解析数字，而不是把整个输入（可达约 2 MB）读
进 `String`；排序的数对和二分查找不变：{1613_binary_search_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1613_binary_search_optimized.cpp`: 时间降低 +81.87%; 内存降低 +18.18%; 基础版本: `1613_binary_search.cpp`.

- `1613_binary_search_optimized.go`: 时间降低 +25.81%; 内存降低 +74.47%; 基础版本: `1613_binary_search.go`.

- `1613_binary_search_optimized.java`: 时间降低 +30.13%; 内存降低 +45.22%; 基础版本: `1613_binary_search.java`.

- `1613_binary_search_optimized.py`: 时间降低 +31.78%; 内存降低 +83.68%; 基础版本: `1613_binary_search.py`.

- `1613_binary_search_optimized.rs`: 时间降低 +0.00%; 内存降低 +79.96%; 基础版本: `1613_binary_search.rs`.

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1613_binary_search.cpp](1613_binary_search.cpp) | G++ 13.2 x64 | binary_search | O((n + q) log n) | AC | 0.171 s | 748 KB | 11288259 |
| [1613_binary_search.go](1613_binary_search.go) | Go 1.14 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 5876 KB | 11288261 |
| [1613_binary_search.java](1613_binary_search.java) | Java 1.8 | binary_search | O((n + q) log n) | AC | 0.156 s | 3388 KB | 11304478 |
| [1613_binary_search.py](1613_binary_search.py) | Python 3.12 x64 | binary_search | O((n + q) log n) | AC | 0.343 s | 26612 KB | 11288262 |
| [1613_binary_search.rs](1613_binary_search.rs) | Rust 1.75 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 3692 KB | 11288265 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1613_binary_search_optimized.cpp](1613_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O((n + q) log n) | AC | 0.031 s | 612 KB | 11304474 |
| [1613_binary_search_optimized.go](1613_binary_search_optimized.go) | Go 1.14 x64 | binary_search | O((n + q) log n) | AC | 0.046 s | 1500 KB | 11304475 |
| [1613_binary_search_optimized.java](1613_binary_search_optimized.java) | Java 1.8 | binary_search | O((n + q) log n) | AC | 0.109 s | 1856 KB | 11304479 |
| [1613_binary_search_optimized.py](1613_binary_search_optimized.py) \* | Python 3.12 x64 | binary_search | O((n + q) log n) | AC | 0.234 s | 4344 KB | 11304476 |
| [1613_binary_search_optimized.rs](1613_binary_search_optimized.rs) | Rust 1.75 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 740 KB | 11304477 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
