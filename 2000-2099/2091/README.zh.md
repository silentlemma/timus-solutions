# 2091. 把培养方案分得最均匀的两门课

[Timus 2091](https://acm.timus.ru/problem.aspx?space=1&num=2091) · 难度 271 · bruteforce

原题作者 Dmitry Ivankov，出自 2014 年乌拉尔联邦大学公开个人赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个 n × m 的表说明 n 个培养方案各包含 m 门课中的哪些。选两门不同的课 A 和 B；它们把方案分成四组：两门都有、只有 A、只有 B、都没有。使最大的一组尽量小，输出其大小和两门课。任何最优的一对都可接受。时间限制 1 秒，内存限制 64 MB。

## 输入

n 和 m（4 ≤ n, m ≤ 100），然后是 n 行，每行 m 个 0 或 1。

## 输出

最大组的最小可能大小，然后是两门课。

## 评测方式

检查器比较大小，并重新统计输出的这对课程的分组。

## 样例

### 样例 1

输入：

```
6 4
0 0 0 1
0 0 1 0
0 1 1 1
1 1 1 1
0 0 0 0
1 0 0 1
```

输出：

```
2
1 3
```

## 解法

课程对少于 5000 个，一对课程的分组只需扫一遍方案，组号为 2·[A] + [B]。枚举所有对的代价是 O(m² n)，五十万步。

样例中课程 1 和 3 给出分组 {4}、{6}、{2, 3} 和 {1, 5}，最大的一组有 2 个方案。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2091_bruteforce.cpp](2091_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 252 KB |
| [2091_bruteforce.go](2091_bruteforce.go) | Go 1.14 x64 | bruteforce | O(m^2 n) | AC | 0.031 s | 1200 KB |
| [2091_bruteforce.java](2091_bruteforce.java) | Java 1.8 | bruteforce | O(m^2 n) | AC | 0.140 s | 5712 KB |
| [2091_bruteforce.py](2091_bruteforce.py) | Python 3.12 x64 | bruteforce | O(m^2 n) | AC | 0.140 s | 776 KB |
| [2091_bruteforce.rs](2091_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 436 KB |
