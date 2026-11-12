# 1375. 不随大流

[Timus 1375](https://acm.timus.ru/problem.aspx?space=1&num=1375) · 难度 541 · number_theory

原题作者 Den Raskovalov，出自 2005 年 4 月 19–24 日在叶卡捷琳堡举行的第九届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定素数 p ≤ 10⁶ 和 0 ≤ k ≤ p − 1，输出任意一对 0 到 p − 1 之间的 x、y，使 x² + y² ≡ k (mod p)；若不存在则输出
`NO SOLUTION`。

时间限制：1 秒。内存限制：64 MB。

## 输入

k 和 p。

## 输出

x 和 y，或 `NO SOLUTION`。

## 样例

### 样例 1

输入：

```
1 3
```

输出：

```
0 2
```

## 解法

对奇素数 p，平方数模 p 取 (p + 1) / 2 个不同的值，k − x² 也取同样多个值。p 个数中的两个各含 (p + 1) / 2 个值的集合
必然相交，所以总有 x² 与 y² 之和为 k：答案总是存在，永远不会输出 `NO SOLUTION`。p = 2 时，任何 k 都等于 0² + 0² 或
1² + 0²。

求解时，先为每个平方数记下一个平方根：对 0 到 p − 1 的 y，把 y 记为 y² mod p 的根。然后依次尝试 x = 0, 1, 2, …，
直到 k − x² mod p 有根为止。大约一半的值是平方数，所以几乎立刻就能结束。`O(p)`。

注意事项：

- k = 0 时答案是 0 0（测试 07）；
- k − x² 要取模 p 的非负值；
- y² 可接近 10¹²，超出 32 位整数。

对 300 以内的所有素数和所有 k 检查过答案，测试由接受任意一对答案的检查程序评判。

## 优化解法

新 C++/Go/Rust 以常数空间素域运算代替 O(p) 根表。p=2 或 k=0 时(k,0)。p≡1 mod4 先用 Euler 判据找非二次剩余 z，令 i=z^((p−1)/4)，则 i²=−1。取与 k 同余的奇数 t=k 或 k+p，a=(t+1)/2、b=(t−1)/2 满足 a²−b²=t，故(a mod p, ib mod p) 即答案。p≡3 mod4 时枚举 x=0…(p−1)/2，对 r=k−x² 计算 y=r^((p+1)/4) 并验 y²=r；若 r 为非零平方，Euler 判据给出 y²=r·r^((p−1)/2)=r。r=0 的平方根为零。枚举 x 恰好覆盖所有平方。平方集 S 与 k−S 各有 (p+1)/2 个元素，必有交集，因此扫描能找到一对。64 位乘积小于 10^12。T 次幂试验时间 O(1+T log p)，最坏 O(p log p)，额外空间 O(1)，不声称渐进时间始终优于表法。收录由实际评测/内存收益决定。Rust 用 C 字符 I/O。保留简单表，Java/Python 复用已达标基础版。

已通过评测的基础实现 [1375_number_theory.java](1375_number_theory.java), [1375_number_theory.py](1375_number_theory.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

五个原文件按余数索引数组。优化的 C++、Go 和 Rust 使用模幂与固定数量的整数。评测检查等式，因此两种方法可以输出不同的数对。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1375_number_theory.cpp](1375_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(p) | AC | 0.031 s | 3656 KB | 11285686 |
| [1375_number_theory.go](1375_number_theory.go) | Go 1.14 x64 | number_theory | O(p) | AC | 0.062 s | 9624 KB | 11285689 |
| [1375_number_theory.java](1375_number_theory.java) | Java 1.8 | number_theory | O(p) | AC | 0.156 s | 5172 KB | 11285695 |
| [1375_number_theory.py](1375_number_theory.py) \* | Python 3.12 x64 | number_theory | O(p) | AC | 0.359 s | 23992 KB | 11285693 |
| [1375_number_theory.rs](1375_number_theory.rs) | Rust 1.75 x64 | number_theory | O(p) | AC | 0.046 s | 7892 KB | 11285697 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1375_math.cpp](1375_math.cpp) | G++ 13.2 x64 | math | O(1 + T log p) | AC | 0.015 s | 108 KB | 11315721 |
| [1375_math.go](1375_math.go) \* | Go 1.14 x64 | math | O(1 + T log p) | AC | 0.031 s | 916 KB | 11315726 |
| [1375_math.rs](1375_math.rs) \* | Rust 1.75 x64 | math | O(1 + T log p) | AC | 0.046 s | 64 KB | 11315729 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
