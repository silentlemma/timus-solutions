# 1641. 值日

[Timus 1641](https://acm.timus.ru/problem.aspx?space=1&num=1641) · 难度 511 · constructive

原题作者 Pavel Atnashev，出自 2008 年 10 月的乌拉尔国立大学中学生竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 名学生每人负责 k 间教室中的一间，每间教室都要有人负责。m 天中每天由负责不同教室的两名学生值日。
任何一对学生不能值日两次，而每名学生至少要值日一次。输出这样的计划；已知它一定存在。

## 输入

n、k 和 m（2 ≤ k ≤ n ≤ 100）。

## 输出

n 行，给出每名学生负责的教室；然后 m 行，给出每天值日的两人。任何合法计划都被接受。

## 样例

### 样例 1

输入：

```
5 3 4
```

输出：

```
1
2
1
2
3
1 2
3 4
3 5
4 5
```

### 样例 2

输入：

```
4 2 4
```

输出：

```
1
2
1
2
1 2
3 4
1 4
2 3
```

## 解法

用图的语言说：把学生分成 k 个非空组，选出 m 条连接不同组的互不相同的边，覆盖所有学生。覆盖 n 名
学生至少需要 ⌈n/2⌉ 条边，而边数至多为完全 k 部图的边数。组越平均，这个边数越大，所以轮流分配
教室（学生 i 负责教室 i mod k）不比任何其他分法差；既然计划存在，m 就放得下。

轮流分配时，学生 i 与 i + 1 的教室总是不同，所以 (0, 1)、(2, 3)…… 这些对用 ⌈n/2⌉ 天就覆盖了
所有人；若人数为奇数，最后一人与学生 0 配对，若 0 与其同屋则改与学生 1 配对。其余的天按顺序取任意
未用过的、不同教室的对。C++ 为 `O(n² log n)`，其余为 `O(n²)`。

易错点：

- 先覆盖所有人很重要：若只是按顺序填满各天，可能全被前面几名学生占去（测试 07）；
- k = n 时每间教室只有一名学生，所有的对都允许（测试 06）。

检查器接受任何合法计划；在 n ≤ 12 的全部 1866 个可行输入上，程序的计划都能通过。

## 优化解法

C++、Java 保持 i mod k 的均衡房间分配。各房间人数为 sᵢ 时，跨房间对数为 (n²−Σsᵢ²)/2。若两房间相差至少两人，从大房间向小房间移动一人会减少 Σsᵢ²。因此均衡分配足够任何可行 m。先输出不相交的相邻编号对；奇 n 时最后学生与零或一号中异房间者配对。ceil(n/2) 初始对覆盖全部学生，也是必要天数下界。再枚举无序跨房间对，以索引公式跳过初始对，直至 m 天。不存已用集合/矩阵、房间数组或全部天数。8192 字节输出替代 Java 增长 builder，Java 也不用 Scanner。最坏 O(n²)、额外空间 O(1)。保留简单版；Go、Python、Rust 复用达标基础版。

已通过评测的基础实现 [1641_constructive.go](1641_constructive.go), [1641_constructive.py](1641_constructive.py), [1641_constructive.rs](1641_constructive.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1641_constructive.cpp](1641_constructive.cpp) | G++ 13.2 x64 | constructive | O(n² log n) | AC | 0.031 s | 300 KB | 11288471 |
| [1641_constructive.go](1641_constructive.go) \* | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1576 KB | 11288472 |
| [1641_constructive.java](1641_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.125 s | 2048 KB | 11288474 |
| [1641_constructive.py](1641_constructive.py) \* | Python 3.12 x64 | constructive | O(n²) | AC | 0.078 s | 1312 KB | 11288473 |
| [1641_constructive.rs](1641_constructive.rs) \* | Rust 1.75 x64 | constructive | O(n²) | AC | 0.031 s | 644 KB | 11288475 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1641_constructive_optimized.cpp](1641_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 104 KB | 11315496 |
| [1641_constructive_optimized.java](1641_constructive_optimized.java) \* | Java 1.8 | constructive | O(n²) | AC | 0.109 s | 388 KB | 11315497 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
