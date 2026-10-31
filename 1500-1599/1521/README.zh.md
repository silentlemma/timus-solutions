# 1521. 军事演习 2

[Timus 1521](https://acm.timus.ru/problem.aspx?space=1&num=1521) · 难度 121 · fenwick

原题作者 Ilya Grebnov、Nikita Rybak 与 Dmitry Kovalioff，出自 Timus Top Coders: Third Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

编号 1 到 N 的 N 名士兵（1 ≤ N ≤ 100000）围成一圈行进。每一轮有一名士兵离开：先是第
K 名（1 ≤ K ≤ N），之后每次是上一个离开者前方第 K 位的士兵，只数仍在行进的人。按离
开的顺序输出士兵编号。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 K。

## 输出

按离开顺序排列的士兵编号。

## 样例

### 样例 1

输入:

```
5 3
```

输出:

```
3 1 5 2 4
```

## 解法

把仍在行进的士兵沿圈依次编为 0, 1, …。若上一个离开者在其中排第 r，那么下一个排第
(r + K − 1) mod（剩余人数），因为离开者的位置由紧跟其后的士兵补上。树状数组中每个仍在行
进的士兵记 1；按 2 的幂下降可在 `O(log N)` 内找到给定排名的士兵，删除则是单点修改。
总计 `O(N log N)`。

注意事项：

- 从普通列表中删除每轮要 `O(N)`，总计 `O(N²)`，对 100000 名士兵太慢（gen1）；
- K = 1 时士兵按顺序离开（测试 03、gen5）；
- K = N 时最后一名士兵先离开（测试 04、gen4）。

## 优化解法

优化的 C++ 解法直接填好树，每个节点写入其区间的长度，因为一开始每个士兵都在行
进；并且在查找过程中顺便删除士兵：下降时没有向前跨步的那些节点，恰好就是区间包含
所找士兵的节点，所以沿途把它们减一，不需要第二遍。树放在静态数组中，每个数用
`printf` 立即输出，而不是把输出收集到字符串里：{1521_fenwick_optimized.cpp}。

优化的 Go 解法直接填好树，每个节点写入其区间的长度，因为一开始每个士兵都在行进；
并且在查找过程中顺便删除士兵：下降时没有向前跨步的那些节点，恰好就是区间包含所找
士兵的节点，所以沿途把它们减一，不需要第二遍。计数用 `int32` 存储（它们不超过
N ≤ 100000，放得下）；N 和 K 逐字节读取，而不是用 `fmt.Scan`；数字用
`strconv.AppendInt` 格式化到一个重复使用的缓冲区中：
{1521_fenwick_optimized.go}。

优化的 Java 解法直接填好树，每个节点写入其区间的长度，因为一开始每个士兵都在行
进；并且在查找过程中顺便删除士兵：下降时没有向前跨步的那些节点，恰好就是区间包含
所找士兵的节点，所以沿途把它们减一，不需要第二遍。N 和 K 从 `System.in` 逐位读
取，而不是用 `BufferedReader` 和 `StringTokenizer`；数字通过 4 KB 的
`BufferedOutputStream` 写出，而不是把输出收集到 `StringBuilder` 中：
{1521_fenwick_optimized.java}。

优化的 Python 解法直接填好树，每个节点写入其区间的长度，因为一开始每个士兵都在行
进；并且在查找过程中顺便删除士兵：下降时没有向前跨步的那些节点，恰好就是区间包含
所找士兵的节点，所以沿途把它们减一，不需要第二遍。树是 32 位无符号整数的 `array`
（计数不超过 N ≤ 100000，放得下），而不是 Python 整数的列表；答案每 1024 个一批
输出，而不是一直攒到最后：{1521_fenwick_optimized.py}。

优化的 Rust 解法直接填好树，每个节点写入其区间的长度，因为一开始每个士兵都在行
进；并且在查找过程中顺便删除士兵：下降时没有向前跨步的那些节点，恰好就是区间包含
所找士兵的节点，所以沿途把它们减一，不需要第二遍。计数用 `u32` 而不是 `usize` 存
储（它们不超过 N ≤ 100000，放得下）；数字通过 `BufWriter` 输出，而不是收集到
`String` 中：{1521_fenwick_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1521_fenwick_optimized.cpp`: 时间降低 -48.39%; 内存降低 +75.84%; 基础版本: `1521_fenwick.cpp`.

- `1521_fenwick_optimized.go`: 时间降低 +25.81%; 内存降低 +46.34%; 基础版本: `1521_fenwick.go`.

- `1521_fenwick_optimized.java`: 时间降低 +26.90%; 内存降低 +82.85%; 基础版本: `1521_fenwick.java`.

- `1521_fenwick_optimized.py`: 时间降低 +4.84%; 内存降低 +88.83%; 基础版本: `1521_fenwick.py`.

- `1521_fenwick_optimized.rs`: 时间降低 +0.00%; 内存降低 +74.68%; 基础版本: `1521_fenwick.rs`.

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1521_fenwick.cpp](1521_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(N log N) | AC | 0.031 s | 2136 KB | 11287371 |
| [1521_fenwick.go](1521_fenwick.go) | Go 1.14 x64 | fenwick | O(N log N) | AC | 0.062 s | 2460 KB | 11287372 |
| [1521_fenwick.java](1521_fenwick.java) | Java 1.8 | fenwick | O(N log N) | AC | 0.171 s | 5016 KB | 11287374 |
| [1521_fenwick.py](1521_fenwick.py) | Python 3.12 x64 | fenwick | O(N log N) | AC | 0.640 s | 12028 KB | 11287373 |
| [1521_fenwick.rs](1521_fenwick.rs) | Rust 1.75 x64 | fenwick | O(N log N) | AC | 0.031 s | 2512 KB | 11287375 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1521_fenwick_optimized.cpp](1521_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(N log N) | AC | 0.046 s | 516 KB | 11304369 |
| [1521_fenwick_optimized.go](1521_fenwick_optimized.go) | Go 1.14 x64 | fenwick | O(N log N) | AC | 0.046 s | 1320 KB | 11304370 |
| [1521_fenwick_optimized.java](1521_fenwick_optimized.java) \* | Java 1.8 | fenwick | O(N log N) | AC | 0.125 s | 860 KB | 11304371 |
| [1521_fenwick_optimized.py](1521_fenwick_optimized.py) \* | Python 3.12 x64 | fenwick | O(N log N) | AC | 0.609 s | 1344 KB | 11304372 |
| [1521_fenwick_optimized.rs](1521_fenwick_optimized.rs) | Rust 1.75 x64 | fenwick | O(N log N) | AC | 0.031 s | 636 KB | 11304373 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
