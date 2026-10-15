# 1628. 白色条纹

[Timus 1628](https://acm.timus.ru/problem.aspx?space=1&num=1628) · 难度 164 · implementation

原题作者 Alexander Ipatov，出自第十三届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

日历是一张 m × n 的表格：第 i 行是一周，第 j 列是一周中的某天。其中 k 个格子被涂黑
（倒霉的日子），其余为白色。线段是 1 × l 或 l × 1 的一排格子。求白色条纹的数量，即在
包含关系下极大的白色线段。

## 输入

第一行为 m、n、k（1 ≤ m, n ≤ 30000，0 ≤ k ≤ 60000）。接下来 k 行每行一个黑格 x y
（1 ≤ x ≤ m，1 ≤ y ≤ n），各格互不相同。

## 输出

白色条纹的数量。

## 样例

### 样例 1

输入：

```
3 5 4
1 1
1 5
2 2
3 3
```

输出：

```
8
```

### 样例 2

输入：

```
5 1 2
2 1
3 1
```

输出：

```
2
```

## 解法

每一行被黑格分成若干白色段，每一列也是如此。长度不小于 2 的段就是一条条纹。单个白格不同：
它在两个方向上都是 1 × 1 的线段，所以只计一次，而且只在它向哪边都不能延长时才计，即它在行
上和列上的邻格全是黑格或在表格之外。否则这个格子已经属于一条更长的条纹。

因此，行统计长度至少为 2 的段，再加上上下都被封住的单个白格；列只统计长度至少为 2 的段。
每行每列各自对黑格排序，用集合判断邻格是否为黑：C++ 用有序集合，其余用哈希集合。
C++：`O(m + n + (m + k) log(k + 1))`；其余：`O(m + n + k log k)`。

易错点：

- 单个白格不能按两个方向各算一次（测试 05）；
- 只有一行或一列时，每个白格在另一方向上都被边界封住（第二个样例）；
- m, n > 1 时，全白的表格有 m + n 条条纹，没有黑格的行和列同样要计入（测试 06）。

在 120 个随机日历和最大的日历上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1628_implementation.cpp](1628_implementation.cpp) | G++ 13.2 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.109 s | 6528 KB |
| [1628_implementation.go](1628_implementation.go) | Go 1.14 x64 | implementation | O(m + n + k log k) | AC | 0.125 s | 13204 KB |
| [1628_implementation.java](1628_implementation.java) | Java 1.8 | implementation | O(m + n + k log k) | AC | 0.109 s | 10240 KB |
| [1628_implementation.py](1628_implementation.py) | Python 3.12 x64 | implementation | O(m + n + k log k) | AC | 0.218 s | 25760 KB |
| [1628_implementation.rs](1628_implementation.rs) | Rust 1.75 x64 | implementation | O(m + n + k log k) | AC | 0.046 s | 9408 KB |
