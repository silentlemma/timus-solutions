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

优化解法（C++、Java）使用同样的排队计数。C++ 用 `scanf` 和 `printf` 代替
`iostream`：124 KB，而不是 392 KB，时间不变。Java 从较小的缓冲区中手工解析数字，
而不是使用 `Scanner`：364 KB，而不是 1680 KB，时间不变。

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
| [1787_simulation_optimized.java](1787_simulation_optimized.java) \* | Java 1.8 | simulation | O(n) | AC | 0.125 s | 364 KB | 11303638 |

\* 未进入当前评测机上该语言解法的前 10 名或前 15%，可能还能进一步优化。
