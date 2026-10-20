# 2199. 区间内变化量之和最接近零的两天

[Timus 2199](https://acm.timus.ru/problem.aspx?space=1&num=2199) · 难度 1265 · sqrt_decomposition, sorting

原题作者 Vadim Barinov，出自 2024 年 ICPC 乌拉尔赛区资格赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个由 N 个整数组成的数组 d 接受 Q 个区间查询 [l, r]：给出区间内两个不同的位置 i、j，使 |dᵢ + dⱼ| 最小，若有多个最优可任选。时间限制 3 秒，内存限制 256 MB。

## 输入

N 和 Q（2 ≤ N, Q ≤ 30 000），然后是 |dᵢ| ≤ 10⁹ 的 d，然后是各查询。

## 输出

每个查询输出两个位置。

## 样例

### 样例 1

输入：

```
6 4
17 11 -1 -4 20 -24
1 2
3 4
2 3
1 6
```

输出：

```
1 2
3 4
2 3
5 6
```

## 解法

把元素按绝对值排序。任何集合的最佳一对都是这个顺序中的两个相邻元素：若对 a 和 b 存在介于其间的元素 c，满足 |a| ≤ |c| ≤ |b|，则把 b 换成 c 或把 a 换成 c 不会使 |a + b| 变大，因为 c 的符号与 a 或 b 之一相同。所以一个集合只需要每个元素在该顺序中的前驱和后继。

查询离线处理，按左端点所在的块分组，类似不带删除的莫队算法。块内的查询按右端点排序，区间位于块右侧的部分只增不减，其元素存放在按绝对值排名的位集中，所以新元素通过位运算找到两个邻居并更新最佳一对。左端点与块边界之间为数不多的几天，对每个查询临时加入后再去掉，它们彼此之间的配对每块只预处理一次。

两个廉价的界去掉了大部分工作。整个数组上的最小 |dᵢ + dⱼ| 事先已知，包含达到它的一对的查询直接由前缀表回答。而在整个数组中最佳伙伴也无法超过当前答案的元素根本不需要插入。

Python 版本不使用位集搜索。把元素逐个插入按绝对值排列的顺序，等价于按相反顺序从完整顺序中删除它们，所以在该顺序上的链表从后往前删除，就能给出每个元素到来时的相邻元素。对于块左侧的少数几天，查询需要对每个这样的天 x 找到已到来的、最接近 −x 的元素 y。y 到来时，恰好对按值排序中位于它与相邻元素中点之间的那些 −x 成为最近者，这些区间同样通过从后往前删除求出。这些区间按到来顺序作用到以 16 天为一组的树上，最后一次赋值生效，查询读取其每一天保存的配对元素。

样例中整个数组在第 5 天和第 6 天给出 |20 − 24| = 4。

块长约为 N / √Q 天时，复杂度为 O((N + Q)√N) 次位集操作。

## 各语言说明

- Python 在 PyPy 下运行：在 CPython 3.12 下它在第 4 个测试点超时（3.031 秒），而在 PyPy 3.10 下以 1.125 秒通过。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2199_sqrt_decomposition_sorting.cpp](2199_sqrt_decomposition_sorting.cpp) | G++ 13.2 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 0.656 s | 3472 KB |
| [2199_sqrt_decomposition_sorting.go](2199_sqrt_decomposition_sorting.go) | Go 1.14 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 1.234 s | 12004 KB |
| [2199_sqrt_decomposition_sorting.java](2199_sqrt_decomposition_sorting.java) | Java 1.8 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 1.812 s | 11324 KB |
| [2199_sqrt_decomposition_sorting.py](2199_sqrt_decomposition_sorting.py) | PyPy 3.10 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 1.125 s | 17704 KB |
| [2199_sqrt_decomposition_sorting.rs](2199_sqrt_decomposition_sorting.rs) | Rust 1.75 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 0.703 s | 7536 KB |
