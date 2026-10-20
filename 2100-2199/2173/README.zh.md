# 2173. 每题至多两个赞助商的安排方法数

[Timus 2173](https://acm.timus.ru/problem.aspx?space=1&num=2173) · 难度 835 · dp, combinatorics

原题作者 Vadim Barinov，出自 2022 年乌拉尔团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 M 道题和 N 个赞助商；赞助商 i 必须恰好出现在 sᵢ 道不同的题目中，而每道题至多提到两个赞助商。求安排方法数对 10⁹ + 7 取模；若某道题的赞助商集合不同，则安排不同。时间限制 2 秒，内存限制 256 MB。

## 输入

N 和 M（1 ≤ N ≤ 1000，1 ≤ M ≤ 2000），然后是 s₁ … s_N，1 ≤ sᵢ ≤ M，总和不超过 2M。

## 输出

安排方法数对 10⁹ + 7 取模。

## 样例

### 样例 1

输入：

```
2 2
1 1
```

输出：

```
4
```

### 样例 2

输入：

```
5 13
1 1 1 1 1
```

输出：

```
351780
```

## 解法

逐个加入赞助商。放好 t 次提及后，题目分成三组：其中 j 道有一个赞助商，(t − j) / 2 道有两个，其余为空。对后面的赞助商来说，只有各组的大小有关系，所以状态只需 j。

下一个愿望为 s 的赞助商占用 a 道已有一个赞助商的题和 s − a 道空题，选法为 C(j, a) · C(e, s − a)，其中 e 为空题数。新状态为 j − a + (s − a)。答案是所有最终状态之和。

状态与 t 同奇偶，所以至多 M / 2 + 1 个状态有效，一个愿望为 s 的赞助商需要 O(M · s) 次转移。总共 O(M · Σ sᵢ) = O(M²)，阶乘及其逆元只需预处理一次。

第一个样例中两个赞助商要么共用一道题（两种），要么各占一道（两种），共四种。

## 各语言说明

Python 解答在 PyPy 3.10 上运行；在 CPython 中 5 · 10⁶ 次内层步骤约需一秒。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2173_dp_combinatorics.cpp](2173_dp_combinatorics.cpp) | G++ 13.2 x64 | dp, combinatorics | O(M sum s) | AC | 0.031 s | 256 KB |
| [2173_dp_combinatorics.go](2173_dp_combinatorics.go) | Go 1.14 x64 | dp, combinatorics | O(M sum s) | AC | 0.062 s | 12392 KB |
| [2173_dp_combinatorics.java](2173_dp_combinatorics.java) | Java 1.8 | dp, combinatorics | O(M sum s) | AC | 0.375 s | 6288 KB |
| [2173_dp_combinatorics.py](2173_dp_combinatorics.py) | PyPy 3.10 x64 | dp, combinatorics | O(M sum s) | AC | 0.218 s | 6836 KB |
| [2173_dp_combinatorics.rs](2173_dp_combinatorics.rs) | Rust 1.75 x64 | dp, combinatorics | O(M sum s) | AC | 0.046 s | 312 KB |
