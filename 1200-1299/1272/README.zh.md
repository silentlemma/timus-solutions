# 1272. 不在叶卡捷琳堡的地铁

[Timus 1272](https://acm.timus.ru/problem.aspx?space=1&num=1272) · 难度 144 · dsu

原题作者 Magaz Asanov（由 Igor Goldberg 准备），出自 2003 年 10 月 25 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一座城镇建在 1 ≤ N ≤ 10 000 个岛上，岛间有 0 ≤ K ≤ 12 000 条隧道和
0 ≤ M ≤ 12 000 座桥，它们合起来连通所有岛屿。地铁要利用其中一部分连接所有
岛屿，并且使用的桥尽可能少。最少需要多少座桥？

时间限制：1 秒。内存限制：64 MB。

## 输入

N、K 和 M，然后是 K 条隧道和 M 座桥，每条用两个 1 到 N 之间的岛屿编号表示。

## 输出

最少的桥数。

## 样例

### 样例 1

输入：

```
6 3 4
1 2
2 3
4 5
1 3
3 4
4 6
5 6
```

输出：

```
2
```

## 解法

隧道不计代价，所以全部采用：它们把岛屿分成若干已连通的组。每座桥最多把两组合并成一组，
而整个网络是连通的，所以总能选出桥把各组逐个连起来。因此答案是隧道形成的组数减一，用
并查集处理隧道即可，忽略桥的端点。`O((N + K) log N)`。

注意事项：

- 桥本身无关紧要，重要的只是它们能连接各组，而这一点题目已经保证；
- 隧道可能重复，也可能连接岛屿自身（测试 05）；
- 只有一个岛，或仅靠隧道就能连通全部时，答案为 0（测试 02、04）。

## 优化解法

优化的 C++ 解法从 4 KB 缓冲区中手工解析数字，而不是用 `scanf`，并把父节点存放在
有 10 001 个单元的固定全局数组中（`N ≤ 10 000`，足够用），而不是 `std::vector`。
它还会把桥一直读到末尾，而简单解法不读它们：{1272_dsu_optimized.cpp}。

优化的 Go 解法从 `bufio.Reader` 中逐字节解析数字，而不是用 `fmt.Fscan`，并用
`uint16` 而不是 `int` 存放父节点，`uint16` 足以容纳不超过 10 000 的岛屿编号。它
还会把桥一直读到末尾，而简单解法不读它们：{1272_dsu_optimized.go}。

优化的 Python 解法按 8 KB 分块读入，逐块转换其中的词，边读边跳过桥，而不是一次把
整个输入切分成列表：{1272_dsu_optimized.py}。

优化的 Rust 解法从由标准输入反复填充的 4 KB 缓冲区中手工解析数字，而不是把整个输
入读进 `String`，因此内存中只剩父节点数组和缓冲区：{1272_dsu_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1272_dsu_optimized.cpp`: 时间降低 +51.61%; 内存降低 +49.12%; 基础版本: `1272_dsu.cpp`.

- `1272_dsu_optimized.go`: 时间降低 -106.67%; 内存降低 +35.85%; 基础版本: `1272_dsu.go`.

- `1272_dsu_optimized.py`: 时间降低 -17.20%; 内存降低 +67.67%; 基础版本: `1272_dsu.py`.

- `1272_dsu_optimized.rs`: 时间降低 +0.00%; 内存降低 +63.93%; 基础版本: `1272_dsu.rs`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1272_dsu.java](1272_dsu.java).

- 所有语言都使用同样的带路径减半的并查集。Python 和 Rust 读入全部输入，额外耗时 `O(M)`。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu.cpp](1272_dsu.cpp) | G++ 13.2 x64 | dsu | O((N + K) log N) | AC | 0.031 s | 228 KB | 11284262 |
| [1272_dsu.go](1272_dsu.go) | Go 1.14 x64 | dsu | O((N + K) log N) | AC | 0.015 s | 1428 KB | 11284264 |
| [1272_dsu.java](1272_dsu.java) | Java 1.8 | dsu | O((N + K) log N) | AC | 0.140 s | 488 KB | 11284270 |
| [1272_dsu.py](1272_dsu.py) | Python 3.12 x64 | dsu | O((N + K) log N + M) | AC | 0.093 s | 3328 KB | 11284266 |
| [1272_dsu.rs](1272_dsu.rs) | Rust 1.75 x64 | dsu | O((N + K) log N + M) | AC | 0.046 s | 732 KB | 11284276 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu_optimized.cpp](1272_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O((N + K) log N + M) | AC | 0.015 s | 116 KB | 11304487 |
| [1272_dsu_optimized.go](1272_dsu_optimized.go) | Go 1.14 x64 | dsu | O((N + K) log N + M) | AC | 0.031 s | 916 KB | 11304488 |
| [1272_dsu_optimized.py](1272_dsu_optimized.py) \* | Python 3.12 x64 | dsu | O((N + K) log N + M) | AC | 0.109 s | 1076 KB | 11304489 |
| [1272_dsu_optimized.rs](1272_dsu_optimized.rs) | Rust 1.75 x64 | dsu | O((N + K) log N + M) | AC | 0.046 s | 264 KB | 11304490 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
