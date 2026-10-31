# 1213. 把蟑螂赶进气闸最少要开几次隔板

[Timus 1213](https://acm.timus.ru/problem.aspx?space=1&num=1213) · 难度 170 · graphs

原题作者 Evgeny Krokhalev，出自 2002 年 10 月 USU Open Collegiate Programming Contest（Junior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

货舱最多有 30 个隔舱，由隔板相连，每个隔舱里都满是蟑螂。向一个隔舱放毒气并打开
它的一块隔板，所有蟑螂都会跑到相邻的隔舱。每个隔舱都与气闸相通。求把所有蟑螂都
赶进气闸最少要打开几次隔板。

时间限制：1 秒。内存限制：64 MB。

## 输入

气闸的名字，然后每行一块隔板，写作用 `-` 连接的两个隔舱名，最后一行是 `#`。名字
最多 20 个拉丁字母和数字，区分大小写。

## 输出

最少的打开次数。

## 样例

### 样例 1

输入：

```
Gateway
Machinery-Gateway
Machinery-Control
Control-Central
Control-Engine
Central-Engine
Storage-Gateway
Storage-Waste
Central-Waste
#
```

输出：

```
6
```

## 解法

除气闸外，每个隔舱一开始都有蟑螂，最后必须为空，而隔舱只有在打开它自己的某块隔板
时才会变空，所以每个隔舱至少要打开一次。这也足够了：取一棵能从每个隔舱通到气闸的
隔板树，从最远的隔舱开始向气闸方向依次清空，每个隔舱都通过通往气闸路上的那块隔板。
答案就是不同隔舱名的个数减一。`P` 为隔板数时为 `O(P log P)`。

注意事项：

- `Engine` 和 `engine` 是不同的隔舱；
- 气闸可能根本没有列出隔板，这时答案是 0；
- 隔板的布局无关紧要，只有隔舱的数量有关。

答案已在 100 个随机货舱上与另一份独立解答比对。

## 优化解法

优化的 C++ 解法用 `scanf` 把隔板读入 42 字节的缓冲区（足够放下两个最多 20 个字符
的名字和连字符），并把不同的名字存在一个 30 个名字、每个 21 字节的静态表中，用
`strcmp` 查找：隔舱最多 30 个，线性查找很便宜。这取代了 `iostream`、
`std::string` 和 `std::set` 的结点：{1213_graphs_optimized.cpp}。

优化的 Java 解法用 `BufferedReader` 和 `StringTokenizer` 读取记号，而不是用初始
化正则表达式代价较高的 `Scanner`。它用 `indexOf` 找到连字符并直接加入两个名字，
省去了 `split` 和 `Arrays.asList` 产生的临时数组和列表包装对象：
{1213_graphs_optimized.java}。

优化的 Rust 解法逐行读取输入，而不是把全部输入读进一个字符串，并把不同的名字存在
一个线性查找的小向量中，而不是哈希集合：隔舱最多 30 个，所以无论隔板有多少，最多
只保存 30 个名字：{1213_graphs_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1213_graphs_optimized.cpp`: 时间降低 +0.00%; 内存降低 +74.49%; 基础版本: `1213_graphs.cpp`.

- `1213_graphs_optimized.java`: 时间降低 +28.44%; 内存降低 +72.07%; 基础版本: `1213_graphs.java`.

- `1213_graphs_optimized.rs`: 时间降低 +50.00%; 内存降低 +50.96%; 基础版本: `1213_graphs.rs`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1213_graphs.go](1213_graphs.go).

- 所有语言都把名字收集到集合中，输出集合大小减一。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1213_graphs.cpp](1213_graphs.cpp) | G++ 13.2 x64 | graphs | O(P log P) | AC | 0.015 s | 392 KB | 11283651 |
| [1213_graphs.go](1213_graphs.go) | Go 1.14 x64 | graphs | O(P log P) | AC | 0.015 s | 1064 KB | 11283652 |
| [1213_graphs.java](1213_graphs.java) | Java 1.8 | graphs | O(P log P) | AC | 0.109 s | 1876 KB | 11283654 |
| [1213_graphs.py](1213_graphs.py) | Python 3.12 x64 | graphs | O(P log P) | AC | 0.078 s | 384 KB | 11283653 |
| [1213_graphs.rs](1213_graphs.rs) | Rust 1.75 x64 | graphs | O(P log P) | AC | 0.062 s | 416 KB | 11283655 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1213_graphs_optimized.cpp](1213_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(P log P) | AC | 0.015 s | 100 KB | 11307251 |
| [1213_graphs_optimized.java](1213_graphs_optimized.java) | Java 1.8 | graphs | O(P log P) | AC | 0.078 s | 524 KB | 11307254 |
| [1213_graphs_optimized.rs](1213_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(P log P) | AC | 0.031 s | 204 KB | 11307256 |
