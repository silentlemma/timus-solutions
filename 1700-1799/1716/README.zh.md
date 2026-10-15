# 1716. 另一种解法

[Timus 1716](https://acm.timus.ru/problem.aspx?space=1&num=1716) · 难度 727 · probability

原题作者 Alexander Pronchenkov，由 Daniil Ayzenshteyn 整理，出自 NEERC 2009 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

某题每个测试的答案是 YES（3 字节）或 NO（2 字节）。一个作弊程序在第一个测试输出 YES，之后每个测试输出前一个测试的答案。
给定测试数 n 和答案文件的总大小 s，在所有测试顺序等可能的情况下，求未通过测试数的期望。

## 输入

n 和 s（1 ≤ n ≤ 5000，2n ≤ s ≤ 3n）。

## 输出

未通过测试数的期望，误差不超过 10⁻⁵。

## 样例

### 样例 1

输入：

```
3 7
```

输出：

```
2.0000000
```

## 解法

由大小可得数量：y = s − 2n 个答案是 YES，k = n − y 个是 NO。由期望的线性性，把每个测试未通过的概率相加。
第一个测试的答案为 NO 时未通过，概率为 k/n。之后的每个测试在其答案与前一个不同时未通过：
两个给定位置以任意顺序放着一个 YES 和一个 NO 的概率为 2yk/(n(n − 1))。其余 n − 1 个测试合计 2yk/n，所以期望为

k/n + 2yk/n = k(2y + 1)/n。

样例中 y = 1，k = 2，得 2 · 3/3 = 2。`O(1)`。

注意事项：

- 第一个测试与一个假想的 YES 比较，而不是不比较；
- k(2y + 1) 约可达 1.25 · 10⁷，完全在 64 位整数范围内，只在最后做除法；
- n = 1 不需要特殊处理，因为公式中不再含有 n − 1。

对 7 以内的每个 n 和每种 YES 数量，公式都与枚举所有顺序的结果一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1716_probability.cpp](1716_probability.cpp) | G++ 13.2 x64 | probability | O(1) | AC | 0.015 s | 140 KB |
| [1716_probability.go](1716_probability.go) | Go 1.14 x64 | probability | O(1) | AC | 0.031 s | 1084 KB |
| [1716_probability.java](1716_probability.java) | Java 1.8 | probability | O(1) | AC | 0.109 s | 1820 KB |
| [1716_probability.py](1716_probability.py) | Python 3.12 x64 | probability | O(1) | AC | 0.078 s | 416 KB |
| [1716_probability.rs](1716_probability.rs) | Rust 1.75 x64 | probability | O(1) | AC | 0.062 s | 268 KB |
