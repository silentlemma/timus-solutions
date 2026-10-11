# 1263. 选举

[Timus 1263](https://acm.timus.ru/problem.aspx?space=1&num=1263) · 难度 42 · implementation

原题作者 Den Raskovalov，出自 2003 年 10 月 11 日斯维尔德洛夫斯克州中学生公开团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 N 名候选人（1 ≤ N ≤ 10 000）和 M 名选民（1 ≤ M ≤ 10 000）；每名选民投给一名候选人。
对每名候选人，输出其得票占比的百分数，保留小数点后两位并带 `%` 号。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 M，然后是 M 个 1 到 N 之间的候选人编号。

## 输出

N 行百分数。

## 样例

### 样例 1

输入：

```
3 6
1
2
3
2
1
1
```

输出：

```
50.00%
33.33%
16.67%
```

## 解法

统计每名候选人的票数，输出保留两位小数的 100 · 票数 / M。`O(N + M)`。

注意事项：

- 没有得票的候选人也要输出一行 `0.00%`（测试 03）；
- 占比可能恰好落在最后一位的一半上，例如 1/32 = 3.125%（测试 04、05）。这些解答像 C 的
  `printf` 一样把这种情况舍入到偶数：3.12%；
- N = 10 000 时，某些语言逐行输出很慢：先把输出收集起来。

## 各语言说明

- C++、Go、Python 和 Rust 直接格式化 double；四者都对 double 的精确值按“半数取偶”舍入。
- Java 的 `String.format` 是“半数进位”，所以 Java 对同一个 double 取 `BigDecimal`，并用
  `HALF_EVEN` 舍入。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1263_implementation.cpp](1263_implementation.cpp) | G++ 13.2 x64 | implementation | O(N + M) | AC | 0.031 s | 252 KB |
| [1263_implementation.go](1263_implementation.go) | Go 1.14 x64 | implementation | O(N + M) | AC | 0.031 s | 1456 KB |
| [1263_implementation.java](1263_implementation.java) | Java 1.8 | implementation | O(N + M) | AC | 0.156 s | 5696 KB |
| [1263_implementation.py](1263_implementation.py) | Python 3.12 x64 | implementation | O(N + M) | AC | 0.078 s | 1948 KB |
| [1263_implementation.rs](1263_implementation.rs) | Rust 1.75 x64 | implementation | O(N + M) | AC | 0.015 s | 468 KB |
