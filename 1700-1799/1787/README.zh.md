# 1787. 去 MEGA 的转弯

[Timus 1787](https://acm.timus.ru/problem.aspx?space=1&num=1787) · 难度 25 · simulation

原题作者 Bulat Zaynullin，出自 2010 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个红绿灯每分钟放行 k 辆车转弯。路口一开始是空的，第 i 分钟有 aᵢ 辆新车到达。n 分钟后有多少辆车在等待？

## 输入

k 和 n（1 ≤ k, n ≤ 100），然后是 a₁、…、aₙ（0 ≤ aᵢ ≤ 100）。

## 输出

等待的车辆数。

## 样例

### 样例 1

输入：

```
5 3
6 7 2
```

输出：

```
0
```

### 样例 2

输入：

```
5 3
20 0 0
```

输出：

```
5
```

## 解法

逐分钟跟踪堵车：加上新到的车，减去 k，如果结果小于零，堵车就是空的。`O(n)`。

第一个样例中堵车依次为 1、3、0，因为最后一分钟红绿灯前只有 5 辆车。第二个样例中依次为 15、10、5。

注意事项：

- 堵车数不能为负：空闲的一分钟不能把通行能力留到以后，所以用所有 aᵢ 之和减去 n·k 是错误的；
- 同样的原因，顺序也很重要：第一个样例倒过来，即 2 7 6，会剩下 3 辆车而不是 0。

在 150 个随机情形上（任意车辆数以及接近 k 的车辆数），答案与一个独立的已通过实现一致。

## 优化解法

`1787_simulation_optimized.java`. Java 保留相同的流式排队递推：加入本分钟来车数，减去每分钟通行能力，再将等待数截断为非负。每步只保留等待数量，不保存来车数组，也不把未用容量带到以后。固定 256 字节输入缓冲区和直接十进制输出替代 Scanner 与通用格式化。时间 O(N)，辅助空间 O(1)。题目给定的分钟数和来车上界保证计数可用 int。

精确源代码 Java 1.8 Accepted #11327468：0.109 s / 316 KB。2026-11-20 保存的编译器组比较：时间 65/755、内存 5/755。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11303638 为 0.125 s / 364 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1787_simulation_optimized.java`: 0.109 s / 316 KB; 保留教学基础版 `1787_simulation.java`: 0.125 s / 1680 KB.

优化解法（C++、Java）使用同样的排队计数。C++ 用 `scanf` 和 `printf` 代替
`iostream`：124 KB，而不是 392 KB，时间不变。

从输入迭代器逐项读取车流量，仅保留当前等待车辆数。通过的提交 11324248 用时 0.125 秒、占用 244 KB；简单版用时 0.078 秒、占用 420 KB。记录的运行时间高于简单版。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1787_simulation.cpp](1787_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 392 KB | 11303509 |
| [1787_simulation.go](1787_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.031 s | 1076 KB | 11289817 |
| [1787_simulation.java](1787_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.125 s | 1680 KB | 11289820 |
| [1787_simulation.py](1787_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 420 KB | 11289819 |
| [1787_simulation.rs](1787_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.046 s | 248 KB | 11303511 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1787_simulation_optimized.cpp](1787_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 124 KB | 11303637 |
| [1787_simulation_optimized.java](1787_simulation_optimized.java) \* | Java 1.8 | simulation | O(N) time; O(1) auxiliary space | AC | 0.109 s | 316 KB | 11327468 |
| [1787_simulation_optimized.py](1787_simulation_optimized.py) \* | PyPy 3.10 x64 | simulation | O(n) | AC | 0.125 s | 244 KB | 11324248 |

\* 已通过评测；尚未达到单独排名目标：C++ 要求时间和内存均为前十或前 15%，其他语言类别要求两项均第一。此标记与收录条件分开，该版本仍可进一步优化。
