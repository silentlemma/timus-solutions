# 2199. 区间内变化量之和最接近零的两天

[Timus 2199](https://acm.timus.ru/problem.aspx?space=1&num=2199) · 难度 1123 · sqrt_decomposition, sorting

原题作者 Vadim Barinov，出自 2024 年 ICPC 乌拉尔赛区资格赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个由 N 个整数组成的数组 d 接受 Q 个区间查询 [l, r]：给出区间内两个不同的位置 i、j，使 |dᵢ + dⱼ| 最小，若有多个最优可任选。时间限制 3 秒，内存限制 256 MB。

## 输入

N 和 Q（2 ≤ N ≤ 30 000, 1 ≤ Q ≤ 30 000），然后是 |dᵢ| ≤ 10⁹ 的 d，然后是满足 1 ≤ l < r ≤ N 的各查询。

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

把元素按绝对值排序。至少存在一对相邻元素达到最优。考虑 |a| ≤ |c| ≤ |b|：若 a、b 同号，(a, c) 不劣于 (a, b)；否则，c 与 b 同号时选择 (a, c)，c 与 a 同号时选择 (c, b)，都不会变差。零可以归入任一符号。反复替换即可得到相邻的最优对，因此插入时只需检查前驱和后继。

查询离线处理，按左端点所在的块分组。每块 B 天，块内查询按右端点排序，块右侧的核心部分只增不减。C++、Java 和 Rust 用有序集合保存绝对值排名，Go 用记录排名占用次数的树状数组，并按序号查找元素。每次查找或更新需要 O(log N)。跨越块边界的查询比较核心内部的最优对、预处理的块后缀内部最优对，以及跨界配对：对每个后缀元素查找核心中相邻的排名。后缀不会插入核心。完全位于块内的查询使用临时集合，每次查询后清空。

编译型语言版本使用两个界。若查询包含达到整个数组最小目标值的一对，前缀表可直接给出答案。此外，如果某元素在整个数组中的最佳伙伴也无法改善当前答案，就可以跳过它。这些剪枝改善实际性能，但不改变最坏情况的复杂度。

Python 使用相同的分块方式，但采用不同的预处理，不使用上述两种剪枝。按绝对值顺序插入元素等价于从完整顺序中逆序删除。链表可以预先记录核心增长及块后缀构建过程中每次插入的邻居。完全位于块内的查询扫描绝对值顺序，按查询端点筛选日期。对于跨界配对，边缘的每个值 x 需要核心中最接近 −x 的值。按数值顺序逆序删除，可以得到新核心元素严格成为最近者的反射值区间；距离相等时保留较早的伙伴。二分查找确定该区间在反射后的边缘值中的边界。按到达顺序，将区间赋值应用到以 16 个边缘元素为一组的树上，两端单独更新。最新时间戳生效，各查询读取其后缀元素的伙伴。

样例中整个数组在第 5 天和第 6 天给出 |20 − 24| = 4。

令 1 ≤ B ≤ N，块长 B 约为 N / √Q。编译型语言版本的时间复杂度为 O(N log N + Q log Q + (N²/B + QB) log N)，Python 为 O(N log N + Q log Q + (N²/B) log(B+1) + QB)。五个版本的辅助空间均为 O(N + Q)。表中 B 表示块长。

易错点：Q 可以等于 1（测试 02–04），这些测试合法，无需替换。相邻指绝对值顺序，而非日期顺序（测试 06）；只要求至少一对最优解相邻。有序集合和树状数组的操作具有对数复杂度，不能按常数时间的位集操作计算。

## 各语言说明

- 表中保留了 PyPy 3.10 的历史评测结果。CPython 的性能取决于运行时和硬件；这些时间不保证 CPython 的速度，也不对应本地测试编号。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2199_sqrt_decomposition_sorting.cpp](2199_sqrt_decomposition_sorting.cpp) | G++ 13.2 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 0.656 s | 3472 KB |
| [2199_sqrt_decomposition_sorting.go](2199_sqrt_decomposition_sorting.go) | Go 1.14 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 1.234 s | 12004 KB |
| [2199_sqrt_decomposition_sorting.java](2199_sqrt_decomposition_sorting.java) | Java 1.8 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 1.812 s | 11324 KB |
| [2199_sqrt_decomposition_sorting.py](2199_sqrt_decomposition_sorting.py) | PyPy 3.10 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B) log(B+1) + QB) | AC | 1.125 s | 17704 KB |
| [2199_sqrt_decomposition_sorting.rs](2199_sqrt_decomposition_sorting.rs) | Rust 1.75 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 0.703 s | 7536 KB |
