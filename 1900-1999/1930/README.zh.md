# 1930. 换挡次数最少的路线

[Timus 1930](https://acm.timus.ru/problem.aspx?space=1&num=1930) · difficulty 162 · shortest_paths

Original problem from Ural Regional School Programming Contest 2012 | by Grigoriy Nazarov (prepared by Bulat Zaynullin).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每条道路可双向行驶。输入 a,b 表示 a→b 需要上坡挡，反向需要下坡挡。
求给定不同起点与终点之间最少换挡次数。初始挡位任选且不计费用。
保证存在路线。限制：1.5 秒，64 MB。

## 输入

首先 n,m，2≤n≤10000，1≤m≤100000。接着 m 行不同端点 a,b，
编号在 1..n，a→b 为上坡。没有自环，每对无序城市至多一条路。
最后一行是不同且连通的起点、终点。其他城市可以处于不同连通分量。
城市编号大小不代表道路方向。

## 输出

一个整数：最少换挡次数。

## 评测方式

精确比较一个整数记号。

## 样例

```
3 2
1 2
3 2
1 3
```

```
1
```

```
3 3
1 2
2 3
3 1
1 3
```

```
0
```

## 解法

每城建立两个状态，表示城市与当前挡位。经过要求挡位 d 的道路时，
由 (城市,g) 转到 (邻城,d)，g=d 时费用为 0，否则为 1。起点两个
状态距离均为 0，表示首次挡位免费选择。终点任意挡位都可接受。

运行 0–1 BFS：零费用改善放双端队列前端，一费用改善放后端。
首次弹出时确定状态，后来的重复项跳过。确定任一终点状态即返回。
队列按 Dijkstra 的距离顺序处理未确定状态：零费用仍属当前距离，
一费用排在后面，因此首次确定的距离最优。

每条实际路线对应同样换挡数的状态路径；反之，每个状态转移对应
合法道路行驶及可能的一次提前换挡。两个零距离初始状态包含两种
免费初始选择。因此状态最短距离恰为题目答案，首次确定终点便取得它。

时间、空间均为 O(n+m)。共有 2n 个状态、4m 个可能转移。
每个状态确定后仅扫描一次所属城市的邻接表，重复队列项跳过，
每次成功改善对应一条转移。

边数最少不一定换挡最少。必须区分同一城市的两个挡位状态，
同样便宜但不同挡位的到达不能合并。初始挡位不计一次换挡，
也不限定上坡挡开始。逐条使用给定方向：第二例包含有向环，
不能按编号推断高度排序。只保证起终点连通，不保证整个图连通。

## 优化解法

优化的 C++ 解法从用 `fread` 反复填充的 4 KB 缓冲区中手工解析至多 200 004 个数，
并用 `printf` 输出，而不是用 `iostream`；图和 0–1 BFS 不变：
{1930_shortest_paths_optimized.cpp}。

优化的 Go 解法从标准输入读入的 4 KB 缓冲区中手工解析数字，而不是对至多 200 004
个数逐个调用 `fmt.Fscan`；图和 0–1 BFS 不变：
{1930_shortest_paths_optimized.go}。

优化的 Java 解法从 `BufferedInputStream` 中手工解析数字，而不是用
`StreamTokenizer`，并把双端队列做成 `int` 数组上的环形缓冲区，而不是装箱
`Integer` 的 `ArrayDeque`。设邻接项数为 `A = 2m`，则进入队列的状态至多 `2 + 2A`
个，所以容量 `2A + 3` 永远不会占满，还留有一个空位：
{1930_shortest_paths_optimized.java}。

优化的 Python 解法按 4 KB 分块读入，而不是一次切分整个输入，并把每个邻接表存成无
符号 16 位数的 `array("H")`，而不是整数对象的列表：由于 n ≤ 10000，目标状态
2·城市+挡位至多为 19 999：{1930_shortest_paths_optimized.py}。

优化的 Rust 解法把邻接表存成 `Vec<u16>` 而不是 `Vec<usize>`，每项占 2 字节而不是
8 字节：由于 n ≤ 10000，目标状态 2·城市+挡位至多为 19 999。数字从 4 KB 缓冲区中
手工解析，而不是把整个输入读进 `String`：{1930_shortest_paths_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1930_shortest_paths_optimized.cpp`: 时间降低 +67.39%; 内存降低 +12.81%; 基础版本: `1930_shortest_paths.cpp`.

- `1930_shortest_paths_optimized.go`: 时间降低 +66.67%; 内存降低 +20.11%; 基础版本: `1930_shortest_paths.go`.

- `1930_shortest_paths_optimized.java`: 时间降低 +37.60%; 内存降低 -36.59%; 基础版本: `1930_shortest_paths.java`.

- `1930_shortest_paths_optimized.py`: 时间降低 +0.00%; 内存降低 +87.93%; 基础版本: `1930_shortest_paths.py`.

- `1930_shortest_paths_optimized.rs`: 时间降低 +0.00%; 内存降低 +69.02%; 基础版本: `1930_shortest_paths.rs`.

## 各语言说明

邻接项编码为 2·邻城+所需挡位，每条路存两项。距离用有符号 32 位整数足够；2n 可作
无穷大，因为扩展图简单路径少于 2n 条费用至多 1 的边。Java 用 `StreamTokenizer`
读入，每个城市一个 `int` 邻接数组，并使用 `ArrayDeque`。Go 用两个栈实现双端队
列，仅当前端栈为空时才反转延迟的后端栈；每个延迟项最多转移一次，总工作量线性。
C++、Rust 使用标准双端队列，Python 使用 deque，并用 bytearray 存放已确定标记。输
入缓冲与图总空间仍为 O(n+m)。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1930_shortest_paths.cpp](1930_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(n+m) | AC | 0.046 s | 1936 KB | 11291679 |
| [1930_shortest_paths.go](1930_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(n+m) | AC | 0.093 s | 6744 KB | 11291681 |
| [1930_shortest_paths.java](1930_shortest_paths.java) | Java 1.8 | shortest_paths | O(n+m) | AC | 0.125 s | 2536 KB | 11307200 |
| [1930_shortest_paths.py](1930_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(n+m) | AC | 0.187 s | 19520 KB | 11291686 |
| [1930_shortest_paths.rs](1930_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(n+m) | AC | 0.015 s | 4468 KB | 11291694 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1930_shortest_paths_optimized.cpp](1930_shortest_paths_optimized.cpp) | G++ 13.2 x64 | shortest_paths | O(n+m) | AC | 0.015 s | 1688 KB | 11307202 |
| [1930_shortest_paths_optimized.go](1930_shortest_paths_optimized.go) | Go 1.14 x64 | shortest_paths | O(n+m) | AC | 0.031 s | 5388 KB | 11307203 |
| [1930_shortest_paths_optimized.java](1930_shortest_paths_optimized.java) | Java 1.8 | shortest_paths | O(n+m) | AC | 0.078 s | 3464 KB | 11307206 |
| [1930_shortest_paths_optimized.py](1930_shortest_paths_optimized.py) | Python 3.12 x64 | shortest_paths | O(n+m) | AC | 0.187 s | 2356 KB | 11307205 |
| [1930_shortest_paths_optimized.rs](1930_shortest_paths_optimized.rs) | Rust 1.75 x64 | shortest_paths | O(n+m) | AC | 0.015 s | 1384 KB | 11307204 |
