# 1330. 区间

[Timus 1330](https://acm.timus.ru/problem.aspx?space=1&num=1330) · 难度 95 · prefix_sums

原题作者 Den Raskovalov，出自 2004 年 10 月 16 日第十届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N ≤ 10 000 个传感器给出 −10 000 到 10 000 之间的整数读数。回答最多 100 000 个问题：第 i 到第 j 个传感器
（i ≤ j）读数之和。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

N，然后 N 个读数，然后 Q 和 Q 对 i, j。

## 输出

每行一个和。

## 样例

### 样例 1

输入：

```
5
1
2
3
-1
4
3
1 5
4 4
1 4
```

输出：

```
9
-1
5
```

## 解法

维护 before[i]，即前 i 个读数之和，before[0] = 0。从 i 到 j 的和就是 before[j] − before[i − 1]，每个问题
一次减法。`O(N + Q)`。

注意事项：

- 和在 −10⁸ 到 10⁸ 之间，32 位整数放得下；
- 可能根本没有问题（测试 03）；
- 有 100 000 个问题时，输入输出要大块读写，才能在 0.5 秒内完成。

## 各语言说明

- Java 通过自己的字节缓冲区读取输入，并把答案收集成一个字符串。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1330_prefix_sums.cpp](1330_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 2784 KB |
| [1330_prefix_sums.go](1330_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 2828 KB |
| [1330_prefix_sums.java](1330_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + Q) | AC | 0.109 s | 7492 KB |
| [1330_prefix_sums.py](1330_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 27608 KB |
| [1330_prefix_sums.rs](1330_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 3736 KB |
