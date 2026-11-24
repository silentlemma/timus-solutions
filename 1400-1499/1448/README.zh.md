# 1448. 霍格沃茨的照明

[Timus 1448](https://acm.timus.ru/problem.aspx?space=1&num=1448) · 难度 580 · constructive

原题由 Alexander Mironenko（构思）和 Stanislav Vasiliev（题面与程序）完成，出自 2006 年 3 月 24–25 日第十届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

走廊里有一排 N 盏灯（1 ≤ N ≤ 10⁶），每盏要么全亮要么全灭。阿格斯·费尔奇想要
b%（0 ≤ b ≤ 100）的亮度并尽量均匀：输出 N 个由 0 和 1 组成的数字，使任意连续
L 盏灯中亮着的数量与 L b / 100 相差不超过 2。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

N，然后是 b。

## 输出

灯的排列。任何满足条件的排列都被接受。

## 样例

### 样例 1

输入:

```
10
33
```

输出:

```
0100100100
```

## 解法

第 i 盏灯（从 0 开始计）亮，当且仅当 ⌊(i + 1) b / 100⌋ 大于 ⌊i b / 100⌋。这样
前 k 盏中亮着 ⌊k b / 100⌋ 盏，从 l 到 r 的一段有 ⌊r b / 100⌋ − ⌊l b / 100⌋ 盏，
与 (r − l) b / 100 相差不到 1，远在允许的 2 之内。图案每 100 盏重复一次，因为 i
加 100 会让两个下取整都恰好加 b。`O(N)`。

注意事项：

- b = 0 和 b = 100 时整排只有一种数字（测试 02、03、05、gen1、gen2）；
- 缓冲最多一百万个数字的输出，避免每个数字调用一次输出（gen1 到 gen7）；
- 样例中的排列只是众多正确答案之一。

## 优化解法

C++ 版本维护模 100 的余数来生成一个周期，再将它复制到长度为 100 的倍数的固定缓冲区。输出若干完整块和最后一块的前缀。生成的序列相同，耗时 O(N)，额外空间
O(1)。提交 11316954 使用 112 KB，基础版使用 1144 KB，两者均耗时 0.015 秒。

Go 版本用 `copy` 将已生成的前缀逐次加倍，填满固定大小的输出块。提交 11317198 耗时 0.015 秒，使用 924 KB；基础版耗时 0.031 秒，使用 2056 KB。

Java 版本用 `System.arraycopy` 重复复制周期，并将固定大小的数据块直接写入输出流。提交 11317199 用时 0.109 秒、占用 364 KB，基础版则为 0.125 秒和 3076 KB。

Python 版本重复 100 盏灯的周期，形成固定大小的字节块，再输出所有完整块和末尾前缀。提交 11317212 使用 432 KB，基础版使用 2276 KB，两者均耗时 0.078 秒。

Rust 版本将 100 盏灯的周期逐次加倍，填满固定大小的数据块，再输出完整块和末尾前缀。提交 11317214 耗时 0.046 秒，使用 204 KB；基础版耗时 0.031 秒，使用 2048 KB。

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11322145 · Go 1.14 x64 №11322146 · Java 1.8 №11322147 · Python 3.12 x64 №11322148 · Rust 1.75 x64 №11322149.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1448_constructive.cpp](1448_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 1144 KB | 11322145 |
| [1448_constructive.go](1448_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 2056 KB | 11322146 |
| [1448_constructive.java](1448_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.125 s | 3076 KB | 11322147 |
| [1448_constructive.py](1448_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 2276 KB | 11322148 |
| [1448_constructive.rs](1448_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 2048 KB | 11322149 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1448_constructive_optimized.cpp](1448_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 112 KB | 11316954 |
| [1448_constructive_optimized.go](1448_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 924 KB | 11317198 |
| [1448_constructive_optimized.java](1448_constructive_optimized.java) | Java 1.8 | constructive | O(N) | AC | 0.109 s | 364 KB | 11317199 |
| [1448_constructive_optimized.py](1448_constructive_optimized.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 432 KB | 11317212 |
| [1448_constructive_optimized.rs](1448_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 204 KB | 11317214 |

\* 排名快照中没有其他作者的可比 Go 提交。 在排名快照中，Rust 版本的用时排名第二，内存排名第一。该版本满足内存优化标准。
