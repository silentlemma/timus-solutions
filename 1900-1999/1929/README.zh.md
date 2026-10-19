# 1929. 包含指定成员且余下可分组的三人队

[Timus 1929](https://acm.timus.ru/problem.aspx?space=1&num=1929) · difficulty 385 · combinatorics

Original problem from Ural Regional School Programming Contest 2012 | by Olga Soboleva (prepared by Kirill Devyatkin).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 人中有 m 名特殊成员。每队恰好三人，且至少有一名特殊成员。
统计包含 1 号成员、并使其余所有人仍能划分为合法三人队的无序队伍。
无论余下有多少种分组方式，每个选定队伍只计一次。限制：1 秒，64 MB。

## 输入

第一行 n,m：6≤n≤999，n 能被 3 整除，1≤m≤n。
第二行给出 m 个互不相同的特殊成员编号，范围 1..n，次序任意。
1 号可能是特殊成员，也可能不是。

## 输出

一个整数，包含 1 号的可行队伍数。

## 评测方式

精确比较一个整数记号。

## 样例

```
6 4
2 3 4 6
```

```
10
```

## 解法

若 1 号特殊，令 h=1，否则 h=0。其余伙伴中有 S=m−h 名特殊成员，
U=n−m−(1−h) 名普通成员。枚举两名伙伴中特殊人数 r=0,1,2。
所选队伍移除 h+r 名特殊成员，必须满足 h+r≥1。
余下有 t=n/3−1 个队，能分组当且仅当 m−h−r≥t。

必要性：每个剩余队伍需要不同的特殊成员。充分性：先为每队指定
一名不同的特殊成员，恰有 2t 人待安排到 2t 个空位中，任意填入即可。
多余的特殊成员同样能填补空位，除此没有限制。

每个合法 r 的贡献为 C(S,r)·C(U,2−r)。不能选出的数量记作零；
C(a,0)=1、C(a,1)=a、C(a,2)=a(a−1)/2。三个情况互不重叠，
每个无序伙伴对恰好出现一次，因此求和就是答案。

读取编号耗时 O(m)，计数计算 O(1)。C++、Go、Java 流式读取，
辅助空间 O(1)；Python 和 Rust 缓冲输入，占 O(m)。

所选队伍自身也必须有特殊成员。正确移除 1 号所属类别，不要计算
伙伴次序或角色安排。剩余每队要求至少一名而非恰好一名特殊成员。
m<n/3 时答案为零；m=n/3 时每队恰好一名，公式自动涵盖。
C(0,0)=1。找到 1 号后仍应读取剩余编号。

## 各语言说明

有符号 32 位整数足够，答案不超过 C(998,2)=497503，中间乘积
a(a−1) 小于一百万。Go 使用 int，Rust 计数使用 i32，Python 使用整数。
先检查人数能否选出再相乘，普通伙伴可能为零。不需要阶乘、模运算、
浮点数或大整数。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1929_combinatorics.cpp](1929_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(m) | AC | 0.015 s | 392 KB |
| [1929_combinatorics.go](1929_combinatorics.go) | Go 1.14 x64 | combinatorics | O(m) | AC | 0.031 s | 1100 KB |
| [1929_combinatorics.java](1929_combinatorics.java) | Java 1.8 | combinatorics | O(m) | AC | 0.125 s | 2404 KB |
| [1929_combinatorics.py](1929_combinatorics.py) | Python 3.12 x64 | combinatorics | O(m) | AC | 0.078 s | 492 KB |
| [1929_combinatorics.rs](1929_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(m) | AC | 0.046 s | 240 KB |
