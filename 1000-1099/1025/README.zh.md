# 1025. 在两级多数表决中获胜所需的最少支持者

[Timus 1025](https://acm.timus.ru/problem.aspx?space=1&num=1025) · 难度 67 · greedy, sorting

原题出自 2000 年 10 月 7 日斯维尔德洛夫斯克州第二届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

选民被分成 `K` 组（`K` 为奇数，`1 ≤ K ≤ 101`），每组人数为奇数；总人数不超过 9999。一组中超过半数投赞成时
该组表示“赞成”，超过半数的组表示“赞成”时决议通过。求最少需要多少支持者，在合适地分配到各组后能通过任何
决议。

时间限制：1 秒。内存限制：64 MB。

## 输入

`K`，然后是 `K` 个组的人数。

## 输出

最少的支持者人数。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
5
9 3 11 1 7
```

输出：

```
7
```

### 样例 2

输入：

```
1
9999
```

输出：

```
5000
```

## 题解

要通过决议，支持者必须赢得 `K / 2 + 1` 个组（整数除法，`K` 为奇数），而赢得一个 `s` 人的组（`s` 为奇数）
需要 `s / 2 + 1` 名支持者；该组中多出的支持者是浪费，输掉的组中的支持者也是浪费。

所以要选出 `K / 2 + 1` 个组，使代价 `s / 2 + 1` 的总和最小。代价随人数增大而增大，因此最好的组就是最小
的那些：把人数排序，累加前 `K / 2 + 1` 个组的代价。`O(K log K)`。

注意事项：

- 组的多数是 `K / 2 + 1`，`s` 人组内的多数是 `s / 2 + 1`，不是 `s / 2`；
- 输入中的人数没有排序。

## 优化解法

`1025_greedy_sorting_optimized.py`. Python 仍排序组规模并选最小的 floor(K/2)+1 组。每组大小为奇数，因此支持者数为 (sum(selected_sizes)+needed)//2：一次 C 层 sum 和一次除法替代逐组除法的 Python 生成器。读取二进制整数记号，一次写入答案，并在 main 内退出以跳过局部数据清理。时间 O(K log K)，排序数据 O(K)，处理时还保留已读输入。这仍是相同的多数贪心；保留易读的逐组费用基础版。

精确源代码 Python 3.12 x64 Accepted #11327542：0.062 s / 648 KB。2026-11-20 保存的编译器组比较：时间 66/551、内存 502/551。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11324842（PyPy 3.10 x64）为 0.109 s / 212 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1025_greedy_sorting_optimized.py`: 0.062 s / 648 KB; 保留教学基础版 `1025_greedy_sorting.py`: 0.093 s / 372 KB.

`1025_greedy_sorting_optimized.java`. Java 保留最小多数贪心：赢得最小的 floor(K/2)+1 组，每组需要 floor(size/2)+1 位支持者。题目 K<=101，因此将每个读入规模插入 int 数组的有序位置，避免加载 Arrays.sort。这有意将 O(K log K) 排序换成有界的 O(K^2) 比较以减少库启动开销，并非渐近改进。1024 字节输入缓冲区及直接十进制输出避免 Scanner 和数字字符串。辅助存储 O(K)，保留更简洁的库排序教学版。

精确源代码 Java 1.8 Accepted #11327343：0.093 s / 320 KB。2026-11-20 保存的编译器组比较：时间 108/770、内存 4/770。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11303704 为 0.125 s / 384 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1025_greedy_sorting_optimized.java`: 0.093 s / 320 KB; 保留教学基础版 `1025_greedy_sorting.java`: 0.109 s / 1724 KB.

`1025_greedy_sorting_optimized.go`. Go 保留选择最小若干组以获得多数的贪心策略。优化代码直接读取字节，把每组人数插入最多 101 项的固定数组。这里有意使用插入排序：时间为 O(K²)，而基础排序为 O(K log K)；在这个小规模限制下，它省去动态容器和 fmt 的开销。对前 floor(K/2)+1 组求 floor(size/2)+1 之和，并保留使用库排序的原版。

与 `1025_greedy_sorting.go` 相比：时间 0.031 s → 0.015 s；内存 1076 KB → 796 KB。

## 各语言说明

各语言都是同样的排序与求和。

## 题解代码

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1025_greedy_sorting.cpp](1025_greedy_sorting.cpp) | G++ 13.2 x64 | greedy, sorting | O(K log K) | AC | 0.001 s | 188 KB | 11303273 |
| [1025_greedy_sorting.go](1025_greedy_sorting.go) | Go 1.14 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 1076 KB | 11278301 |
| [1025_greedy_sorting.java](1025_greedy_sorting.java) | Java 1.8 | greedy, sorting | O(K log K) | AC | 0.109 s | 1724 KB | 11278306 |
| [1025_greedy_sorting.py](1025_greedy_sorting.py) | Python 3.12 x64 | greedy, sorting | O(K log K) | AC | 0.093 s | 372 KB | 11278304 |
| [1025_greedy_sorting.rs](1025_greedy_sorting.rs) | Rust 1.75 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 220 KB | 11278307 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1025_greedy_sorting_optimized.java](1025_greedy_sorting_optimized.java) \* | Java 1.8 | greedy, sorting | O(K²) time; O(K) auxiliary space | AC | 0.093 s | 320 KB | 11327343 |
| [1025_greedy_sorting_optimized.go](1025_greedy_sorting_optimized.go) | Go 1.14 x64 | greedy, sorting | O(K²) | AC | 0.015 s | 796 KB | 11328361 |
| [1025_greedy_sorting_optimized.py](1025_greedy_sorting_optimized.py) \* | Python 3.12 x64 | greedy, sorting | O(K log K) time; O(K + I) storage | AC | 0.062 s | 648 KB | 11327542 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
