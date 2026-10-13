# 1402. 鸡尾酒

[Timus 1402](https://acm.timus.ru/problem.aspx?space=1&num=1402) · 难度 130 · combinatorics

原题作者 Sergey Pupyrev，出自 2005 年 10 月 15 日第十二届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

鸡尾酒由 N ≤ 21 种饮料中的两种或更多种调成，每种至多用一次，且饮料的顺序不
同算不同的鸡尾酒。求不同鸡尾酒的数目。

时间限制：1 秒。内存限制：64 MB。

## 输入

数 N。

## 输出

鸡尾酒的数目。

## 样例

### 样例 1

输入:

```
3
```

输出:

```
12
```

## 解法

k 种饮料的鸡尾酒就是从中有序地选出 k 种不同的饮料，共有
N·(N − 1)·…·(N − k + 1) 种。对 k 从 2 到 N 求和，每个乘积由上一个得到。
`O(N)`。

注意事项：

- 只有一种饮料时没有鸡尾酒（测试 02）；
- N = 21 时答案约为 1.4·10²⁰，超过 64 位，所以解答使用 128 位整数或大整数
  （测试 07）。

测试按精确比较判定。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1402_combinatorics.cpp](1402_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N) | AC | 0.015 s | 188 KB |
| [1402_combinatorics.go](1402_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N) | AC | 0.031 s | 1176 KB |
| [1402_combinatorics.java](1402_combinatorics.java) | Java 1.8 | combinatorics | O(N) | AC | 0.109 s | 1688 KB |
| [1402_combinatorics.py](1402_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N) | AC | 0.078 s | 388 KB |
| [1402_combinatorics.rs](1402_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N) | AC | 0.031 s | 232 KB |
