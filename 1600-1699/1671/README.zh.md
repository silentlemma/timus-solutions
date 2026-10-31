# 1671. 阿南西的蛛网

[Timus 1671](https://acm.timus.ru/problem.aspx?space=1&num=1671) · 难度 105 · dsu

原题作者 Dmitry Poletaev（由 Alex Samsonov 准备），出自 2008 年 8 月彼得罗扎沃茨克夏季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

蛛网有 N 个结点和 M 根连接结点对的丝。其中 Q 根丝按给定顺序依次被扯断。每次扯断后输出蛛网分成了多少块（连通
部分）。

## 输入

N 和 M（2 ≤ N ≤ 100000，1 ≤ M ≤ 100000），M 根丝（两个端点是编号 1 到 N 的不同
结点），然后是 Q（1 ≤ Q ≤ M）和要扯断的丝的编号，互不相同；丝按输入顺序编号为
1 到 M。

## 输出

Q 个块数，用空格分隔。

## 样例

### 样例 1

输入：

```
4 4
1 2
2 3
1 3
3 4
3
2 4 3
```

输出：

```
1 2 3
```

### 样例 2

输入：

```
3 1
1 2
1
1
```

输出：

```
3
```

## 解法

扯断难以跟踪，而用并查集合并却很容易，所以把过程倒过来。从所有扯断之后的蛛网开始：合并所有不会被扯断的丝。然后
从最后一次扯断往前处理：当前的块数就是这次扯断之后的答案，然后把这根丝接回去。每次合并两个不同的集合，块数减一。
加上路径压缩为 `O((N + M) log N)`。

易错点：

- 同样两个结点之间可能有好几根丝，扯断其中一根不改变任何东西（测试 03）；
- 扯断之后的答案是接回这根丝之前的块数。

在 200 个随机小蛛网上，答案与每次扯断后用搜索重新数块的结果一致。

## 优化解法

优化的 C++ 解法从用 `fread` 读入的 8 KB 块中手动解析数字，而不是为每个数调用
`scanf`；按大小合并，根节点存放其集合大小的相反数，使树保持较浅；某次扯断处理完
后，把答案直接写在该次扯断所在的位置，而不是另开一个数组；答案用 `printf` 输出，
而不是收集到字符串中：{1671_dsu_optimized.cpp}。

优化的 Go 解法从 64 KB 的带缓冲 reader 中逐字节解析数字，并用 `strconv` 通过
64 KB 的 writer 输出，而不是使用 `fmt.Fscan` 和 `fmt.Fprint`；并查集部分不变：
{1671_dsu_optimized.go}。

优化的 Java 解法从 8 KB 的块中手动解析数字，而不是用 `StreamTokenizer`；按大小合
并，根节点存放其集合大小的相反数，使树保持较浅；某次扯断处理完后，把答案直接写在
该次扯断所在的位置，而不是另开一个数组；数字通过 8 KB 的字节缓冲区输出，而不是把
输出收集到 `StringBuilder` 中：{1671_dsu_optimized.java}。

优化的 Python 解法逐行读取输入，把丝的端点和要扯断的丝的编号存放在 32 位无符号整
数数组中（它们不超过 100000，放得下），而不是把输入的每个词都保留为字节串；按大
小合并，根节点存放其集合大小的相反数，使树保持较浅；某次扯断处理完后，把答案直接
写在该次扯断所在的位置，而不是另建一个列表：{1671_dsu_optimized.py}。

优化的 Rust 解法直接从输入字节解析数字，而不是先把它们全部收集到向量中；丝存为
`u32` 对，父节点用 `i32` 而不是 `usize`（N 和 M 不超过 100000，放得下）；按大小
合并，根节点存放其集合大小的相反数，使树保持较浅；某次扯断处理完后，把答案直接写
在该次扯断所在的位置；通过 `BufWriter` 输出，而不是拼接字符串向量：
{1671_dsu_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1671_dsu_optimized.cpp`: 时间降低 +83.42%; 内存降低 +50.73%; 基础版本: `1671_dsu.cpp`.

- `1671_dsu_optimized.go`: 时间降低 +81.87%; 内存降低 +21.86%; 基础版本: `1671_dsu.go`.

- `1671_dsu_optimized.java`: 时间降低 +10.71%; 内存降低 +67.75%; 基础版本: `1671_dsu.java`.

- `1671_dsu_optimized.py`: 时间降低 -4.57%; 内存降低 +70.52%; 基础版本: `1671_dsu.py`.

- `1671_dsu_optimized.rs`: 时间降低 +32.61%; 内存降低 +65.71%; 基础版本: `1671_dsu.rs`.

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1671_dsu.cpp](1671_dsu.cpp) | G++ 13.2 x64 | dsu | O((N + M) log N) | AC | 0.187 s | 2736 KB | 11304020 |
| [1671_dsu.go](1671_dsu.go) | Go 1.14 x64 | dsu | O((N + M) log N) | AC | 0.171 s | 7576 KB | 11304036 |
| [1671_dsu.java](1671_dsu.java) | Java 1.8 | dsu | O((N + M) log N) | AC | 0.140 s | 6400 KB | 11304022 |
| [1671_dsu.py](1671_dsu.py) | Python 3.12 x64 | dsu | O((N + M) log N) | AC | 0.328 s | 35904 KB | 11304037 |
| [1671_dsu.rs](1671_dsu.rs) | Rust 1.75 x64 | dsu | O((N + M) log N) | AC | 0.046 s | 11480 KB | 11304038 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1671_dsu_optimized.cpp](1671_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O((N + M) log N) | AC | 0.031 s | 1348 KB | 11304032 |
| [1671_dsu_optimized.go](1671_dsu_optimized.go) | Go 1.14 x64 | dsu | O((N + M) log N) | AC | 0.031 s | 5920 KB | 11304261 |
| [1671_dsu_optimized.java](1671_dsu_optimized.java) \* | Java 1.8 | dsu | O((N + M) log N) | AC | 0.125 s | 2064 KB | 11304033 |
| [1671_dsu_optimized.py](1671_dsu_optimized.py) \* | Python 3.12 x64 | dsu | O((N + M) log N) | AC | 0.343 s | 10584 KB | 11304034 |
| [1671_dsu_optimized.rs](1671_dsu_optimized.rs) | Rust 1.75 x64 | dsu | O((N + M) log N) | AC | 0.031 s | 3936 KB | 11304035 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
