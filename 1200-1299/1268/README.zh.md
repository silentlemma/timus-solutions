# 1268. 小楚

[Timus 1268](https://acm.timus.ru/problem.aspx?space=1&num=1268) · 难度 722 · number_theory

原题作者 Pavel Atnashev，出自 2003 年 10 月 25 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

小楚在出生后第 K, K², K³, … 天醒来，并且星期几绝不能重复；一周有 N 天，N 为素数
（2 < N < 65 536），K 不超过一周。对 T ≤ 6553 个 N 中的每一个，输出使醒来次数最多的 K；
从样例可以看出，要求的是最大的那个 K。

时间限制：0.25 秒。内存限制：64 MB。

## 输入

T，然后是 T 个素数 N。

## 输出

每个 N 对应的 K，每行一个。

## 样例

### 样例 1

输入：

```
4
3
5
7
11
```

输出：

```
2
3
5
8
```

## 解法

第 i 次醒来是星期 K^i mod N。这些值以 K 模 N 的乘法阶为周期重复，所以醒来次数最多
（N − 1 次）的是原根。答案就是模 N 的最大原根。

g 是原根，当且仅当对 N − 1 的每个素因子 q 都有 g^((N−1)/q) ≠ 1 mod N。用最小素因子筛
（到 65 536）分解 N − 1，然后依次尝试 g = N − 1, N − 2, …，直到有一个通过。原根在剩余
中占相当比例，所以只需试少数几个候选，每个只做几次快速幂。重复的 N 直接查表。大约为
`O(L log log L + T · k log N)`，其中 L 为筛的上限，k 为候选个数。

注意事项：

- 任何原根都能让星期互不相同，但要求的是最大的那个（样例中 N = 11 时是 8 而不是 2）；
- 时间限制只有四分之一秒，查询多达 6553 个，所以应当用筛分解 N − 1，而不是每次从头
  试除（测试 04、05）；
- 当 N − 1 是 2 的幂时，只需检验一个幂（测试 06）。

对小于 3000 的每个素数，都与逐个列出候选数各次幂的结果比较过。

## 各语言说明

- 所有语言都建立同样的筛，并按 N 保存答案表。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1268_number_theory.cpp](1268_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.015 s | 708 KB |
| [1268_number_theory.go](1268_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 2440 KB |
| [1268_number_theory.java](1268_number_theory.java) | Java 1.8 | number_theory | O(L log log L + T · k log N) | AC | 0.093 s | 2884 KB |
| [1268_number_theory.py](1268_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.109 s | 4508 KB |
| [1268_number_theory.rs](1268_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.015 s | 1420 KB |
