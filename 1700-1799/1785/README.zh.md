# 1785. 本地化之难

[Timus 1785](https://acm.timus.ru/problem.aspx?space=1&num=1785) · 难度 16 · implementation

原题为民间流传的题目，出自 2010 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

某游戏用一个词而不是数字来表示军队规模：1–4 为 "few"，5–9 为 "several"，10–19 为 "pack"，20–49 为 "lots"，
50–99 为 "horde"，100–249 为 "throng"，250–499 为 "swarm"，500–999 为 "zounds"，1000 及以上为 "legion"。
给定怪物数量，输出对应的词。

## 输入

n（1 ≤ n ≤ 2000）。

## 输出

n 对应的词。

## 样例

### 样例 1

输入：

```
7
```

输出：

```
several
```

### 样例 2

输入：

```
40
```

输出：

```
lots
```

## 解法

把各区间的下界从大到小（1000、500、250、100、50、20、10、5、1）和对应的词放在一起。跳过大于 n 的下界，第一个不大于 n 的下界给出答案。`O(1)`。

样例中 7 依次越过 1000 到 10，停在 5，即 "several"；40 停在 20，即 "lots"。

注意事项：

- 下界属于较大的那个词：5 是 "several"，1000 是 "legion"；
- 从 1000 到 2000 的所有 n 都是 "legion"。

在 1 到 2000 的每个 n 上，答案都与一个独立的已通过实现一致。

## 优化解法

优化的 C++ 解法在同一张表中查找单词，但用 `scanf` 读入、用 `puts` 输出，而不是
`iostream`：116 KB，而不是 376 KB，时间不变。

优化的 Java 解法直接从 `System.in` 逐字节解析数字，而不是使用 `Scanner`：0.093 s，
而不是 0.125 s；340 KB，而不是 1600 KB。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1785_implementation.cpp](1785_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 376 KB | 11303506 |
| [1785_implementation.go](1785_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1080 KB | 11289797 |
| [1785_implementation.java](1785_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1600 KB | 11303507 |
| [1785_implementation.py](1785_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 424 KB | 11289798 |
| [1785_implementation.rs](1785_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 228 KB | 11289801 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1785_implementation_optimized.cpp](1785_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 116 KB | 11303636 |
| [1785_implementation_optimized.java](1785_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.093 s | 340 KB | 11303777 |
