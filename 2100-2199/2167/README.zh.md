# 2167. 把一个数变成质数的最小异或密钥

[Timus 2167](https://acm.timus.ru/problem.aspx?space=1&num=2167) · 难度 493 · bitmask, number_theory

原题作者 Vadim Barinov，出自 2022 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对 T 个小于 2²⁰ 的数 a 中的每一个，求使 a XOR k 为质数的最小非负密钥 k。时间限制 2 秒，内存限制 256 MB。

## 输入

T（1 ≤ T ≤ 10⁵），然后是这些数（0 ≤ a ≤ 1 048 575）。

## 输出

每个数的最小密钥。

## 样例

### 样例 1

输入：

```
3
5
6
1
```

输出：

```
0
1
2
```

## 解法

对固定的 a，密钥 k = a XOR p 与质数 p 一一对应，所以问题是找出使 a XOR p 最小的质数 p。小于 2²⁰ 的密钥已经能得到所有小于 2²⁰ 的质数（包括 2），而更大的质数需要至少 2²⁰ 的密钥，所以只需考虑小于 2²⁰ 的质数。

p 与 a 在越高的位上相同，异或值就越小。用筛法求出小于 2²⁰ 的质数，并对每个 j 建一张表，记录是否存在以给定 j 位前缀开头的质数；每张表都是下一张表中相邻两项的 OR。查询时从高位开始确定 p 的各位：若某个质数具有保留 a 当前位后的更长前缀，就保留这一位，否则取另一位。准备 O(2²⁰) 之后，每个数只需 20 步。

样例中 5 是质数，6 XOR 1 = 7，1 XOR 2 = 3。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2167_bitmask_number_theory.cpp](2167_bitmask_number_theory.cpp) | G++ 13.2 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.109 s | 2300 KB |
| [2167_bitmask_number_theory.go](2167_bitmask_number_theory.go) | Go 1.14 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.031 s | 3080 KB |
| [2167_bitmask_number_theory.java](2167_bitmask_number_theory.java) | Java 1.8 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.140 s | 4904 KB |
| [2167_bitmask_number_theory.py](2167_bitmask_number_theory.py) | Python 3.12 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.671 s | 16692 KB |
| [2167_bitmask_number_theory.rs](2167_bitmask_number_theory.rs) | Rust 1.75 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.031 s | 4172 KB |
