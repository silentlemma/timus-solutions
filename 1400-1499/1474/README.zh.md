# 1474. 关于青蛙

[Timus 1474](https://acm.timus.ru/problem.aspx?space=1&num=1474) · 难度 725 · constructive

原题作者 Alexander Ipatov，出自 2006 年 8 月彼得罗扎沃茨克夏季集训的乌拉尔国立大学与奥廖尔国立技术大学比赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

土墩 0 … 2N（1 ≤ N ≤ 499）上：N 只白青蛙在 0 … N − 1，土墩 N 是空的，N 只黑青
蛙在 N + 1 … 2N。白青蛙可以向右移到空着的相邻土墩，或向右跳过一只黑青蛙落到空
土墩上；黑青蛙向左做同样的事。走法顺序任意。要在一百万步以内交换两种颜色，输出
步数和每一步出发的土墩；若不可能则输出 −1。

时间限制：1 秒。内存限制：64 MB。

## 输入

N。

## 输出

K，然后是 K 个出发土墩。任何正确的序列都可以。

## 样例

### 样例 1

输入:

```
1
```

输出:

```
3
2 0 1
```

## 解法

青蛙只会向前走，所以每只白青蛙恰好越过每只黑青蛙一次，而越过只能靠跳：共 N² 次
跳跃。所有青蛙合计走过 2N(N + 1) 个土墩，跳一次走两个，移一次走一个，所以共有
2N 次移动。因此任何成功的游戏都恰好需要 N² + 2N 步，N = 499 时为 249 999 步，答
案永远不是 −1；唯一的危险是死局，即两只同色青蛙互相挡住。

走法按轮次进行，各轮的步数为 1, 2, …, N，再一次 N，然后 N, …, 1，黑白轮流，黑
色先走。每一轮中，能跳进空土墩就跳，否则就移过去。这种安排
避免了死局，所以总有可走的一步；对 1 到 499 的每个 N 重放走法都确认能完成
交换。`O(N²)`。

注意事项：

- 顺序很重要：不按轮次的贪心走法可能让两只同色青蛙一前一后被困住（02，检
  查程序会重放每一步）；
- 答案永远不会是 −1（所有测试）；
- N = 499 时要输出 249 999 个出发土墩编号，适合使用缓冲输出（gen4）。

## 优化解法

优化版本直接计算下一个空位。递增长度的一组动作最后走一步，递减长度的一组动作最先走一步。中间一组只包含跳跃。输出时复用位置的十进制表示。

G++ 13.2 x64（提交 11320508）的运行时间从 0.031 秒变为 0.015 秒，内存从 1524 KB 变为 224 KB。

Go 1.14 x64（提交 11320528）的运行时间从 0.046 秒变为 0.046 秒，内存从 10276 KB 变为 1152 KB。

Java 1.8（提交 11320556）的运行时间从 0.14 秒变为 0.109 秒，内存从 8416 KB 变为 772 KB。

Python 3.12 x64（提交 11320580）的运行时间从 0.25 秒变为 0.109 秒，内存从 23792 KB 变为 2044 KB。

Rust 1.75 x64（提交 11320607）的运行时间从 0.031 秒变为 0.015 秒，内存从 14900 KB 变为 248 KB。

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11322266 · Go 1.14 x64 №11322267 · Java 1.8 №11322268 · Python 3.12 x64 №11322269 · Rust 1.75 x64 №11322270.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1474_constructive.cpp](1474_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.031 s | 1524 KB | 11322266 |
| [1474_constructive.go](1474_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.046 s | 10276 KB | 11322267 |
| [1474_constructive.java](1474_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.14 s | 8416 KB | 11322268 |
| [1474_constructive.py](1474_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.25 s | 23792 KB | 11322269 |
| [1474_constructive.rs](1474_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.031 s | 14900 KB | 11322270 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1474_constructive_optimized.cpp](1474_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.015 s | 224 KB | 11320508 |
| [1474_constructive_optimized.go](1474_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N^2) | AC | 0.046 s | 1152 KB | 11320528 |
| [1474_constructive_optimized.java](1474_constructive_optimized.java) | Java 1.8 | constructive | O(N^2) | AC | 0.109 s | 772 KB | 11320556 |
| [1474_constructive_optimized.py](1474_constructive_optimized.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.109 s | 2044 KB | 11320580 |
| [1474_constructive_optimized.rs](1474_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.015 s | 248 KB | 11320607 |

\* 带星号的版本仍有提升排名的空间。
