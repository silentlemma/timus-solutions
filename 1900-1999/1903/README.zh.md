# 1903. Counting Sorted Selections

[Timus 1903](https://acm.timus.ru/problem.aspx?space=1&num=1903) · difficulty 937 · combinatorics

Original problem by Alex Samsonov, prepared by Alexander Fetisov, from Ural Championship 2012.

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 n 个身份不同的对象，每个对象有一个类别。恰好选择 t 个对象，必须包含
指定对象 k。所选对象按类别非降序排列，相同类别可任意排序。
要求 k 能占据第 x 个位置。统计集合数量，而不是排列数量，模 P = 10⁹+7。
时限 1 秒，内存限制 64 MB。

## 输入

先给出 n 和 t，1 ≤ t < n ≤ 5000。接着是 n 个类别 cᵢ，范围 1 到 5000。
最后是 k 和 x，1 ≤ k ≤ n、1 ≤ x ≤ t。k 是原输入中的身份编号，
不是排序后的排名。

## 输出

输出合法集合数模 10⁹+7。

## 评测方式

精确比较一个整数词元，使用 `tokens` 模式。

## 样例

### 示例 1

```
5 3
2 1 1 3 1
2 3
```

```
1
```

### 示例 2

```
4 2
1 1 1 1
1 2
```

```
3
```

## 解法

设 v = cₖ，L 为类别严格小于 v 的对象数，G 为严格大于 v 的对象数。
k 不属于这两组。在另外 t−1 个所选对象中，设 a 个较小，b 个较大。

排序后，相同类别区间占据 a+1 到 t−b。因此 k 能位于 x 当且仅当
`a ≤ x−1` 且 `b ≤ t−x`。无需乘上同类排列数，只要求存在一种顺序。

先计入所有包含 k 的 `C(n−1,t−1)` 个集合。减去较小对象过多的集合：

`A = Σ(a=x…min(L,t−1)) C(L,a) C(n−1−L,t−1−a)`。

再减去较大对象过多的集合：

`B = Σ(b=t−x+1…min(G,t−1)) C(G,b) C(n−1−G,t−1−b)`。

每项从一个严格类别组中选择恰好指定的数量，其余从补集中任取，包括与 k
同类的对象。两类非法集合不相交：若同时发生则 `a+b ≥ t+1`，
但另外所选对象只有 t−1 个。因此答案是 `C(n−1,t−1) − A − B` 模 P。

每个包含 k 的集合最初恰好计数一次，当且仅当它的同类区间不包含 x 时被
减去。两类不相交，所以不会重复扣除。剩余集合均可把 k 放在 x，证明成立。

预处理到 n−1 的阶乘与逆阶乘。P 是素数且 n < P，阶乘均可逆。
只进行一次模幂 `factorial[n−1]^(P−2)`，然后反向填充逆阶乘。
这样 `C(N,r) = N! / (r!(N−r)!)` 可常数时间计算；r 不在 [0,N] 时为零。

每个求和至多 n 项。时间 `O(n + log P)`，空间 `O(n)`。
P 固定时对 n 为线性时间，不需要排序。

第一例中，第三个位置的类别为 1，只有选中全部三个类别 1 的对象才行，
即编号 2、3、5。第二例中，k 可与另外三个身份中的任意一个组成集合，
答案为三，而不是六个排列。

## 各语言说明

五种实现均计算两个互斥非法族。C++、Go、Java、Rust 使用 64 位乘法，
每次乘法之间都取模；三个余数直接相乘会溢出。减法后立即归一化。
Python 使用 CPython 3.12 和模幂 `pow`。

注意严格比较类别、始终包含身份 k、区分同类对象的身份，以及同类块中所有
可能的位置。空求和为零；唯一最小类别不可能排在第二位。

在 9117 个小查询上，答案与枚举全部 47 013 个带标号子集的结果一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1903_combinatorics.cpp](1903_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n + log P) | AC | 0.015 s | 428 KB |
| [1903_combinatorics.go](1903_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n + log P) | AC | 0.031 s | 1232 KB |
| [1903_combinatorics.java](1903_combinatorics.java) | Java 1.8 | combinatorics | O(n + log P) | AC | 0.093 s | 540 KB |
| [1903_combinatorics.py](1903_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n + log P) | AC | 0.078 s | 1588 KB |
| [1903_combinatorics.rs](1903_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n + log P) | AC | 0.046 s | 264 KB |
