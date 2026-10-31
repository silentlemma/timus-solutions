# 1155. 成对清除立方体各顶点上的粒子

[Timus 1155](https://acm.timus.ru/problem.aspx?space=1&num=1155) · 难度 171 · constructive

原题出自 2001 年 4 月在彼尔姆举行的乌拉尔团体程序设计锦标赛英语轮。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

八个舱室 `A` 到 `H` 位于立方体的顶点上（`A B C D` 围成一个面，`E F G H` 按
同样顺序在它们上方），每个舱室有 0 到 100 个粒子。一次操作在两个相邻舱室中
各产生或各湮灭一个粒子。输出至多 1000 次操作使所有舱室变空，或者输出
`IMPOSSIBLE`。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

一行包含八个 0 到 100 的整数，依次对应 `A` 到 `H`。

## 输出

每行一次操作：两个舱室和 `+` 或 `-`；或者 `IMPOSSIBLE`。

## 评测方式

任何合法的操作序列都被接受。检查程序重放这些操作：每次操作必须连接相邻
舱室，任何舱室都不能变成负数，操作不超过 1000 次，最后所有舱室为空。当且
仅当下文所说的两侧总数不同时，才应输出 `IMPOSSIBLE`。

## 样例

### 样例 1

输入：

```
1 0 1 0 3 1 0 0
```

输出：

```
EF-
AE-
BA+
CB-
AE-
```

### 样例 2

输入：

```
0 1 0 1 2 3 2 2
```

输出：

```
IMPOSSIBLE
```

## 解法

像棋盘一样给顶点染色：`A C F H` 在一侧，`B D E G` 在另一侧。每条棱都连接
两侧，所以每次操作让两侧总数改变同样的量，它们的差永远不变。若差不为零，
答案是 `IMPOSSIBLE`。

否则，先把十二条棱各处理一遍，在每条棱上湮灭两端都允许的最多对数。数量
只减不增，所以之后每条棱都有一端为空。仍有粒子的顶点，它的三个邻居都为空，
而它的对顶点——另一侧唯一与它不相邻的顶点——拥有那一侧的全部粒子。由于
两侧总数相等，剩下的是两个对顶点 `u` 和 `w` 中各 `k` 个粒子。它们相隔三条棱
`u x y w`，三步操作“在 `x y` 产生、在 `u x` 湮灭、在 `y w` 湮灭”可以各去掉
一个。第一遍最多 400 次操作，剩余部分最多 `3·100` 次，所以不会超过 1000。

注意事项：

- 只有两个舱室都有粒子时才能湮灭一对，所以每组三步中先做产生；
- 输入全为零时不需要任何操作（测试 03）；
- 八个数必须在同一行；分成多行不符合输入格式，Python 只读取第一行；
- 是否 `IMPOSSIBLE` 只取决于两侧总数，与粒子的分布无关。

答案已用检查程序在全部 13 个固定和生成测试上验证。独立判定程序和操作重放
检查还通过了 3000 个小规模随机输入和 374 个边界用例，最多需要 500 次操作。

## 优化解法

优化的 C++ 解法输出同样的操作，但把每个顶点的粒子数和三个邻居存在以顶点字母为下
标的小型固定数组中，而不是 `std::map`，用 `scanf` 代替 `iostream` 读入，并用
`printf` 立即输出每个操作，而不是把全部输出先拼成字符串：
{1155_constructive_optimized.cpp}。

优化的 Java 解法输出同样的操作，但把每个顶点的粒子数和三个邻居存在以顶点字母为下
标的固定数组中，而不是装箱字符的映射和由 lambda 建立的列表，并按 4 KB 分块逐字节
读入八个数，而不是用 `Scanner`：{1155_constructive_optimized.java}。

优化的 Rust 解法输出同样的操作，但把每个顶点的粒子数和三个邻居存在以顶点字母为下
标的固定数组中，而不是哈希表，并把每个操作直接写入 `BufWriter`，而不是把全部输出
先拼成字符串：{1155_constructive_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1155_constructive_optimized.cpp`: 时间降低 -106.67%; 内存降低 +75.25%; 基础版本: `1155_constructive.cpp`.

- `1155_constructive_optimized.java`: 时间降低 +40.38%; 内存降低 +88.26%; 基础版本: `1155_constructive.java`.

- `1155_constructive_optimized.rs`: 时间降低 +0.00%; 内存降低 +50.46%; 基础版本: `1155_constructive.rs`.

## 各语言说明

- 所有语言按相同顺序处理各棱，并输出相同的操作。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1155_constructive.cpp](1155_constructive.cpp) | G++ 13.2 x64 | constructive | O(total) | AC | 0.015 s | 404 KB | 11281010 |
| [1155_constructive.go](1155_constructive.go) | Go 1.14 x64 | constructive | O(total) | AC | 0.031 s | 1116 KB | 11281106 |
| [1155_constructive.java](1155_constructive.java) | Java 1.8 | constructive | O(total) | AC | 0.156 s | 3884 KB | 11281181 |
| [1155_constructive.py](1155_constructive.py) | Python 3.12 x64 | constructive | O(total) | AC | 0.078 s | 612 KB | 11281128 |
| [1155_constructive.rs](1155_constructive.rs) | Rust 1.75 x64 | constructive | O(total) | AC | 0.015 s | 436 KB | 11281207 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1155_constructive_optimized.cpp](1155_constructive_optimized.cpp) \* | G++ 13.2 x64 | constructive | O(total) | AC | 0.031 s | 100 KB | 11307258 |
| [1155_constructive_optimized.java](1155_constructive_optimized.java) \* | Java 1.8 | constructive | O(total) | AC | 0.093 s | 456 KB | 11307261 |
| [1155_constructive_optimized.rs](1155_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(total) | AC | 0.015 s | 216 KB | 11307262 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
